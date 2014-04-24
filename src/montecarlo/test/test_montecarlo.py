"""
Test MonteCarlo DOE generator.
"""

import logging
import unittest

from montecarlo.montecarlo import MonteCarlo

from openmdao.main.api import Assembly
from openmdao.lib.drivers.api import DOEdriver
from openmdao.lib.casehandlers.api import ListCaseRecorder

from openmdao.examples.simple.paraboloid import Paraboloid

from numpy import random, array, std


class MonteCarlo_Test_Assembly(Assembly):

    def configure(self):
        self.add('paraboloid', Paraboloid())

        self.add('driver', DOEdriver())
        self.driver.log_level = logging.INFO

        # Configure the generator.
        self.driver.DOEgenerator = MonteCarlo()
        self.driver.DOEgenerator.num_samples = 5000
        self.driver.DOEgenerator.dist_types = {
            'Default':random.uniform, 'y':random.standard_normal}
        self.driver.DOEgenerator.dist_args = {'Default':[0, 1], 'y':[]}
        self.driver.DOEgenerator.parameters = ['x', 'y']

        # Configure driver parameters.
        self.driver.add_parameter('paraboloid.x', low=0, high=1)
        self.driver.add_parameter('paraboloid.y', low=0, high=1)

        #tell the DOEdriver to also record f_xy.
        self.driver.add_response('paraboloid.f_xy')

        #Simple recorder which stores the cases in memory.
        self.recorders = [ListCaseRecorder(),]

        self.driver.workflow.add('paraboloid')


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.doe = MonteCarlo_Test_Assembly()
        self.doe.run()

        self.data = self.doe.recorders[0].get_iterator()

        self.x = array([case['paraboloid.x'] for case in self.data])
        self.y = array([case['paraboloid.y'] for case in self.data])
        self.z = array([case['paraboloid.f_xy'] for case in self.data])

    def test_x(self):
        # make sure the uniform distribution is around x
        self.assertAlmostEqual(self.x.mean(), 0.5, places=1)

        #make sure the max of the uniform distribution is below 1, but close to it
        x_max = max(self.x)

        self.assertAlmostEqual(x_max, 1.0, places=1)
        self.assertTrue((x_max < 1.0))

        #make sure the max of the uniform distribution is below 1, but close to it
        x_min = min(self.x)

        self.assertAlmostEqual(x_min, 0.0, places=1)
        self.assertTrue((x_min > 0.0))

    def test_y(self):
        #Make sure mean ~ 0 and std. dev ~ 1 for standard normal dist.
        self.assertAlmostEqual(self.y.mean(), 0.0, places=1)
        self.assertAlmostEqual(std(self.y), 1, places=1)


if __name__ == "__main__":
    unittest.main()
