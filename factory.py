from PIL import Image, ImageDraw

from abc_builder import ABCBuilder


class Factory:
    def __init__(self, builder_cls):
        self.img = Image.new('RGB', (600, 400), 'white')
        self.idraw = ImageDraw.Draw(self.img)

        self.builder = builder_cls(self.img)
        self.header_text = 'Hi! Congratulations, you got: \n' + self.builder.header_text

    def add_header(self):
        self.idraw.text((20, 20), self.header_text, fill='black')

    def construct(self):
        self.builder.add_body()
        self.builder.add_wheels()
        self.builder.add_windows()
        self.builder.add_emblem()

        self.add_header()

    def get_result(self, res_type, filename=None):
        if res_type == '1':
            self.img.show()
        elif res_type == '2' and filename:
            self.builder.save(filename)
