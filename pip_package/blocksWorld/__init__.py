# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

import importlib

from blocksWorld import *
from blocksWorld.draw import *
from blocksWorld.localTypes import *
from blocksWorld.polygon import *

globals().update(importlib.import_module('blocksWorld').__dict__)
