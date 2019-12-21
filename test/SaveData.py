from PathsModule import AggregateOutputPath
import os
import json

def Save(data, FileName):
    '''
        This function saves all data into a Json file to be used later to generate an exact replica to data set.
    :return:
        Nothing
    '''

    JsonFileName1 = FileName  # modified data file name.
    JsonFilepath1 = os.path.join(AggregateOutputPath, JsonFileName1)

    try:
        with open(JsonFilepath1, 'w') as f:
            json.dump(data, f, indent=1, sort_keys=True)
    except FileNotFoundError:
        print("couldn't save the file")
    return print('done!')
