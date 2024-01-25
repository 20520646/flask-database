import cv2
from time import sleep
count = 51
cap = cv2.VideoCapture(0)
while  count <= 100:
    ret, frame =  cap.read()
    key = cv2.waitKey(10)
    # tempo = float(1)
    # sleep(tempo)
    # print("3")
    # sleep(tempo)
    # print("2")
    # sleep(tempo)
    # print("1")
    if not ret or key == ord('q'):
        break
    cv2.imwrite(f'train/20520438/{count}.jpg', frame)
    sleep(1)
    cv2.imshow(f'{count}',frame)
    print(count)
    count += 1
cv2.destroyAllWindows()
cap.release()