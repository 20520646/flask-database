import sklearn
from sklearn.preprocessing import LabelEncoder, Normalizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from mtcnn import MTCNN
from numpy import load
from extract_faces import extract_face
from make_embeddings import get_embeddings
import pickle
from firebase1 import get_firebase
def train_model(faces, labels):
   
    in_encoder = Normalizer(norm ='l2')
    faces = in_encoder.transform(faces)
    out_encoder = LabelEncoder()
    out_encoder.fit(labels)

    # print(labels, type(labels))

    labels = out_encoder.transform(labels)
    # print(labels)

    model = SVC(kernel='linear', probability=True)
    model.fit(faces, labels)

    yhat_train = model.predict(faces)
    
    score_train = accuracy_score(labels, yhat_train)
    # print(labels, yhat_train)
    print(f'>>> Accuracy: {score_train*100}')
    
    return model, out_encoder

if __name__ == '__main__':
    url = './data_embeddings.npz'
    data = load(url)
    faces, labels = data['arr_0'], data['arr_1']
    # print(f'>>> Dataset: train={faces.shape[0]}')
    # model, out_encoder = train_model(faces, labels)
    # in_encoder = Normalizer(norm ='l2')
    # faces = in_encoder.transform(faces)
    out_encoder = LabelEncoder()
    out_encoder.fit(labels)

    # print(labels, type(labels))

    labels = out_encoder.transform(labels)
    with open('faces_classification.pkl',  'rb') as file:
       model = pickle.load(file)
    # with open('faces_classification.pkl',  'wb') as file:
    #     pickle.dump(model,file)
    print(labels)
    img = get_firebase()
    face, box = extract_face("",link = False, img = img)
    embedding = get_embeddings([face])

    yhat_class = model.predict(embedding)
    yhat_prop = model.predict_proba(embedding)
    class_index = yhat_class[0]
    print(class_index)
    class_probability = yhat_prop[0,class_index] * 100
    predict_name = out_encoder.inverse_transform(yhat_class)
    print("probability: ", class_probability)
    print("name: ", predict_name[0])

