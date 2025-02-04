from vbo import VBO
from shader_program import ShaderProgram

#vertex array object
class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # cat vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])
        
        # road vao
        self.vaos['road'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['road'])
        
        # house vao
        self.vaos['house'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['house'])
        # house2 vao
        self.vaos['house2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['house2'])
        # grass vao
        self.vaos['grass'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['grass'])
        # tree vao
        self.vaos['tree'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['tree'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()