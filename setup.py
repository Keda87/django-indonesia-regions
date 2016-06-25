import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-indonesia-regions',
    version='1.0.0-rc.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Pluggable django providing indonesian regions model including the initial data',
    long_description=README,
    url='https://github.com/Keda87/django-indonesia-regions',
    author='Adiyat Mubarak',
    author_email='adiyatmubarak@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)