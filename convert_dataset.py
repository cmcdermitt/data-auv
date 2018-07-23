import numpy as np
import cv2
from PIL import Image

image_location = './images/'
annotation_location = './annotations/'

dataset = np.load('my_dataset.npz')

print(type(dataset))

print(len(dataset['images']))
print(len(dataset['boxes']))


for i, img_array in enumerate(dataset['images']):
    img= Image.fromarray(img_array)
    img.save(image_location + 'img%05d.jpg' % (i))

for i, entry in enumerate(dataset['boxes']):
    print(entry)
    with open(annotation_location + 'anno%05d.txt'% (i), 'w') as anno:
        for box in entry:
            for value in box:
                anno.write(str(value) + ' ')
            anno.write('\n')
    


#data format for boxes is [label, x_min, y_min, x_max, y_max]

