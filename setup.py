import os
from setuptools import setup

setup(name='awscli-v1-completer',
      version='0.1.1',
      description='awscli v1 completer with server and client',
      author='Jiho Jung',
      author_email='jihojung88' '@' 'gmail.com',
      license="Apache License 2.0",
      #scripts=['bin/aws_bash_completer', 'bin/awscli-v1-completer'],
      scripts=['bin/awscli-v1-completer'],
      packages=['awscli_v1_completer'],
      # packages=find_packages(exclude=['tests*']),
      python_requires=">= 3.7",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
      ],

      )
