# -*- coding: utf-8 -*-
from setuptools import setup
import codecs

with codecs.open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

packages = \
['newspaper_wrapper', 'newspaper_wrapper.videos']

package_data = \
{'': ['*'], 'newspaper_wrapper': ['resources/misc/*', 'resources/text/*']}

install_requires = \
['Pillow>=7.1.2,<8.0.0',
 'PyYAML>=5.3.1,<6.0.0',
 'beautifulsoup4>=4.9.0,<5.0.0',
 'cssselect>=1.1.0,<2.0.0',
 'feedfinder2>=0.0.4,<0.0.5',
 'feedparser>=5.2.1,<6.0.0',
 'jieba3k>=0.35.1,<0.36.0',
 'lxml>=4.5.0,<5.0.0',
 'nltk>=3.5,<4.0',
 'pythainlp>=2.1.4,<3.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'tinysegmenter>=0.4,<0.5',
 'tldextract>=2.2.2,<3.0.0']

setup_kwargs = {
    'name': 'newspaper3k-wrapper',
    'version': '0.1.0',
    'description': 'Wrapper over newspaper3k library to provide support to nepali sites',
    'long_description': readme,
    'author': 'hemanta212',
    'author_email': 'sharmahemanta.212@gmail.com',
    'maintainer': None,
    'license':'MIT',
    'maintainer_email': None,
    'url': 'https://github.com/pykancha/newspaper3k_wrapper',
    'packages': packages,
    'zip_safe': False,
    'include_package_data':True,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
