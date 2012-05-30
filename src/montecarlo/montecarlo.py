""" DOEgenerator that performs a Monte Carlo Design of Experiments using user-defined
random distributions for each variable. Plugs into the DOEgenerator socket on a
DOEdriver."""

# pylint: disable-msg=E0611,F0401
from numpy import linspace,random,array,concatenate
from enthought.traits.api import HasTraits
from openmdao.lib.datatypes.api import Int, Dict, ListStr, Str
from openmdao.lib.casehandlers.api import ListCaseIterator
from openmdao.main.interfaces import implements, IDOEgenerator

class MonteCarlo(HasTraits):
    """ DOEgenerator that performs a random Design of Experiments with given
    distributions on all design variables. Plugs into the DOEgenerator socket on a 
    DOEdriver."""
    
    implements(IDOEgenerator)
    
    # pylint: disable-msg=E1101
    parameters = ListStr(iotype='in',
                       desc='A list of names of variables to be included '
                       'in the Monte Carlo dataset.')
    
    num_parameters = Int(0, iotype="in", desc="number of parameters in the DOE "
                                              "if the parameters are not explicitly defined")
    
    num_samples = Int(0, iotype="in", desc="number of total samples in "
                                              "the DOE")
    dist_types = Dict(key_trait=Str,
                      allow_none=True,
                      desc='Dictionary that provides mapping between '
                           'variables and the distribution type associated with '
                           'the variable in question .'
                      )    
    
    dist_args = Dict(key_trait=Str,
                          allow_none=True,
                          desc='Dictionary that provides mapping between variables and '
                          'arguments that should be passed to the surrogate model. Keys should '
                          'match those in the surrogate dictionary. Values should be lists. '
                          'Array sizes should be left blank (default to 1). Default key must have '
                          'blank size value.')
    
    def __init__(self, num_samples=None, *args, **kwargs):
    
        super(MonteCarlo, self).__init__(*args, **kwargs)
        
        self.num = 0
        
        if num_samples is not None: 
            self.num_samples = num_samples
        
    def __iter__(self):
        """Return an iterator over our sets of input values"""
        #if self.num_samples < 2: 
        #    raise ValueError("Uniform distributions must have at least 2 samples. num_samples is set to less than 2")
        return self
                                           
    def next(self):
        if self.num < self.num_samples:
            self.num = self.num+1
            #create list of putputs. Append items to this as they are created
            self.outputs = []
            if self.parameters != []:                
                #Create iteration output for explicit parameters
                for parameter in self.parameters:
                    if parameter in self.dist_types:
                        #make sure that dist_args is given
                        if parameter not in self.dist_args:
                            raise Exception("Parameters with specified distributions must "
                                            "be supplied with input arguments in dist_Args")
                        #compute values for given parameter. Append this to output list.
                        self.p_out = self.dist_types[parameter](*self.dist_args[parameter])
                        if type(self.p_out) == 'numpy.ndarray':
                            self.outputs += p_out.tolist()
                        else:
                            self.outputs.append(self.p_out)
                    else:
                        self.p_out = self.dist_types['Default'](*self.dist_args['Default'])
                        self.outputs.append(self.p_out)
                        
            else: #parameters is none: default to num_parameters and utilize defaults
                self._args = self.dist_args['Default'][:]
                self._args.append(self.num_parameters)
                self.outputs = self.dist_types['Default'](*self._args)
            self._outputs = array(self.outputs)
            return self._outputs
        else:
            raise StopIteration()

if __name__ == "__main__":
    from numpy import random
    from montecarlo import MonteCarlo
    
    _test = MonteCarlo()
    _test.num_parameters = 7
    _test.parameters = ['x','y','z','u']
    _test.num_samples = 10
    _test.dist_types = {'Default':random.uniform,'y':random.standard_normal}
    _test.dist_args = {'Default':[0,1],'y':[]}
    for iters in _test:
        A =  iters
        print(A)