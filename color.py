import cv2
import time
import sys
import numpy as np

class mouseParam:
    def __init__(self, input_img_name):
        #マウス入力用のパラメータ
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}
        #マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)
    
    #コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType    
        self.mouseEvent["flags"] = flags    

    #マウス入力用のパラメータを返すための関数
    def getData(self):
        return self.mouseEvent
    
    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]                

    #マウスフラグを返す関数
    def getFlags(self):
        return self.mouseEvent["flags"]                

    #xの座標を返す関数
    def getX(self):
        return self.mouseEvent["x"]  

    #yの座標を返す関数
    def getY(self):
        return self.mouseEvent["y"]  

    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])
        

if __name__ == "__main__":
    #入力画像
    read1 = cv2.imread("2019-12-10 16.15.jpg")
    
    #表示するWindow名
    window_name = "input window"

    height = read1.shape[0]
    width = read1.shape[1]
    exheight = height * 2
    exwigth = width * 2
    print(exheight)

    read = cv2.resize(read1,None,fx = 1.5,fy = 1.5)

 
    #画像の表示
    cv2.imshow(window_name, read)
    
    #コールバックの設定
    mouseData = mouseParam(window_name)
    
    while 1:
        cv2.waitKey(20)
        #左クリックがあったら表示
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
            print(mouseData.getPos())
            pixelValue = read[mouseData.getPos()]
            print (('pixelValue = ') + str(pixelValue))
        #右クリックがあったら終了
        elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
            break
            
    cv2.destroyAllWindows()            
    print("Finished")
