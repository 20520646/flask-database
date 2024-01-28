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
    train_faces, train_labels, test_faces, test_labels = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3'],
    train_embeddings = get_embeddings(train_faces)
    print(">>> Train shape: ", train_embeddings.shape)
    test_embeddings = get_embeddings(test_faces)
    print(">>> Test shape: ", test_embeddings.shape)
    file_name = 'data_embeddings.npz'
    savez_compressed(file_name, train_embeddings, train_labels, test_embeddings, test_labels)
    
if __name__ == '__main__':
    url = './data_faces.npz'
    makes_embeddings_file(url)
    
