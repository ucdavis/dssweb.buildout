# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("version.txt")).read().strip()

setup(name='dssweb.theme.magic',
      version=version,
      description="Themes for Plone/Diazo powered sites",
      long_description=open(os.path.join("README.md")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
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
      namespace_packages=['dssweb','dssweb.theme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.theming',
          'webcouturier.dropdownmenu',
           'z3c.jbot',
      ],
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      )
