# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("dssweb", "config", "version.txt")).read().strip()

setup(name='dssweb.config',
      version=version,
      description="Config Files for Dssweb Poject",

      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme psych mobile ucdavis',
      author='Carol McMasters-Stone',
      author_email='cbeck@ucdavis.edu',
      url='http://it.dss.ucdavis.edu/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dssweb',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
         
      ],
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      )
