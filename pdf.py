# importing modules
from pdf2image import convert_from_path

""" img = convert_from_path('agni3.pdf', 300, poppler_path = r'C:/Program Files/poppler-0.68.0/bin')

img[0].save('test.jpg', 'JPEG')
print(range(len(img)))
print(range(1)) """

for i in [1 ,2, 3]:
    img = convert_from_path(f'agni{i}.pdf', 300, poppler_path = r'C:/Program Files/poppler-0.68.0/bin')

    img[0].save(f'agni{i}.jpg', 'JPEG')

    
