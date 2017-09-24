
import cv2

img = cv2.imread('pandas.jpg')
a = img.shape
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, '4', (a[0] - 200, 100), font, 2, (0, 0, 255), 4)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyWindow('image')
cv2.imwrite('pandas_number.jpg', img)
