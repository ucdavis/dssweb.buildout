import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '3.0.2.dev0'

long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
    + '\n'
    )


setup(name='dss.portlet.person',
      version=version,
      description="An editable person HTML portlet for Plone.",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      keywords='dss portlet person',
      author='Carol McMasters-Stone ',
      author_email='cbeck@ucdavis.edu',
      url='',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=["dss", 'dss.portlet'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
              'plone.app.testing',
          ]
      ),
      install_requires=[
          'setuptools',
          "plone.portlets",
          "plone.app.portlets",
          "plone.app.textfield",
          "plone.i18n",
          'zope.component',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
          'Zope2',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
