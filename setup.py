# coding: utf-8

from setuptools import setup, find_packages

version = '0.1.4'
readme = open('README.rst').read()

setup(name='eispatterns-examples',
      version=version,
      description='Enterprise Information Systems Patterns Examples',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='enterprise information systems, business process, design patterns',
      author='Me and my posse',
      author_email='ratembr@gmail.com',
      url='https://github.com/ratem/eispatterns-examples',
      license='MIT License',
      packages=find_packages()
      )

