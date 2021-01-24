
'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')



'''
import sys
dir(sys)
print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')


''''''''''''''''''''''''''''''
import math
dir()
a = 30

x = 0
list_xx = [0,1]
y = 360
while x < y:
    list.append(list_xx,x)
    x += 1
    print(x)
x = 0
while x < y:
    b = math.cos(list_xx[x])
    x += 1
    print(b)

''''''''''''''''''
import function
dir(function)
function.Fibo(30)

print(function.sum_xx(4))

''''''''''''''''''''''''
str = input('请输入键盘上的数据：')

print(str);



''''''''''''''''''''''''''
f = open("C:/Users/cao/Desktop/python_test.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()


from datetime import date

now = date.today()

print(now)



a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)
'''
'''
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = '#123' 
             '1'.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

'''


import socket
import _thread
import sys

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\test_tools0612\test_tools.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
cmd_input = ''
s = -1
Gps_xyh = ['8', '5', '8', '5', '8', '5', '8', '5', '8', '6', '8', '6', '8', '6', '8', '6', '0', '0', '8', '9', '8', '9', '1', '3']
Gps = '858585858686868600898913'

def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

def byte_TO_Char(buf, len):
    i = 0
    data = ''
    while i < len * 2:
        data = data + chr(int(buf[i: i + 2], 16))
        i += 2
    return data

def byte_TO_int(buf, len):
    i = 0
    data = 0
    while i < len * 2:
        data = data + int(buf[i: i + 2], 16)
        i += 2
    return data

def byte_TO_intt(buf, len):
    i = 0
    data = 0

    while i < len * 2:
        data = data + int(buf[i: i + 2], 16)
        i += 2
    if data&0b100000000 == 0b100000000:
        tem = ~data&0b011111111
        tem = 0-tem
    else:
        return data
    return tem

def dipose(cmd, len, data):
    get_data = ''
    if cmd == 'B0':
        simstatus = data[:2]
        if simstatus == '00':
            tmp_buf = 'SIM卡不可用\n'
        elif simstatus == '01':
            tmp_buf = 'SIM卡已插入\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        networkavailable = data[2: 4]
        if networkavailable == '00':
            tmp_buf = '网络不可用\n'
        elif simstatus == '01':
            tmp_buf = '网络可用\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        window.ui.textBrowser.append(get_data)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)


    elif cmd == '54' or cmd == '50':
        calltype = data[:2]
        if calltype == '00':
            tmp_buf = 'No Call\n'
        elif calltype == '01':
            tmp_buf = 'Reserved\n'
        elif calltype == '02':
            tmp_buf = 'B/I-Call\n'
        elif calltype == '03':
            tmp_buf = 'E-Call(SOS)\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        status = data[2: 4]
        if status == '00':
            tmp_buf = 'Call start\n'
        elif status == '01':
            tmp_buf = 'Incoming call\n'
        elif status == '02':
            tmp_buf = 'Call failed - reconnectionl\n'
        elif status == '03':
            tmp_buf = 'Call failed\n'
        elif status == '04':
            tmp_buf = 'Call connecting\n'
        elif status == '05':
            tmp_buf = 'Call connected\n'
        elif status == '06':
            tmp_buf = 'Call data sending\n'
        elif status == '07':
            tmp_buf = 'Call ended\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        callbackmode = data[4: 6]
        if callbackmode == '00':
            tmp_buf = 'Normal\n'
        elif callbackmode == '01':
            tmp_buf = 'CallBack\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        window.ui.textBrowser.append(get_data)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    elif cmd == '56':
        remaintime = data[:4]
        get_data = 'CallBack 剩余时间：' + str(int(remaintime, 16))
        window.ui.textBrowser.append(get_data)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    elif cmd == '10':
        signal_type = data[:2]
        if signal_type == '00':
            tmp_buf = '无网络\n'
        elif signal_type == '01':
            tmp_buf = '正在连接网络\n'
        elif signal_type == '02':
            tmp_buf = '2G网络在线\n'
        elif signal_type == '03':
            tmp_buf = '3G网络在线\n'
        elif signal_type == '04':
            tmp_buf = '4G网络在线\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        signal_connect = data[2: 4]
        if signal_connect == '00':
            tmp_buf = '相邻小区\n'
        elif signal_connect == '01':
            tmp_buf = '当前小区\n'
        else:
            tmp_buf = '未知状态\n'
        get_data += tmp_buf
        tmp_buf = byte_TO_Char(data[4: 14], 5)
        get_data += tmp_buf + ':'
        if tmp_buf == '00000':
            get_data += '没有注册到网络\n'
        elif tmp_buf == '46000':
            get_data += '中国移动\n'
        elif tmp_buf == '46001':
            get_data += '中国联通\n'
        elif tmp_buf == '46002':
            get_data += '中国移动\n'
        elif tmp_buf == '46003':
            get_data += '中国电信\n'
        else:
            get_data += '其他\n'
        tmp_buf = byte_TO_Char(data[14: 44], 15)
        get_data += tmp_buf + '\n'
        window.ui.textBrowser_2.append(get_data)
        window.ui.textBrowser_2.moveCursor(window.ui.textBrowser_3.textCursor().End)

    elif cmd == '40':
        csq = data[:2]
        csq = str(int(csq, 16))
        # window.ui.textBrowser_3.clear()
        window.ui.textBrowser_3.append(csq)
        window.ui.textBrowser_3.moveCursor(window.ui.textBrowser_3.textCursor().End)

    elif cmd == 'A0':
        Txbytes = data[:16]
        Rxbytes = data[16:32]
        bytescount = '上行数据流量：\n' + str(int(Txbytes, 16)) + '\n'
        bytescount += '下行数据流量：\n' + str(int(Rxbytes, 16)) + '\n'
        window.ui.textBrowser_4.append(bytescount)
        window.ui.textBrowser_4.moveCursor(window.ui.textBrowser_4.textCursor().End)

    elif cmd == '90':
        p = 0
        mpuversion = data[: p + 20 * 2]
        p = p + 20 * 2
        mpuversion = 'mpuversion=' + byte_TO_Char(mpuversion, 20)
        print(mpuversion)
        get_data += mpuversion + '\n'

        mcuversion = data[p: p + 20 * 2]
        p = p + 20 * 2
        mcuversion = 'mcuversion=' + byte_TO_Char(mcuversion, 20)
        print(mcuversion)
        get_data += mcuversion + '\n'

        hardversion = data[p: p + 20 * 2]
        p = p + 20 * 2
        hardversion = 'hardversion=' + byte_TO_Char(hardversion, 20)
        print(hardversion)
        get_data += hardversion + '\n'

        imsi = data[p: p + 15 * 2]
        p = p + 15 * 2
        imsi = 'imsi=' + byte_TO_Char(imsi, 15)
        print(imsi)
        get_data += imsi + '\n'

        iccid = data[p: p + 20 * 2]
        p = p + 20 * 2
        iccid = 'iccid=' + byte_TO_Char(iccid, 20)
        print(iccid)
        get_data += iccid + '\n'

        msisdn = data[p: p + 15 * 2]
        p = p + 15 * 2
        msisdn = 'msisdn=' + byte_TO_Char(msisdn, 15)
        print(msisdn)
        get_data += msisdn + '\n'

        imei = data[p: p + 15 * 2]
        p = p + 15 * 2
        imei = 'imei=' + byte_TO_Char(imei, 15)
        print(imei)
        get_data += imei + '\n'

        tboxid = data[p: p + 24 * 2]
        p = p + 24 * 2
        tboxid = 'tboxid=' + byte_TO_Char(tboxid, 24)
        print(tboxid)
        get_data += tboxid + '\n'

        supplierid = data[p: p + 6 * 2]
        supplierid = 'supplierid=' + byte_TO_Char(supplierid, 6)
        print(supplierid)
        get_data += supplierid + '\n'
        window.ui.textBrowser.append(get_data)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    elif cmd == 'XX':

        text = "设置成功\n已向Tbox发送设置的模拟位置信息"

        latitude = 'latitude= ' + data[0:8]
        get_data = latitude + '\n'
        longitude = 'longitude= ' + data[8:16]
        get_data += longitude + '\n'
        altitude = 'altitude= ' + data[16:24]
        get_data += altitude + '\n'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.append(get_data)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    elif cmd == 'YY':
        text = "已向Tbox发送默认模拟位置信息\n发送的数据为\nlatitude = 85858585\nlongitude = 86868686\naltitude = 00898913"
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    elif cmd == 'F2':
        p = 0

        vin = data[: p + 17 * 2]
        p = p + 17 * 2
        vin = 'vin=' + byte_TO_Char(vin, 17)
        print(vin)
        get_data += vin + '\n'

        tboxid = data[p: p + 24 * 2]
        p = p + 24 * 2
        tboxid = 'tboxid=' + byte_TO_Char(tboxid, 24)
        print(tboxid)
        get_data += tboxid + '\n'

        iccid = data[p: p + 20 * 2]
        p = p + 20 * 2
        iccid = 'iccid=' + byte_TO_Char(iccid, 20)
        print(iccid)
        get_data += iccid + '\n'

        msisdn = data[p: p + 15 * 2]
        p = p + 15 * 2
        msisdn = 'msisdn=' + byte_TO_Char(msisdn, 15)
        print(msisdn)
        get_data += msisdn + '\n'

        imsi = data[p: p + 15 * 2]
        p = p + 15 * 2
        imsi = 'imsi=' + byte_TO_Char(imsi, 15)
        print(imsi)
        get_data += imsi + '\n'

        Net_tpye = data[p: p + 1 * 2]
        p = p + 1 * 2
        Net_tpye = 'Net_tpye=' + str(byte_TO_int(Net_tpye, 1))
        print(Net_tpye)
        Net_tpye += Net_tpye + '\n'

        Operator = data[p: p + 5 * 2]
        p = p + 5 * 2
        Operator = 'Operator=' + byte_TO_Char(Operator, 5)
        print(Operator)
        get_data += Operator + '\n'

        IP = data[p: p + 15 * 2]
        p = p + 15 * 2
        IP = 'IP=' + byte_TO_Char(IP, 15)
        print(IP)
        get_data += IP + '\n'

        Earfcn = data[p: p + 1 * 2]
        p = p + 1 * 2
        Earfcn = 'Earfcn=' + str(byte_TO_int(Earfcn, 1))
        print(Earfcn)
        get_data += Earfcn + '\n'


        pci = data[p: p + 1 * 2]
        p = p + 1 * 2
        pci = 'pci=' + str(byte_TO_int(pci, 1))
        print(pci)
        get_data += pci + '\n'


        Globe_ci = data[p: p + 4 * 2]
        p = p + 4 * 2
        Globe_ci = 'Globe_ci=' + str(byte_TO_int(Globe_ci, 4))
        print(Globe_ci)
        get_data += Globe_ci + '\n'

        Tac = data[p: p + 2 * 2]
        p = p + 2 * 2
        Tac = 'Tac=' + str(byte_TO_int(Tac, 2))
        print(Tac)
        get_data += Tac + '\n'

        ul_bw = data[p: p + 8 * 2]
        p = p + 8 * 2
        ul_bw = 'ul_bw=' + str(byte_TO_int(ul_bw, 8))
        print(ul_bw)
        get_data += ul_bw + '\n'

        dl_bw = data[p: p + 8 * 2]
        p = p + 8 * 2
        dl_bw = 'dl_bw=' + str(byte_TO_int(dl_bw, 8))
        print(dl_bw)
        get_data += dl_bw + '\n'

        Rsrp = data[p: p + 2 * 2]
        p = p + 2 * 2
        Rsrp = 'Rsrp=' + str(byte_TO_intt(Rsrp, 2))
        print(Rsrp)
        get_data += Rsrp + '\n'

        Rsrq = data[p: p + 2 * 2]
        p = p + 2 * 2
        Rsrq = 'Rsrq=' + str(byte_TO_intt(Rsrq, 2))
        print(Rsrq)
        get_data += Rsrq + '\n'

        Rssi = data[p: p + 1 * 2]
        p = p + 1 * 2
        Rssi = 'Rssi=' + str(byte_TO_int(Rssi, 1))
        print(Rssi)
        get_data += Rssi + '\n'

        APN = data[p: p + 1 * 2]
        p = p + 1 * 2
        APN = 'APN=' + str(byte_TO_int(APN, 1))
        print(APN)
        get_data += APN + '\n'

        longitude = data[p: p + 4 * 2]
        p = p + 4 * 2
        longitude = 'longitude=' + str(byte_TO_int(longitude, 4))
        print(longitude)
        get_data += longitude + '\n'

        latitude = data[p: p + 4 * 2]
        p = p + 4 * 2
        latitude = 'latitude=' + str(byte_TO_int(latitude, 4))
        print(latitude)
        get_data += latitude + '\n'

        Esim_status = data[p: p + 1 * 2]
        p = p + 1 * 2
        Esim_status = 'Esim_status=' + str(byte_TO_int(Esim_status, 1))
        print(Esim_status)
        get_data += Esim_status + '\n'

        Voice_status = data[p: p + 1 * 2]
        p = p + 1 * 2
        Voice_status = 'Voice_status=' + str(byte_TO_int(Voice_status, 1))
        print(Voice_status)
        get_data += Voice_status + '\n'

        Net_connection_status = data[p: p + 1 * 2]
        p = p + 1 * 2
        Net_connection_status = 'Net_connection_status=' + str(byte_TO_int(Net_connection_status, 1))
        print(Net_connection_status)
        get_data += Net_connection_status + '\n'

        DTC_status = data[p: p + 1 * 2]
        DTC_status = 'DTC_status=' + str(byte_TO_int(DTC_status, 1))
        print(DTC_status)
        get_data += DTC_status + '\n'

        window.ui.textBrowser.append(get_data)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    if cmd == 'B7':


        text = 'recved cmd = B7'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)
        return_cmd1()

    if cmd == 'BB':
        text = 'recved cmd = BB'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)
        return_cmd2()

    if cmd == 'B4':
        text = 'recved cmd = B4'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)
        return_cmd3()

    if cmd == 'B3':
        text = 'recved cmd = B3'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    if cmd == 'B5':
        text = 'recved cmd = B5'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)

    if cmd == '02':
        text = 'recved cmd = 02'
        window.ui.textBrowser.append(text)
        window.ui.textBrowser.moveCursor(window.ui.textBrowser.textCursor().End)
        return_version_v2x()

    else:
        get_data = ''

    return 0

def return_cmd1():
    cmd_input = 'B7'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)

    cmd_input = 'B3'
    len = '0005'
    data = '1000100011'
    sendcmd(cmd_input, len, data)
    return 0

def return_cmd2():

    cmd_input = 'BB'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)


    InstallationConsent = '0'
    InstallationOrder = '1000'
    TimeStamp = '1000'
    Reason = '0'
    InstallationStartTimeSet = '00'

    data = InstallationConsent + InstallationOrder + TimeStamp + Reason + InstallationStartTimeSet
    cmd_input = 'B5'
    len = '0006'
    sendcmd(cmd_input, len, data)

    return 0
def return_cmd3():
    cmd_input = 'B4'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)

def return_version_v2x():



    cmd_input = '02'
    len = '0005'
    data = '1000100011'
    sendcmd(cmd_input, len, data)

def sendcmd(cmd, len, data):
    global s
    buf_send = '0D052A'
    buf_send = buf_send + cmd
    buf_send = buf_send + len
    buf_send = buf_send + data
    crc = int(cmd, 16) ^ int(len[:2], 16) ^ int(len[2:4], 16)
    i = 0
    while (i < int(len, 16) * 2):
        crc = crc ^ int(data[i: i + 2], 16)
        i += 2

    a = hex(crc)[2: 4]
    a = a.upper()

    buf_send = buf_send + a
    buf_send = buf_send + '0D0A'
    buf_send = str.encode(buf_send)
    s.send(buf_send)
    return 0


def connect_tbox():
    try:
        # _thread.start_new_thread(sendthread, ())
        _thread.start_new_thread(revcthread, ())
    except Exception as err:
        print(err)
    return 0


def revcthread():
    #HOST = '192.168.225.1'
    #PORT = 28888
    HOST = '192.168.100.1'
    PORT = 50000
    BUFSIZ = 1024
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    window.ui.textBrowser.append("车机启动，接收TBox数据。。。\n")

    while True:
        # if (BUFSIZ > 0):
        buf = bytes.decode(s.recv(BUFSIZ))
        print(buf)
        sumlen = len(buf)
        print(sumlen)
        # print('buf=',buf,'sumlen=',sumlen)
        p = 0
        while (p < sumlen):
            p += 6

            tmp_cmd = buf[p: p + 2]
            # print('cmd=',tmp_cmd);
            p += 2

            tmp_len = int(buf[p: p + 4], 16)
            # print('tmp_len=',tmp_len)
            p += 4

            tmp_data = buf[p: p + tmp_len * 2]  # 2char is byte
            # print("cmd=%s, tmp_len=%x, tmp_data=%s"%(tmp_cmd,tmp_len,tmp_data))
            p += tmp_len * 2
            dipose(tmp_cmd, tmp_len, tmp_data)
            p += 6
        if cmd_input == 'exit':
            print('exiting...')
            break
    s.close
    return 0

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\test0616.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 739)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 50, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 230, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 230, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 290, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 290, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(780, 170, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 170, 91, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 170, 91, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 290, 91, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 570, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(760, 480, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(550, 230, 91, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 101, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 270, 451, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 150, 451, 91))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(290, 50, 201, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(40, 50, 221, 71))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 470, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 500, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 530, 61, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(550, 350, 91, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(670, 350, 91, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(780, 350, 91, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(550, 410, 91, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(670, 410, 91, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(630, 470, 91, 20))
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(630, 500, 91, 20))
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(630, 530, 91, 20))
        self.lineEdit_3.setMaxLength(8)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 560, 481, 121))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "连接Tbox"))
        self.pushButton_2.setText(_translate("MainWindow", "拨打B-call"))
        self.pushButton_3.setText(_translate("MainWindow", "拨打E-call"))
        self.pushButton_4.setText(_translate("MainWindow", "挂断B-call"))
        self.pushButton_5.setText(_translate("MainWindow", "挂断E-call"))
        self.pushButton_6.setText(_translate("MainWindow", "查询电话状态"))
        self.pushButton_7.setText(_translate("MainWindow", "查询Tbox信息"))
        self.pushButton_8.setText(_translate("MainWindow", "查询网络状态"))
        self.pushButton_9.setText(_translate("MainWindow", "CallBack时间"))
        self.pushButton_10.setText(_translate("MainWindow", "清除测试结果"))
        self.pushButton_11.setText(_translate("MainWindow", "发送GPS信息"))
        self.pushButton_12.setText(_translate("MainWindow", "工程模式\n"
"一键测试"))
        self.label.setText(_translate("MainWindow", "实时上下行速度"))
        self.label_2.setText(_translate("MainWindow", "实时信号强度"))
        self.label_3.setText(_translate("MainWindow", "网络状态"))
        self.label_4.setText(_translate("MainWindow", "测试结果"))
        self.label_5.setText(_translate("MainWindow", "请输入经度"))
        self.label_6.setText(_translate("MainWindow", "请输入纬度"))
        self.label_7.setText(_translate("MainWindow", "请输入海拔"))
        self.pushButton_13.setText(_translate("MainWindow", "FOTA1.5测试"))
        self.pushButton_14.setText(_translate("MainWindow", "预留2"))
        self.pushButton_15.setText(_translate("MainWindow", "预留3"))
        self.pushButton_16.setText(_translate("MainWindow", "预留4"))
        self.pushButton_17.setText(_translate("MainWindow", "设置GPS"))
        self.lineEdit.setText(_translate("MainWindow", "85858585"))
        self.lineEdit_2.setText(_translate("MainWindow", "86868686"))
        self.lineEdit_3.setText(_translate("MainWindow", "00898913"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">重要提醒：</span></p><p>使用前请先点击连接Tbox</p><p>测试GPS时需要<span style=\" font-weight:600; color:#ff0000;\">同时改变</span>经纬度和海拔三个值，并<span style=\" font-weight:600; color:#ff0000;\">点击设置GPS按键</span>后再发送GPS信息</p><p>否则仍会发送默认信息</p></body></html>"))



def get_TBox_info():
    cmd_input = '90'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0


def get_Sim_status():
    cmd_input = 'B0'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0


def call_state():
    cmd_input = '54'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0


def get_callbacktime():
    cmd_input = '56'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0


def call_b_call():
    cmd_input = '52'
    len = '0002'
    data = '0102'
    sendcmd(cmd_input, len, data)
    return 0


def call_e_call():
    cmd_input = '52'
    len = '0002'
    data = '0103'
    sendcmd(cmd_input, len, data)
    return 0


def hang_up_e_call():
    cmd_input = '52'
    len = '0002'
    data = '0003'
    sendcmd(cmd_input, len, data)
    return 0

def test_fota():
    cmd_input = 'FF'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0

def test_v2x():
    cmd_input = '01'
    len = '0'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0

def Engineer_test():
    cmd_input = 'F1'
    len = '0000'
    data = ''
    sendcmd(cmd_input, len, data)
    return 0

def Send_GpsInfo():

     global Gps

     if Gps != "858585858686868600898913":
          set_gps = str(Gps)
          flag = 0
     else:
          latitude = '85858585'
          longitude = '86868686'
          altitude = '00898913'
          set_gps = latitude + longitude + altitude
          flag = 1
     if findLen(set_gps) !=24:
         latitude = '85858585'
         longitude = '86868686'
         altitude = '00898913'
         set_gps = latitude + longitude + altitude
         flag = 1
     posCanBeTrusted = '01'
     direction = '6615'
     time = '92221763'
     speed = '5777'
     posState = '01'
     MarsCoordinates = '01'
     data = set_gps + posCanBeTrusted + direction + time + speed + posState + MarsCoordinates
     cmd_input = '70'
     len = '0017'
     sendcmd(cmd_input, len, data)
     if flag == 0:
         dipose('XX', 24, set_gps)
     elif flag == 1:
         dipose('YY', 24, set_gps)

     return 0

def Get_GpsInfo():

    global Gps
    Gps = "".join(Gps_xyh)
    a = len(Gps)

def sendx(x):
    global Gps_xy
    x = str(x)
    Gps_xyh[0:8] = x

def sendy(y):
    global Gps_xyh
    y = str(y)
    Gps_xyh[9:16] = y



def sendh(h):
    global Gps_xyh
    h = str(h)
    Gps_xyh[16:24] = h

class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.query_formula)
        self.ui.pushButton.clicked.connect(connect_tbox)
        # self.ui.pushButton_2.clicked.connect(call_b_call)
        self.ui.pushButton_3.clicked.connect(call_e_call)
        self.ui.pushButton_5.clicked.connect(hang_up_e_call)
        self.ui.pushButton_6.clicked.connect(call_state)
        self.ui.pushButton_7.clicked.connect(get_TBox_info)
        self.ui.pushButton_8.clicked.connect(get_Sim_status)
        self.ui.pushButton_9.clicked.connect(get_callbacktime)
        self.ui.pushButton_10.clicked.connect(self.clear_text)
        self.ui.pushButton_11.clicked.connect(Send_GpsInfo)
        self.ui.pushButton_12.clicked.connect(Engineer_test)
        self.ui.pushButton_13.clicked.connect(test_fota)
        self.ui.pushButton_14.clicked.connect(test_v2x)
        self.ui.pushButton_17.clicked.connect(Get_GpsInfo)
        self.ui.lineEdit.textChanged.connect(self.Get_X)
        self.ui.lineEdit_2.textChanged.connect(self.Get_Y)
        self.ui.lineEdit_3.textChanged.connect(self.Get_H)

    def clear_text(self):
        self.ui.textBrowser.clear()

    def Get_X(self, text):
        sendx(text)

    def Get_Y(self, text):
        sendy(text)

    def Get_H(self, text):
        sendh(text)

app = QtWidgets.QApplication(sys.argv)
window = query_window()
window.show()
sys.exit(app.exec_())
