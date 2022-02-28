# coding:utf8
import base64

import cv2
import dlib
import numpy as np

'''
cv2.imshow("image", img_blank)  # 显示图片
cv2.waitKey(0)  # 窗口一直开着

'''
dector = dlib.get_frontal_face_detector()


def cv2_base64(image):
    base64_str = cv2.imencode('.jpg', image)[1].tostring()
    base64_str = base64.b64encode(base64_str)
    return base64_str


def image_to_base64(image_np):
    image = cv2.imencode('.jpg', image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1]

    return image_code


def base64_cv2(base64_str):
    print(base64_str)
    img_string = base64.b64decode(base64_str)
    nparr = np.fromstring(img_string, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image


def base64_to_image(base64_code):
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.fromstring(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)

    return img


def tranposeDector(imgstr, cnt=0):
    img = base64_to_image(imgstr)
    '''
    :param infile:  imread后的图片对象
    '''
    # 检测图上的人脸数
    try:
        dets = dector(img, 1)
    except Exception as ex:  # 脸部无法检测
        return (ex)
    # 身份证上只能有一个人脸，即为检查结果的第一个值
    if dets:
        face = dets[0]  # [(354, 96) (444, 186)] 检测出左上、右下两个点
        # 计算想裁取的图片的高度 下-上
        height = face.bottom() - face.top() + 60
        # 计算想裁取的图片的宽度 右-左
        width = face.right() - face.left() + 40
        # 以计算出的图片大小生成空白板
        img_blank = np.zeros((height, width, 3), np.uint8)
        # 将图片写入空白板
        try:
            for i in range(height):
                for j in range(width):  # top线上方40像素位置开始读, left线左15像素位置开始读
                    img_blank[i][j] = img[face.top() - 40 + i][face.left() - 15 + j]
            return cv2_base64(img_blank)
            # cv2.imwrite(os.path.join(outPic, str(randint(0,10000))+".jpg"), img_blank)  # 保存写入数据后的空白板图片
        except Exception as ex:
            print(ex)
        cv2.destroyAllWindows()  # 释放所有窗口资源
    else:
        cnt += 1
        if cnt < 3:
            transposeImage = cv2.transpose(img)  # 图像反向旋转90度
            flipedImageX = cv2.flip(transposeImage, 0)  # 沿X轴方向的镜像图片
            cv2.imshow("flipedImageX", flipedImageX)
            cv2.waitKey(100)
            tranposeDector(flipedImageX, cnt)
        else:
            print("人脸检测失败 transpose times:", cnt)
            cv2.destroyAllWindows()  # 释放所有窗口资源
