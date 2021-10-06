import cv2
import datetime 

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(1)

try:
    while(True):

        # フレームの読み取り
        ret,frame=capture.read()

        # グレースケール変換
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame_gray",gray)

        #メイン処理 日付と時刻を表す文字列を含んだファイル名のファイルを作成
        date0=datetime.datetime.now()
        date_str_form=date0.strftime("%Y%m%d_%H%M%S_%f")
        cv2.imwrite(date_str_form+".jpg",gray)

        cv2.waitKey(1000)

except:
    cv2.destroyWindow("Window")

