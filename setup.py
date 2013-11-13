#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Carlin Kersch',
 'author_email': 'ckersch@asdl.gatech.edu',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'DOEgenerator for Monte Carlo Simulation',
 'download_url': '',
 'entry_points': '[openmdao.doegenerator]\nmontecarlo.montecarlo.MonteCarlo=montecarlo.montecarlo:MonteCarlo\n\n[openmdao.component]\ntest_montecarlo.MonteCarlo_Test_Assembly=test_montecarlo:MonteCarlo_Test_Assembly\n\n[openmdao.container]\ntest_montecarlo.MonteCarlo_Test_Assembly=test_montecarlo:MonteCarlo_Test_Assembly',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao, Monte Carlo Simulation'],
 'license': 'GNU General Public License, version 2',
 'maintainer': 'Carlin Kersch',
 'maintainer_email': 'ckersch@asdl.gatech.edu',
 'name': 'montecarlo',
 'package_data': {'montecarlo': ['sphinx_build/html/index.html',
                                 'sphinx_build/html/.buildinfo',
                                 'sphinx_build/html/py-modindex.html',
                                 'sphinx_build/html/objects.inv',
                                 'sphinx_build/html/searchindex.js',
                                 'sphinx_build/html/search.html',
                                 'sphinx_build/html/pkgdocs.html',
                                 'sphinx_build/html/usage.html',
                                 'sphinx_build/html/genindex.html',
                                 'sphinx_build/html/srcdocs.html',
                                 'sphinx_build/html/_sources/usage.txt',
                                 'sphinx_build/html/_sources/pkgdocs.txt',
                                 'sphinx_build/html/_sources/index.txt',
                                 'sphinx_build/html/_sources/srcdocs.txt',
                                 'sphinx_build/html/_static/plus.png',
                                 'sphinx_build/html/_static/comment-bright.png',
                                 'sphinx_build/html/_static/comment.png',
                                 'sphinx_build/html/_static/down-pressed.png',
                                 'sphinx_build/html/_static/sidebar.js',
                                 'sphinx_build/html/_static/doctools.js',
                                 'sphinx_build/html/_static/ajax-loader.gif',
                                 'sphinx_build/html/_static/default.css',
                                 'sphinx_build/html/_static/down.png',
                                 'sphinx_build/html/_static/jquery.js',
                                 'sphinx_build/html/_static/underscore.js',
                                 'sphinx_build/html/_static/minus.png',
                                 'sphinx_build/html/_static/up-pressed.png',
                                 'sphinx_build/html/_static/up.png',
                                 'sphinx_build/html/_static/pygments.css',
                                 'sphinx_build/html/_static/searchtools.js',
                                 'sphinx_build/html/_static/file.png',
                                 'sphinx_build/html/_static/basic.css',
                                 'sphinx_build/html/_static/websupport.js',
                                 'sphinx_build/html/_static/comment-close.png',
                                 'sphinx_build/html/_modules/index.html',
                                 'sphinx_build/html/_modules/montecarlo/montecarlo.html',
                                 'test/test_montecarlo.py']},
 'package_dir': {'': 'src'},
 'packages': ['montecarlo'],
 'url': '',
 'version': '0.3.3',
 'zip_safe': False}


setup(**kwargs)

