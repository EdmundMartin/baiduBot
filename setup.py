from setuptools import setup

setup(
  name='baidubot',
  packages=['baidubot'],
  version='0.1.0',
  description='A simple Python module to scrape search results from Baidu',
  author='Edmund Martin',
  author_email='edmartin101@googlemail.com',
  url='https://github.com/EdmundMartin/',
  keywords=['baidu', 'scraping'],
  include_package_data=True,
  install_requires=['requests >= 2.0.0', 'beautifulsoup4>=4.6.0']
)