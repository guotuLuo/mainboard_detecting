import cv2
import numpy
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\24031\Desktop\2.jpg')
template = cv2.imread(r'C:\Users\24031\Desktop\template1up.jpg')
h, w = template.shape[:2]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# 先使用计算平方的方法匹配模板
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
# 得到计算值的最大值、最小值以及它们的左上角的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# 运用所有方法
for meth in methods:
    img2 = img.copy()

    # 匹配方法的真值
    method = eval(meth)
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED，取最小值；否则取最大值。
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 画矩形
    cv2.rectangle(img2, top_left, bottom_right, 255, 10)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

