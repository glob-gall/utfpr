import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures[1] = self.get_texture(path='textures/img_1.png')
        self.textures[2] = self.get_texture(path='textures/img_2.png')
        self.textures['cat'] = self.get_texture(path='objects/gato/Cat_diffuse.jpg')
        self.textures['road'] = self.get_texture(path='objects/road/road.jpg')
        self.textures['house'] = self.get_texture(path='objects/house/texture-1.jpg')
        self.textures['house2'] = self.get_texture(path='objects/house/texture-2.jpg')
        self.textures['grass'] = self.get_texture(path='objects/grass/10450_Rectangular_Grass_Patch_v1_Diffuse.jpg')
        self.textures['tree'] = self.get_texture(path='objects/tree/10447_Pine_Tree_v1_Diffuse.jpg')


    def get_texture(self, path):
        
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]