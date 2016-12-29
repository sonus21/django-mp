#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='django-mercadopago-simple',
    description='MercadoPago integration for django',
    author='Hugo Osvaldo Barrera',
    author_email='hbarrera@z47.io',
    url='https://gitlab.com/hobarrera/django-mercadopago',
    license='ISC',
    packages=find_packages(),
    long_description=open('README.rst').read(),
    install_requires=open('requirements.txt').readlines(),
    use_scm_version={'version_scheme': 'post-release'},
    setup_requires=['setuptools_scm'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
