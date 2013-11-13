
================
Package Metadata
================

- **author:** Carlin Kersch

- **author-email:** ckersch@asdl.gatech.edu

- **classifier**:: 

    Intended Audience :: Science/Research
    Topic :: Scientific/Engineering

- **description-file:** README.txt

- **entry_points**:: 

    [openmdao.doegenerator]
    montecarlo.montecarlo.MonteCarlo=montecarlo.montecarlo:MonteCarlo
    [openmdao.component]
    test_montecarlo.MonteCarlo_Test_Assembly=test_montecarlo:MonteCarlo_Test_Assembly
    [openmdao.container]
    test_montecarlo.MonteCarlo_Test_Assembly=test_montecarlo:MonteCarlo_Test_Assembly

- **keywords:** openmdao, Monte Carlo Simulation

- **license:** GNU General Public License, version 2

- **maintainer:** Carlin Kersch

- **maintainer-email:** ckersch@asdl.gatech.edu

- **name:** montecarlo

- **requires-dist:** openmdao.main

- **requires-externals:** numpy

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** DOEgenerator for Monte Carlo Simulation

- **version:** 0.3.2

