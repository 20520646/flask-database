from mtcnn import MTCNN
import argparse
import tensorflow as tf
import cv2
from os.path import isdir
from os import listdir
from numpy import asarray
from numpy import savez_compressed
def extract_face(filename, required_size=(160, 160)):
    detector = MTCNN()
    print(">>> filename", filename)
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face = detector.detect_faces(img)
    print(">>> faces", face)
    arr=[x,y,width,height] = face[0]['box']
    face = img[y:y+height,x:x+width]
    face = cv2.resize(face, required_size, face)
    return face, arr

def load_faces(directory):
	faces = list()
	# enumerate files
	for filename in listdir(directory):
		# path
		path = directory + filename
		# get face
		face,_ = extract_face(path)
		# store
		faces.append(face)
	return faces

# load a dataset that contains one subdir for each class that in turn contains images
def load_dataset(directory):
	X, y = list(), list()
	# enumerate folders, on per class
	for subdir in listdir(directory):
		# path
		path = directory + subdir + '/'
		# skip any files that might be in the dir
		if not isdir(path):
			continue
		# load all faces in the subdirectory
		faces = load_faces(path)
		# create labels
		labels = [subdir for _ in range(len(faces))]
		# summarize progress
		print(f'>loaded {len(faces)} examples for class: {subdir}')
		# store
		X.extend(faces)
		y.extend(labels)
	return asarray(X), asarray(y)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-td', '--train_data', required=True)
    ap.add_argument('-vd', '--val_data', required=True)
    ap.add_argument('-sd', '--save_data', required=True)
    args = vars(ap.parse_args())
    trainX, trainy = load_dataset(args['train_data'])
    print(trainX.shape, trainy.shape)
    
    testX, testy = load_dataset(args['val_data'])
    savez_compressed(args['save_data'], trainX, trainy, testX, testy)
    