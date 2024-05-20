from rembg import remove
from PIL import Image

input_path = 'E:\downloads\photo_2024-04-03_00-12-09.jpg'
output_path = 'E:\downloads'
input_photo = Image.open(input_path)
output = remove(input_photo)
output.save(output_path)
print('done')
