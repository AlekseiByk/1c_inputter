from pynput.keyboard import Key, Controller
from pymouse import PyMouse
import pyscreenshot as ImageGrab
import cv2
import numpy
import time

threshold = .9
keyboard = Controller()
mouse = PyMouse()
delta = 300

def check_for_error(x, y):
    box = (x - delta , int(y - delta/2), x + delta , int(y + delta/2))
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')

    rgb_im.save("images/im.png")
    img_rgb = cv2.imread('images/im.png')
    template = cv2.imread('images/im_error.png')

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) != 0:
        return True
    
    template = cv2.imread('images/im_notfound.png')

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) != 0:
        return True
    
    return False

def find_coordinates():
    im = ImageGrab.grab()
    rgb_im = im.convert('RGB')
    rgb_im.save("images/im.png")
    img_rgb = cv2.imread('images/im.png')

    template = cv2.imread('images/im_create.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)

    if len(loc[0]) == 0:
        print('Cannot find create button/field on the screen. Stopping...')
        exit()
        
    x_create = int(loc[1] + w/2)
    y_create = int(loc[0] + h/2)
    mouse.press(x_create, y_create, 1)

    #----------------------------------searching for fields
    time.sleep(0.2)
    im = ImageGrab.grab()
    rgb_im = im.convert('RGB')
    rgb_im.save("images/im.png")
    img_rgb = cv2.imread('images/im.png')

    template = cv2.imread('images/im_student.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) == 0:
        print('Cannot find student field on the screen. Stopping...')
        exit()

    x_temp = int(loc[1][0])
    y_temp = int(loc[0][0])

    box = (x_temp, y_temp - 2, x_temp + 450, y_temp + h + 2)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    rgb_im.save("images/im.png")
    img_cropped_rgb = cv2.imread('images/im.png')

    template = cv2.imread('images/im_input.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_cropped_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) == 0:
        print('Cannot find student input field on the screen. Stopping...')
        exit()

    x_student = int(loc[1][0] + x_temp + w/2)
    y_student = int(loc[0][0] + y_temp + h/2)

    template = cv2.imread('images/im_search.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) == 0:
        print('Cannot find category field on the screen. Stopping...')
        exit()

    x_cat = int(loc[1][0] + w/4)
    y_cat = int(loc[0][0] + h/2)

    template = cv2.imread('images/im_sum.png')
    h, w = template.shape[:-1]
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) == 0:
        print('Cannot find sum field on the screen. Stopping...')
        exit()

    x_sum = int(loc[1][0])
    y_sum = int(loc[0][0] + h/2)

    template = cv2.imread('images/im_docs.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) == 0:
        print('Cannot find docs field on the screen. Stopping...')
        exit()

    x_temp = int(loc[1][0])
    y_temp = int(loc[0][0])

    box = (x_temp, y_temp - 2, x_temp + 300, y_temp + h + 2)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    rgb_im.save("images/im.png")
    img_cropped_rgb = cv2.imread('images/im.png')

    template = cv2.imread('images/im_rect.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_cropped_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    if len(loc[0]) == 0:
        print('Cannot find docs tik field on the screen. Stopping...')
        exit()

    x_docs = int(loc[1][0] + x_temp + w/2)
    y_docs = int(loc[0][0] + y_temp + h/2)
    return x_create, y_create, x_student, y_student, \
           x_docs, y_docs, x_sum, y_sum, x_cat, y_cat
