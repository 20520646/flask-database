import sklearn
from extract_faces import extract_face
from make_embeddings import get_embeddings
import pickle
import cv2

if __name__ == '__main__':
    with open('faces_classification.pkl',  'rb') as file:
        model = pickle.load(file)

        file_name = './datasets/test/5.jpeg'
        face, box = extract_face(file_name)
        embedding = get_embeddings([face])

        yhat_class = model.predict(embedding)
        yhat_prop = model.predict_proba(embedding)
        class_index = yhat_class[0]
        class_probability = yhat_prop[0,1] * 100
        print("probability: ", class_probability)
        img = cv2.imread(file_name)
        rate = img.shape[0]/img.shape[1]
        cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0,0,255), 3)
        cv2.putText(img, f'{class_index}, {class_probability:0.3f}', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1*rate, color = (0,255,0))
        cv2.imshow(class_index, img)
        cv2.waitKey(0)