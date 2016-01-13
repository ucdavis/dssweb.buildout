from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='dssweb.facnavviews',
      version=version,
      description="DSS-specific views for EEA Faceted Navigation",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dssweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eea.facetednavigation',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
