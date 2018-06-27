# https://pypi.org/project/recordtype/

from recordtype import recordtype

Point = recordtype('Point', 'x y', default = 0)
Vertex = recordtype('Vertex', [('char', '+'), ('point', Point())])
