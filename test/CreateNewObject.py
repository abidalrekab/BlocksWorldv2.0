
def CreateNewObject(data, name, center,vertex, radii, nrVertices, rotation):
    '''
    This function under construction
    :param name:
    :param layer:
    :param center:
    :param radii:
    :param nrVertices:
    :param rotation:
    :return:
    '''
    return data['layer0'][0]["AggrObjects"].append(
        {'GUID': name, 'center': center, "Vertices": vertex, 'radii': radii, 'nrVertices': nrVertices, 'orientation': rotation})
