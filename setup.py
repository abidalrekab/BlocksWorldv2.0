# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

from setuptools import setup, find_packages

setup(
    author = 'Dan Petre',
    author_email = 'danut.petre@gmail.com',
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5" ,
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    description = ("BlocksWorld is a tool for generating simple test images."),
    install_requires=['pillow', 'recordtype', 'numpy'],
    include_package_data=True,
    keywords = "blocks world",
    license = "MIT",
    long_description=open('README.rst').read(),
    name = "blocksWorld",
    packages=['blocksWorld'],
    url = "https://github.com/takanokage/blocksWorld",
    project_urls={
        'Documentation': 'https://github.com/takanokage/blocksWorld/wiki',
        'Source code': 'https://github.com/takanokage/blocksWorld',
        'Issues': 'https://github.com/takanokage/blocksWorld/issues',
        'Unittest': 'https://github.com/takanokage/blocksWorld/test'
        },
    version = '0.0.7',
    test_suite='test',
)
