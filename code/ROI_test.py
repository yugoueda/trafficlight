import numpy as np
import cv2


class PointList():
    def __init__(self, npoints):
        self.npoints = npoints
        self.ptlist = np.empty((npoints, 2), dtype=int)
        self.pos = 0

    def add(self, x, y):
        if self.pos < self.npoints:
            self.ptlist[self.pos, :] = [x, y]
            self.pos += 1
            return True
        return False


def onMouse(event, x, y, flag, params):
    wname, img, ptlist = params
    if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
        img2 = np.copy(img)
        h, w = img2.shape[0], img2.shape[1]
        cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
        cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
        cv2.imshow(wname, img2)

    if event == cv2.EVENT_LBUTTONDOWN:  # レフトボタンをクリックしたとき、ptlist配列にx,y座標を格納する
        if ptlist.add(x, y):
            print('[%d] ( %d, %d )' % (ptlist.pos - 1, x, y))
            cv2.circle(img, (x, y), 2, (0, 0, 255), 2)
            cv2.imshow(wname, img)
        else:
            print('All points have selected.  Press ESC-key.')
        if(ptlist.pos == ptlist.npoints):
            print(ptlist.ptlist)
            cv2.line(img, (ptlist.ptlist[0][0], ptlist.ptlist[0][1]),
                     (ptlist.ptlist[1][0], ptlist.ptlist[1][1]), (0, 255, 0), 2)
            cv2.line(img, (ptlist.ptlist[1][0], ptlist.ptlist[1][1]),
                     (ptlist.ptlist[2][0], ptlist.ptlist[2][1]), (0, 255, 0), 2)
            cv2.line(img, (ptlist.ptlist[2][0], ptlist.ptlist[2][1]),
                     (ptlist.ptlist[3][0], ptlist.ptlist[3][1]), (0, 255, 0), 2)
            cv2.line(img, (ptlist.ptlist[3][0], ptlist.ptlist[3][1]),
                     (ptlist.ptlist[0][0], ptlist.ptlist[0][1]), (0, 255, 0), 2)


                


if __name__ == '__main__':
    img = cv2.imread("2019-12-04 12.13.jpg")
    wname = "MouseEvent"
    wname2 = "roi"
    cv2.namedWindow(wname)
    npoints = 4
    ptlist = PointList(npoints)
    cv2.setMouseCallback(wname, onMouse, [wname, img, ptlist])
    cv2.imshow(wname, img)
    
    


    cv2.waitKey()
    cv2.destroyAllWindows()