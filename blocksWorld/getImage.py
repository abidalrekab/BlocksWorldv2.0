from PIL import Image, ImageDraw

def getImage(imageMode, imageSize, imageBackground):

    """
    This function is to generate an image with a specific background, mode, and size
    inputs: plotting mode, image size in tuple (x,y), background color 'while' for ex.
    returns: image , and canvas objects

    """

    image = Image.new(imageMode, imageSize, imageBackground)
    canvas = ImageDraw.Draw(image)

    return image, canvas