import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100,50), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0,255,255))
cv2.putText(img, "Mercury", (120,240), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(127,127,127))
cv2.putText(img, "Venus", (190,260), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,255))
cv2.putText(img, "Earth", (290,270), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(255,170,86))
cv2.putText(img, "Mars", (390,250), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(51,146,255))
cv2.putText(img, "Jupiter", (550,375), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(86,170,255))
cv2.putText(img, "Saturn", (750,310), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(86,255,255))
cv2.putText(img, "Uranus", (970,290), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(255,255,86))
cv2.putText(img, "Neptune", (1110,280), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(191,0,0))


cv2.imshow("output",img)
cv2.waitKey(0)