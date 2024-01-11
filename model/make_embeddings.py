from keras_facenet import FaceNet 
from numpy import load, savez_compressed

#get embeddings vector in facses of user
def get_embeddings(faces):
    embedder = FaceNet()
    embeddings = embedder.embeddings(faces)
    print(embeddings)
    return embeddings

#make a file contains embeding vectors
def makes_embeddings_file(url):
    data = load(url)
    faces, labels = data['arr_0'], data['arr_1']
    embeddings = get_embeddings(faces)
    print(">>> Train shape: ", embeddings.shape)
    file_name = 'data_embeddings.npz'
    savez_compressed(file_name, embeddings, labels)
    
if __name__ == '__main__':
    url = './data_faces.npz'
    makes_embeddings_file(url)
    
    
