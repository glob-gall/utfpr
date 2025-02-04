import numpy as np
from base import BaseVBO
import pywavefront
from models.Tree import TreeVBO
from models.Cat import CatVBO
from models.House import HouseVBO,House2VBO
from models.Road import RoadVBO
from models.Cube import CubeVBO
from models.Grass import GrassVBO
#virtual buffer object
class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['cat'] = CatVBO(ctx)
        self.vbos['road'] = RoadVBO(ctx)
        self.vbos['house'] = HouseVBO(ctx)
        self.vbos['house2'] = House2VBO(ctx)
        self.vbos['grass'] = GrassVBO(ctx)
        self.vbos['tree'] = TreeVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

















