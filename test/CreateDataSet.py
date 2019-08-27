

def DataSet():
    """
    inputs:
        - DataSetID is a unique name for the data set using Hash function so reperducing the dataset
    again won't be ambiguous.
        - nrFrame is the number of frames per second for the animation section.
        - nrShapes defines how many shape there are in a single image.
        - TyShapes defines a kind of shapes that are drawn { poly1 (a point ) , poly2 (a line ), poly3...so on}
        - Transformation is a list of all transformation that are being used to generate the dataset
    :return:
        - a complete data set with the ability to save, load, delete or insert.
        - ability to aggregate objects.
    """

    imageExt = ".jpg"                                   # extension
    imageDimensions = [320, 480]                        # length X width
    imageBackground = "white"                           # background

    def ___init__(self, DataSetID , nrFrames , nrShapes, TyShapes , Transformations = []):
        self.name = DataSetID
        self.nrframes = nrFrames                        # the number of frames per second
        self.nrshapes = nrShapes                        # the number of shapes to be created
        self.Tyshapes = TyShapes                        # ['poly1','20%','poly2','80%']
        self.Transformations = Transformations          # rotation, translation, scaling
        self.edges = "True"                             # draw edges True or False
        self.overlap = 'Disable'

    def imageName(self, name):
        return name + imageExt

    def createShape():
        """


        :return:
        """
        pass

    def aggregate():
        """


        :return:
        """
        pass

    def ComputeCenterOfMass():
        pass

    def Create(NrImages, ):
        pass

    def save():
        """


        :return:
        """
        pass

    def load():
        """


        :return:
        """
        pass

    def delete():
        """

        :return:
        """
        pass

    def insert():
        """


        :return:
        """
        pass

