#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Adafruit_PCA9685
import time

#サーボモーターをコントロールするためのクラス
class servo_Class:
    #ChannelはPCA9685のサーボモーターを繋いだチャンネル
    #ZeroOffsetはサーボモーターの基準の位置を調節するためのパラメーターです
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset

        #Adafruit_PCA9685の初期化
        
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(60)

    """角度を設定する関数です"""
    def SetPos(self,pos):
        #pulse = 150～650 : 0 ～ 180度
        #PCA9685はパルスで角度を制御しているため0~180のように角度を指定しても思った角度にはなりません
        #そこで角度の値からパルスの値へと変換します。PCA9685ではパルス150~650が角度の0~180に対応しているみたいです
        #下の式の(650-150)/180は1度あたりのパルスを表しています
        #それにpos(制御したい角度)を掛けた後、150を足すことでことで角度をパルスに直しています。
        #最後にZeroOffsetを足すことで基準にしたい位置に補正します
        pulse = (650-150)/180*pos+150+self.ZeroOffset
        print("pulse")
        print(int(pulse))
        self.pwm.set_pwm(self.Channel, 0, int(pulse))

class UsbLocker:
    # UsbフラッシュメモリのLock-unlockを行うクラスです,装置特有のオフセットや角度を吸収します
    def __init__(self, Number):
        self.Servo = servo_Class(Channel=Number-1, ZeroOffset=-5)
        
    def Lock(self):
        self.Servo.SetPos(50)
        
    def Unlock(self):
        self.Servo.SetPos(130)

"""制御を行うメインの部分です"""
if __name__ == '__main__':
    #今回はサーボモーターが3つあります
    #Servo0 = servo_Class(Channel=0, ZeroOffset=-5)
    usbLocker0 = UsbLocker(Number=1)

    try:
        #テストでそれぞれのサーボモーターを45度,90度と繰り返し動かしてみます。
        while True:
            print('Lock')
            usbLocker0.Lock()
            time.sleep(2)

            print('Unlock')
            usbLocker0.Unlock()
            time.sleep(2)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print((str(e)))
