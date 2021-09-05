#クライアントを作成
import socket
import pygame
from pygame.locals import *
import sys
import math

pygame.joystick.init()#pygameにあるjoystickを初期化する
try:#エラー覚悟のtry、これはうまくいった場合
    j = pygame.joystick.Joystick(0) # create a joystick instance接続しているコントローラを変数に入れる
    j.init() # init instance接続しているコントローラを初期化する
except pygame.error:#うまくいかなかった場合
    print ('Joystickが見つかりませんでした。')
    
def zahyou(x,y):
    if x<0.4 and x>-0.4 and y<0:
        return b'1'
    elif x>=0.4 and x<=1 and y<0:
        return b'2'
    elif x>=-1 and x<=-0.4 and y<0:
        return b'3'
    else:
        return 0



def main():
    button=0
    x=0.0
    y=0.0
    pygame.init()#pygameを初期化する
    clock=pygame.time.Clock()#clockオブジェクトを作成
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        #IPアドレスとポートを指定
        print("before")
        s.bind(('192.168.111.100',8888))
        print("after")
        #1接続
        s.listen(1)
        #connectionするまで待つ
        #サーバにメッセージを送る
        print("before")
        conn,addr=s.accept()
        print("after")
        while True:
            for event in pygame.event.get():#起こったイベントをeventにいれて起こった数だけループする
                if event.type == pygame.locals.JOYAXISMOTION: # 7
                    x , y = j.get_axis(0), j.get_axis(1)
                    #stringをbytesにする
                    print("x:",x)
                    print("y:",y)
                    str_x=zahyou(x,y)
                    if not str_x==0:
                        print("str_x:",str_x)
                        conn.send(str_x)  
                if event.type==pygame.locals.JOYBUTTONDOWN:
                    if event.button==1:
                        pygame.quit()
                        sys.exit()

                clock.tick(10)#一秒間に10回フレームを更新する
            
    

    print("aiueo")

if __name__=='__main__':
    main()