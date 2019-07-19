#!/usr/bin/env python
"""
    This module helps with the tests.
"""
import os
import sys

crtScriptDir = os.path.dirname(sys.argv[0])
root = os.path.abspath(crtScriptDir)

outputPath = os.path.join(root, "data/output")
outputPath = os.path.abspath(outputPath)

referencePath = os.path.join(root, "data/reference")
referencePath = os.path.abspath(referencePath)

# fileType = '.png'

# Result image for draw
def FileName(name):
    return name + '.png'

def Validate(referenceFile, resultFile):
    # compare results agains reference data
    with open(resultFile, "rb") as result:
        with open(referenceFile, "rb") as reference:
            assert(reference.read() == result.read())
