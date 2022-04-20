from random import randint
from captcha.image import ImageCaptcha
import random

def randomTextGenerator():
    length = randint(5,7)
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

image = ImageCaptcha(width = 280, height = 90)

text = randomTextGenerator()

data = image.generate(text)

image.write(text, r'demo.png')
