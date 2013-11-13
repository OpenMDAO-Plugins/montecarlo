""" DOEgenerator that performs a Monte Carlo Design of Experiments using
user-defined random distributions for each variable. Plugs into the DOEgenerator
socket on a DOEdriver."""

# pylint: disable-msg=E0611,F0401
<<<<<<< HEAD
from numpy import linspace,random,array,concatenate
=======
from numpy import random, array
>>>>>>> 3f80dac93b701ee4d32c1ba6a99d750eed2d01ec
from traits.api import HasTraits
from openmdao.lib.datatypes.api import Int, Dict, Str, List
from openmdao.main.interfaces import implements, IDOEgenerator


class MonteCarlo(HasTraits):
    """ DOEgenerator that performs a random Design of Experiments with given
    distributions on all design variables. Plugs into the DOEgenerator socket
    on a DOEdriver."""

    implements(IDOEgenerator)

    # pylint: disable-msg=E1101
    parameters = List(Str, iotype='in',
                      desc='A list of names of variables to be included '
                           'in the Monte Carlo dataset.')

    num_parameters = Int(0, iotype="in",
                         desc="number of parameters in the DOE "
                              "if the parameters are not explicitly defined")

    num_samples = Int(0, iotype="in", desc="number of total samples in the DOE")

    dist_types = Dict(key_trait=Str,
                      allow_none=True,
                      desc='Dictionary that provides mapping between '
                           'variables and the distribution type associated with '
                           'the variable in question .')

    dist_args = Dict(key_trait=Str,
                     allow_none=True,
                     desc='Dictionary that provides mapping between variables '
                          'and arguments that are required to define their '
                          'distributions. Keys should match those in '
                          'dist_types. Values should be lists.')

    def __init__(self, num_samples=None):
        super(MonteCarlo, self).__init__()
        self.num = 0
        if num_samples is not None:
            self.num_samples = num_samples

    def __iter__(self):
        """Return an iterator over our sets of input values"""
        return self

    def next(self):
        """Return next set of input values"""
        if self.num < self.num_samples:
            self.num += 1
            #create list of putputs. Append items to this as they are created
            outputs = []
            if self.parameters:
                #Create iteration output for explicit parameters
                for parameter in self.parameters:
                    if parameter in self.dist_types:
                        #make sure that dist_args is given
                        if parameter not in self.dist_args:
                            raise Exception("Parameters with specified distributions must "
                                            "be supplied with input arguments in dist_args")
                        #compute values for given parameter. Append this to output list.
                        p_out = self.dist_types[parameter](*self.dist_args[parameter])
                    else:
                        p_out = self.dist_types['Default'](*self.dist_args['Default'])

                    if type(p_out) == 'numpy.ndarray':
                        outputs += p_out.tolist()
                    else:
                        outputs.append(p_out)

            else: #parameters is none: default to num_parameters and utilize defaults
                args = self.dist_args['Default']
                args.append(self.num_parameters)
                outputs = self.dist_types['Default'](*args)
            return array(outputs)
        else:
            raise StopIteration()


if __name__ == "__main__":
    _test = MonteCarlo()
    _test.num_parameters = 7
    _test.parameters = ['x', 'y', 'z', 'u']
    _test.num_samples = 10
    _test.dist_types = {'Default':random.uniform, 'y':random.standard_normal}
    _test.dist_args = {'Default':[0, 1], 'y':[]}
    for iters in _test:
        A =  iters
        print(A)
