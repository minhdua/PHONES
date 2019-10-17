import os
pathImage = 'data/phones/'
pathLabel = 'data/labels'

listImage = os.listdir(pathImage)
listLabel = os.listdir(pathLabel)

listImage = [f.split('.')[0] for f in listImage]
listLabel = [f.split('.')[0] for f in listLabel]

images = [f for f in listImage if f not in listLabel]

for img in images:
	imgDelete = pathImage + img + '.jpg'
	os.remove(pathImage + img + '.jpg')
