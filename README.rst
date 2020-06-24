Copyright (c) 2020 Mohamed Abidalrekab, Dan Petre

The MIT License (MIT)

About This Project
##################

BlocksWorld is a tool for generating simple test images.

Core features
=============

* generate simple test image that resemble:
- Different basic objects that form a complex entity like a car, House, Bicycle ,.... etc.
- Objects can be generated based on four parameters:
    - Distortion ( with precentage of 0 ( no distortion ) to 1.0 which heavly distorted.
    - Missing or removing sub-part of an entity.
    - scale (0.5x - 5x )
    - Orientation ( 0 - 360 )

Supported platforms
===================

* Ubuntu 16.04, Python 3.5+

Might work on other configurations however at this time the focus will be on a single platform until the project matures a bit.

Build from source prerequisites
===============================

* Python 3.5+

.. code-block:: bash

    $ sudo apt install python3-pip
    $ sudo apt install python3-setuptools
    $ pip3 install wheel

Similarly, for those who like to experiment:

* Python 2.7+

.. code-block:: bash

    $ sudo apt install python-setuptools
    $ sudo apt install python-pip
    $ pip install wheel

Build wheel:

`./build.sh`.

Install locally built wheel:

`$ pip install --user dist/*`

or, if your pip doesn't automatically use python3:

`$ python3 -m pip install --user dist/*`

Notice the use of the `--user` option. You can install system wide using `sudo` but the project is still in very early stages so installing as user can keep your system files clean(er).

Resources
=========

* Website:
* Code: `https://github.com/takanokage/blocksWorld <https://github.com/takanokage/blocksWorld>`_
* Documentation: `https://github.com/takanokage/blocksWorld/wiki <https://github.com/takanokage/blocksWorld/wiki>`_
* License: `The MIT license <https://opensource.org/licenses/MIT>`_
