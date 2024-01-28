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
def train_model(train_faces, train_labels, test_faces, test_labels):
   
    in_encoder = Normalizer(norm ='l2')
    train_faces = in_encoder.transform(train_faces)
    test_faces = in_encoder.transform(test_faces)
    print('Dataset: train=%d, test=%d' % (train_faces.shape[0], test_faces.shape[0]))

    out_encoder = LabelEncoder()
    out_encoder.fit(train_labels)

    # print(labels, type(labels))

    train_labels = out_encoder.transform(train_labels)
    test_labels = out_encoder.transform(test_labels)

    # print(labels)

    model = SVC(kernel='linear', probability=True)
    model.fit(train_faces, train_labels)

    yhat_train = model.predict(train_faces)
    yhat_test = model.predict(test_faces)
    score_train = accuracy_score(train_labels, yhat_train)
    score_test = accuracy_score(test_labels, yhat_test)

    # print(labels, yhat_train)
    print(f'>>> Accuracy train: {score_train*100}')
    print(f'>>> Accuracy test: {score_test*100}')
    
    return model, out_encoder

if __name__ == '__main__':
    url = './data_embeddings.npz'
    data = load(url)
    train_faces, train_labels, test_faces, test_labels = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    # print(f'>>> Dataset: train={faces.shape[0]}')
    model, out_encoder = train_model(train_faces, train_labels, test_faces, test_labels)
    # in_encoder = Normalizer(norm ='l2')
    # faces = in_encoder.transform(faces)
    # out_encoder = LabelEncoder()
    # out_encoder.fit(train_labels)

    # print(labels, type(labels))

    train_labels = out_encoder.transform(train_labels)
    # with open('faces_classification.pkl',  'rb') as file:
    #    model = pickle.load(file)
    with open('faces_classification.pkl',  'wb') as file:
        pickle.dump(model,file)
    print(train_labels)
    # img = get_firebase()
    # face, box = extract_face("",link = False, img = img)
    img = '/home/kltnofpandn/Desktop/flask-database/dataset/test/20520646/45.jpg'
    face, box = extract_face(img)
    embedding = get_embeddings([face])

    yhat_class = model.predict(embedding)
    yhat_prop = model.predict_proba(embedding)
    class_index = yhat_class[0]
    print(class_index)
    class_probability = yhat_prop[0,class_index] * 100
    predict_name = out_encoder.inverse_transform(yhat_class)
    print("probability: ", class_probability)
    print("name: ", predict_name[0])

#port ip public 42.116.6.42:8276 8287
    #ip nooij bo 192.168.4.170