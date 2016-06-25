import os
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-indonesia-regions',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Pluggable django providing indonesian regions model including the initial data',
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