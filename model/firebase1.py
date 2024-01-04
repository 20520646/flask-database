import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2


def get_firebase(url="data/9.jpg" ):
    cred = credentials.Certificate("sever.json")
    app = firebase_admin.initialize_app(cred, {'storageBucket': 'esp-32-cam-demo.appspot.com'})
    bucket = storage.bucket()
    
    blob_path = url
    blob = bucket.get_blob(blob_path)

    if blob is not None:
        img_bytes = blob.download_as_bytes()
        arr = np.frombuffer(img_bytes, np.uint8)
        if arr.size > 0:
            # Decode the image using OpenCV
            img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    return img
