import os
import cv2
import pytesseract
import tkinter as tk

# 判断screenshot.png文件是否存在
if not os.path.exists("C:\\python\\screenshot.png"):
    # 若不存在，弹出警告框
    popup = tk.Tk()
    popup.geometry("300x150")
    popup.title("警告!")
    tk.Label(popup, text="请先运行Screenshot.py文件!").pack()
    tk.Button(popup, text="确定", command=popup.destroy).pack(pady=10)
    popup.mainloop()
else:
    # 若存在，读取图片并转换为灰度图
    img = cv2.imread("C:\\python\\screenshot.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图转换为二值图
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # 识别图片中的文字
    custom_config = r'-l chi_sim --oem 1 --psm 7'
    code = pytesseract.image_to_string(gray, config=custom_config)
    print(code)
    # 显示图片
    cv2.imshow("img", img)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()