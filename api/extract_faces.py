from mtcnn import MTCNN
from os import listdir
from os.path import isdir
from numpy import asarray, savez_compressed
from mtcnn import MTCNN
import cv2

#init detector
detector = MTCNN()

#extract faces in image
def extract_face(file_name, required_size = (160,160), link = True, img = None):
    #read image
    if link:
        img = cv2.imread(file_name)
    else:
        img = img
    #convert image BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #detect face in image
    faces = detector.detect_faces(img)
    #check if image has not any face, function will return empty list
    if faces == []:
        return faces, []
    #extract face region
    arr = [x,y,w,h] = faces[0]['box']
    face = img[y:y+h, x:x+w]
    #resize image to require size (160 x 160)
    face = cv2.resize(face, required_size, face)
    return face, arr

def load_faces(directory):
    #init list face
    faces = []
    # loop to extract face in image
    for file_name in listdir(directory):
        path = directory + file_name
        print('>>> ',path)
        face, arr = extract_face(path)
        if arr == []:
            continue
        faces.append(face)
    return faces

def load_dataset(directory):
    #init list X contain list face of user and Y have labels of faces
    X, Y = [], []
    #loop to extract faces of user and append it to X, its label to Y
    for subdir in listdir(directory):
        path = directory + '/' + subdir + '/'
        if not isdir(path):
            print('>>> ',path)
            continue
        print('>>> ',path)
        faces = load_faces(path)
        labels = [subdir for _ in range(len(faces))]
        print(f'>>> loaded {len(faces)} examples for class: {subdir}')
        X.extend(faces)
        Y.extend(labels)
    return asarray(X), asarray(Y)

if __name__ == '__main__':

    directory = './dataset/train'
    train_data, train_labels = load_dataset(directory)
    print(train_data.shape, train_labels.shape)

    directory = './dataset/test'
    test_data, test_labels = load_dataset(directory)
    print(test_data.shape, test_labels.shape)

    file_name = './data_faces.npz'

    savez_compressed(file_name, train_data, train_labels,  test_data, test_labels)
