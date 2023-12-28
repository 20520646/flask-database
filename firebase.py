import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2

cred = credentials.Certificate("./sever.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'esp-32-cam-demo.appspot.com'})
bucket = storage.bucket()

blob_path = "data/11.jpg"
blob = bucket.get_blob(blob_path)

if blob is not None:
    print("Blob exists. Downloading image...")
    try:
        # Download the image as a bytes array
        img_bytes = blob.download_as_bytes()

        # Convert the bytes array to a NumPy array
        arr = np.frombuffer(img_bytes, np.uint8)

        # Check if the array is not empty
        if arr.size > 0:
            # Decode the image using OpenCV
            img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

            # Display the image
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Error: Empty image data")
    except Exception as e:
        print(f"Error downloading or decoding image: {e}")

else:
    print(f"Error: Blob '{blob_path}' does not exist.")