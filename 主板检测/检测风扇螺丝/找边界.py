import cv2
import numpy as np

image = cv2.imread(r'C:\Users\24031\Desktop\1.jpg')  # a black objects on white image is better
gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
thresh = cv2.Canny(image, 128, 256)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


def draw_min_rect_circle(img, cnts):  # conts = contours
    img = np.copy(img)

    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # blue

        min_rect = cv2.minAreaRect(cnt)  # min_area_rectangle
        min_rect = np.int0(cv2.boxPoints(min_rect))
        cv2.drawContours(img, [min_rect], 0, (0, 255, 0), 2)  # green

        # (x, y), radius = cv2.minEnclosingCircle(cnt)
        # center, radius = (int(x), int(y)), int(radius)  # for the minimum enclosing circle
        # img = cv2.circle(img, center, radius, (0, 0, 255), 2)  # red
    return img

# def draw_approx_hull_polygon(img, cnts):
#     img = np.copy(img)
#     # img = np.zeros(img.shape, dtype=np.uint8)
#     #
#     # cv2.drawContours(img, cnts, -1, (255, 0, 0), 2)  # blue
#     #
#     # epsilion = img.shape[0]/32
#     # approxes = [cv2.approxPolyDP(cnt, epsilion, True) for cnt in cnts]
#     # cv2.polylines(img, approxes, True, (0, 255, 0), 2)  # green
#     #
#     # hulls = [cv2.convexHull(cnt) for cnt in cnts]
#     # cv2.polylines(img, hulls, True, (0, 0, 255), 2)  # red
#
#     # 我个人比较喜欢用上面的列表解析，我不喜欢用for循环，看不惯的，就注释上面的代码，启用下面的
#     for cnt in cnts:
#         cv2.drawContours(img, [cnt, ], -1, (255, 0, 0), 2)  # blue
#
#         epsilon = 0.01 * cv2.arcLength(cnt, True)
#         approx = cv2.approxPolyDP(cnt, epsilon, True)
#         cv2.polylines(img, [approx, ], True, (0, 255, 0), 2)  # green
#
#         hull = cv2.convexHull(cnt)
#         cv2.polylines(img, [hull, ], True, (0, 0, 255), 2)  # red
#     return img
# #


def draw_approx_hull_polygon(img, cnts):
    img = np.copy(img)
    img = np.zeros(img.shape, dtype=np.uint8)

    cv2.drawContours(img, cnts, -1, (255, 0, 0), 2)  # blue

    min_side_len = img.shape[0] / 16  # 多边形边长的最小值 the minimum side length of polygon
    min_poly_len = img.shape[0] / 8  # 多边形周长的最小值 the minimum round length of polygon
    min_side_num = 3  # 多边形边数的最小值
    min_area = 16.0   # 多边形面积的最小值
    approxs = [cv2.approxPolyDP(cnt, min_side_len, True) for cnt in cnts]  # 以最小边长为限制画出多边形
    approxs = [approx for approx in approxs if cv2.arcLength(approx, True) > min_poly_len]  # 筛选出周长大于 min_poly_len 的多边形
    approxs = [approx for approx in approxs if len(approx) > min_side_num]  # 筛选出边长数大于 min_side_num 的多边形
    # approxs = [approx for approx in approxs if len(approx) < 8]  # 筛选出边长数大于 min_side_num 的多边形

    approxs = [approx for approx in approxs if cv2.contourArea(approx) > min_area]  # 筛选出面积大于 min_area_num 的多边形
    # Above codes are written separately for the convenience of presentation.

    cv2.polylines(img, approxs, True, (0, 255, 0), 2)  # green

    hulls = [cv2.convexHull(cnt) for cnt in cnts]
    # cv2.polylines(img, hulls, True, (0, 0, 255), 2)  # red
    return img


def run():
    image = cv2.imread(r'C:\Users\24031\Desktop\1.jpg')  # a black objects on white image is better

    # gray = cv2.cv2tColor(image.copy(), cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    thresh = cv2.Canny(image, 127, 255)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    imgs = \
    [
        image, thresh,
        draw_min_rect_circle(image, contours),
        draw_approx_hull_polygon(image, contours)
    ]

    for img in imgs:
        cv2.namedWindow("enhanced", 0)
        cv2.resizeWindow("enhanced", 1000, 750)
        cv2.imshow("enhanced", img)

        cv2.waitKey(0)


def run2():
    image = cv2.imread(r'C:\Users\24031\Desktop\1.jpg')  # a black objects on white image is better
    cv2.namedWindow("image", 0)
    cv2.createTrackbar('min', 'image', 0, 255, lambda x: None)
    cv2.createTrackbar('max', 'image', 0, 255, lambda y: None)
    # gray = cv2.cv2tColor(image.copy(), cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    minthreshold = 127
    maxthreshold = 255
    while(1):

        minthreshold = cv2.getTrackbarPos("num", "image")
        maxthreshold = cv2.getTrackbarPos("num", "image")
        thresh = cv2.Canny(image, minthreshold, maxthreshold)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img = draw_approx_hull_polygon(image, contours)
        # cv2.resizeWindow("image", 1000, 750)
        cv2.imshow("image", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break


if __name__ == '__main__':
    run2()
pass
