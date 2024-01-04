from keras_facenet import FaceNet
from numpy import load, savez_compressed
import argparse

def get_embedding(faces):
    embedder = FaceNet()
    embeddings = embedder.embeddings(faces)
    print(faces)

    return embeddings

def load_embedding_files(args):
    data = load('./6_faces_dataset.npz')
    trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    newTrainX = get_embedding(trainX)
    newTestX = get_embedding(testX)

    print(">>> New Train shape", newTrainX.shape, newTestX.shape)
    print(">>> Old Train shape",trainX.shape, testX.shape)
    savez_compressed(args['face_embedding'], newTrainX, trainy, newTestX, testy)
if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument('-fe', '--face_embedding', required=True)
    args = vars(ap.parse_args())
    load_embedding_files(args)

# Gets a detection dict for each face
# in an image. Each one has the bounding box and
# face landmarks (from mtcnn.MTCNN) along with
# the embedding from FaceNet.


# If you have pre-cropped images, you can skip the
# detection step.

