#!/usr/bin/env python
import os
import sys
from PIL import Image, ImageDraw

"""
    This module helps with the tests. 
    - provides root, output path, and reference path directories for 
        - draw
        - polygon
        - transform   
    - it includes three sub-functions:
        - fileName : which create the file name based on the test being performed and add extension to it. 
        - validate : compare whether the resultant file is resemble the reference file. 
        - getImage : create a image with specific requirements.
        - getPath : obtains the path to save the resultant image.
"""

crtScriptDir = os.path.dirname(sys.argv[0])
root = os.path.abspath(crtScriptDir)

outputPath = os.path.join(root, "output")
outputPath = os.path.abspath(outputPath)

referencePath = os.path.join(root, "reference")
referencePath = os.path.abspath(referencePath)

drawReferencePath = os.path.join(referencePath, "draw")
drawReferencePath = os.path.abspath(drawReferencePath)
drawOutputPath = os.path.join(outputPath, "draw")
drawOutputPath = os.path.abspath(drawOutputPath)

polygonOutputPath = os.path.join(outputPath, "polygon")
polygonOutputPath = os.path.abspath(polygonOutputPath)
polygonReferencePath = os.path.join(referencePath, "polygon")
polygonReferencePath = os.path.abspath(polygonReferencePath)

transformOutputPath = os.path.join(outputPath, "transform")
transformOutputPath = os.path.abspath(transformOutputPath)
transformReferencePath = os.path.join(referencePath, "transform")
transformReferencePath = os.path.abspath(transformReferencePath)


def fileName(name):

    """
    This function adds the provided name with an appropriate extension.
    """
    return name + '.png'


def validate(referenceFile, resultFile):

    """
    compare results against reference data
    inputs : the path to the reference file, path to resultant file
    returns : True or False
    """

    with open(resultFile, "rb") as result:
        with open(referenceFile, "rb") as reference:
            assert(reference.read() == result.read())


def getImage(imageMode, imageSize, imageBackground):

    """
    This function is to generate an image with a specific background, mode, and size
    inputs: plotting mode, image size in tuple (x,y), background color 'while' for ex.
    returns: image , and canvas objects

    """

    image = Image.new(imageMode, imageSize, imageBackground)
    canvas = ImageDraw.Draw(image)

    return image, canvas


def getPath(imageName):

    """
    This function is to set a path to resultant and reference files
    inputs: path to (drawing, polygon, transform) folder, path to (drawing, polygon, transform, depends on
     from which test is being called ) reference folder, image name!
    outputs: full path to resultant, and reference files.
    """

    if imageName.find('draw') != -1:

        resultFile = os.path.join(drawOutputPath, imageName)
        referenceFile = os.path.join(drawReferencePath, imageName)

    elif imageName.find('Polygon') != -1:

        resultFile = os.path.join(polygonOutputPath, imageName)
        referenceFile = os.path.join(polygonReferencePath, imageName)

    elif imageName.find('transform') != -1:

        resultFile = os.path.join(transformOutputPath, imageName)
        referenceFile = os.path.join(transformReferencePath, imageName)

    return resultFile, referenceFile
