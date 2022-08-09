from abc_builder import ABCBuilder
from config import img_paths
from PIL import Image, ImageDraw


class LadaBuilder(ABCBuilder):
    def __init__(self, image):
        self.img = image
        self.header_text = 'Fancy Lada! Almost working!!!!!'

    def save(self, filename):
        self.img.save(filename)

    def add_body(self):
        image_path = img_paths['lada']['body']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100))

    def add_wheels(self):
        image_path = img_paths['lada']['wheels']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_windows(self):
        pass

    def add_emblem(self):
        image_path = img_paths['lada']['emblem']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)


class VolkswagenBuilder(ABCBuilder):
    def __init__(self, image):
        self.img = image
        self.header_text = 'Nice Volkswagen! Not average at all!!!!!'

    def save(self, filename):
        self.img.save(filename)

    def add_body(self):
        image_path = img_paths['volkswagen']['body']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_wheels(self):
        image_path = img_paths['volkswagen']['wheels']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_windows(self):
        image_path = img_paths['volkswagen']['windows']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_emblem(self):
        image_path = img_paths['volkswagen']['emblem']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)


class AudiBuilder(ABCBuilder):
    def __init__(self, image):
        self.img = image
        self.header_text = "Pretty Audi! Real man's choice!!!!!"

    def save(self, filename):
        self.img.save(filename)

    def add_body(self):
        image_path = img_paths['audi']['body']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_wheels(self):
        image_path = img_paths['audi']['wheels']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_windows(self):
        image_path = img_paths['audi']['windows']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_emblem(self):
        image_path = img_paths['audi']['emblem']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)


class FerrariBuilder(ABCBuilder):
    def __init__(self, image):
        self.img = image
        self.header_text = 'Super expensive Ferrari! All the girls love you now!!!!!'

    def save(self, filename):
        self.img.save(filename)

    def add_body(self):
        image_path = img_paths['ferrari']['body']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_wheels(self):
        image_path = img_paths['ferrari']['wheels']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_windows(self):
        image_path = img_paths['ferrari']['windows']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)

    def add_emblem(self):
        image_path = img_paths['ferrari']['emblem']
        new_image = Image.open(image_path, 'r')
        self.img.paste(new_image, (100, 100), new_image)
