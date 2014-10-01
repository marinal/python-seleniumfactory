from setuptools import setup, find_packages

from selenium_factory import version

setup(
    name='python-seleniumfactory',
    version=version,
    description="Python SeleniumFactory",
    long_description="""
Simple interface factory to create Selenium objects, inspired by
SeleniumFactory interface from
https://github.com/infradna/selenium-client-factory.  The main objective is to
be able to have an automatic interface to easily run tests under the Bamboo
Sauce Ondemand plugin as well as local tests.  The factory object reads
environments variables setup by the Bamboo plugin and creates a remote Sauce
OnDemand session accordingly, otherwise it creates a local selenium
configuration.
Forked from the https://github.com/smartkiwi/SeleniumFactory-for-Python
    """,
    author='Matt Fair',
    author_email='matt.fair@gmail.com',
    maintainer='Erik LaBianca',
    maintainer_email='erik.labianca@wisertogether.com',
    url='https://github.com/syapse/python-seleniumfactory',
    license='Unknown',
    platforms=['any'],
    packages=find_packages(),
    install_requires=[
         'selenium',
         ],
    entry_points="""
     # -*- Entry points: -*-
     """,
)