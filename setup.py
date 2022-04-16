# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['scraper']

package_data = \
    {'': ['*']}

install_requires = \
    ['click',
     'drmaa',
     'gitpython',
     'numpy',
     'pandas',
     'salib>=1.3.8,<2.0.0',
     'tinydb>=4.0.0,<5.0.0',
     'tqdm',
     'xarray']


setup_kwargs = {
    'name': 'scraper',
    'version': '0.1.0',
    'description': 'Web scraper',
    'author': 'Akshit',
    'maintainer': None,
    'maintainer_email': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
