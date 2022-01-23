import cv2
import numpy

src = cv2.imread(r'C:\Users\24031\Desktop\1.jpg')
# cv2.namedWindow('src', 0)
# cv2.resizeWindow('src', 1000, 750)
# cv2.imshow('src', src)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)       # 转换成hsv色彩风格
mask = cv2.inRange(hsv, (35, 43, 46), (180, 30, 255))   # 利用inRange产生mask
# cv2.namedWindow('mask1', 0)
# cv2.resizeWindow('mask1', 1000, 750)
# cv2.imshow('mask1', mask)

mask = cv2.bitwise_not(mask)
# cv2.namedWindow('mask2', 0)
# cv2.resizeWindow('mask2', 1000, 750)
# cv2.imshow('mask2', mask)

timg1 = cv2.bitwise_and(src, src, mask=mask)
# cv2.namedWindow('timg1', 0)
# cv2.resizeWindow('timg1', 1000, 750)
# cv2.imshow('timg1', timg1)

# cv2.waitKey(0)

hsv1 = cv2.cvtColor(timg1, cv2.COLOR_BGR2HSV)       # 转换成hsv色彩风格
mask = cv2.inRange(hsv1, (0, 0, 221), (99, 255, 255))   # 利用inRange产生mask
cv2.namedWindow('mask3', 0)
cv2.resizeWindow('mask3', 1000, 750)
cv2.imshow('mask3', mask)

mask = cv2.bitwise_not(mask)
cv2.namedWindow('mask4', 0)
cv2.resizeWindow('mask4', 1000, 750)
cv2.imshow('mask4', mask)

timg1 = cv2.bitwise_and(timg1, timg1, mask=mask)
cv2.namedWindow('timg2', 0)
cv2.resizeWindow('timg2', 1000, 750)
cv2.imshow('timg2', timg1)
cv2.waitKey(0)

