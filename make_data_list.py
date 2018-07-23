import os

imagepath = 'images/'
annopath = 'annotations/'

images = sorted(os.listdir('./images'))
annotations = sorted(os.listdir('./annotations'))

imagepaths = [imagepath + i for i in images]
annopaths = [annopath + i for i in annotations]

with open('train.txt', 'w') as train:
    for image in imagepaths[:200]: #first 200 are for training, rest are for validation
        train.write(image + '\n')

with open('val.txt', 'w') as val:
    for anno in annopaths[200:]:
        val.write(anno + '\n')

with open('reltrain.txt', 'w') as reltrain:
    for line in zip(imagepaths, annopaths)[:200]:
        reltrain.write(str(line[0] + ' ' + str(line[1]) + '\n'))

with open('relval.txt', 'w') as relval:
    for line in zip(imagepaths, annopaths)[200:]:
        relval.write(str(line[0] + ' ' + str(line[1]) + '\n'))