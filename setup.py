import re

from setuptools import find_packages, setup


with open('netsgiro/__init__.py') as fh:
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))


with open('README.rst') as fh:
    long_description = fh.read()


setup(
    name='netsgiro',
    version=metadata['version'],
    description='File parsers for Nets AvtaleGiro and OCR Giro',
    long_description=long_description,
    url='https://github.com/otovo/python-netsgiro',
    author='Otovo AS',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='avtalegiro ocr giro',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
    ],
    extras_require={
        'dev': [
            'check-manifest',
            'flake8',
            'flake8-import-order',
            'mypy',
            'pytest',
            'tox',
        ],
    },
)
