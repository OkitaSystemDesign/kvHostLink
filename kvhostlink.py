#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

import time
from socket import *
import struct
import datetime

BUFSIZE = 4096

class kvHostLink:
    addr = ()
    destfins = []
    srcfins = []
    port = 8501
    

    def __init__(self, host):
        self.addr = host, self.port

    def sendrecive(self, command):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('', self.port))
        s.settimeout(2)

        starttime = time.time()

        s.sendto(command, self.addr)
        #print("send:%r" % (command))
        rcvdata = s.recv(BUFSIZE)

        elapsedtime = time.time() - starttime
        #print ('receive: %r\t Length=%r\telapsedtime = %sms' % (rcvdata, len(rcvdata), str(elapsedtime * 1000)))
        #print()
        return rcvdata

    def mode(self, mode):
        senddata = 'M' + mode
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv

    def unittype(self):
        rcv = self.sendrecive("?k\r".encode())
        return rcv

    def errclr(self):
        senddata = 'ER'
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv

    def er(self):
        senddata = '?E'
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv

    def settime(self):
        dt_now = datetime.datetime.now()
        senddata = 'WRT ' + str(dt_now.year)[2:]
        senddata = senddata + ' ' + str(dt_now.month)
        senddata = senddata + ' ' + str(dt_now.day)
        senddata = senddata + ' ' + str(dt_now.hour)
        senddata = senddata + ' ' + str(dt_now.minute)
        senddata = senddata + ' ' + str(dt_now.second)
        senddata = senddata + ' ' + dt_now.strftime('%w')
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv
        
    def set(self, address):
        rcv = self.sendrecive(('ST ' + address + '\r').encode())
        return rcv

    def reset(self, address):
        rcv = self.sendrecive(('RS ' + address + '\r').encode())
        return rcv

    def sts(self, address, num):
        rcv = self.sendrecive(('STS ' + address + ' ' + str(num) + '\r').encode())
        return rcv

    def rss(self, address, num):
        rcv = self.sendrecive(('RSS ' + address + ' ' + str(num) + '\r').encode())
        return rcv

    def read(self, addresssuffix):
        rcv = self.sendrecive(('RD ' + addresssuffix + '\r').encode())
        return rcv

    def reads(self, addresssuffix, num):
        rcv = self.sendrecive(('RDS ' + addresssuffix + ' ' + str(num) + '\r').encode())
        return rcv

    def write(self, addresssuffix, data):
        rcv = self.sendrecive(('WR ' + addresssuffix + ' ' + data + '\r').encode())
        return rcv

    def writs(self, addresssuffix, num, data):
        rcv = self.sendrecive(('WRS ' + addresssuffix + ' ' + str(num) + ' ' + data + '\r').encode())
        return rcv




    def toInt16(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 2):
            tmpdata = arydata[idx:idx+2]
            outdata += (struct.unpack('>h',tmpdata))
        
        return outdata

    def toUInt16(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 2):
            tmpdata = arydata[idx:idx+2]
            outdata += (struct.unpack('>H',tmpdata))
        
        return outdata

    def toInt32(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            outdata += (struct.unpack('>i',tmpdata))
        
        return outdata
            
    def toUInt32(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            outdata += (struct.unpack('>I',tmpdata))
        
        return outdata

    def toInt64(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 8):
            tmpdata = arydata[idx:idx+8]
            outdata += (struct.unpack('>q',tmpdata))
        
    def toUInt64(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 8):
            tmpdata = arydata[idx:idx+8]
            outdata += (struct.unpack('>Q',tmpdata))
        
        return outdata

    def toFloat(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            a = tmpdata[::-1]
            a[0],a[1] = a[1],a[0]
            a[2],a[3] = a[3],a[2]

            outdata += (struct.unpack('>f', a))
        return outdata

    def toDouble(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 8):
            tmpdata = arydata[idx:idx+8]
            a = tmpdata[::-1]
            a[0],a[1] = a[1],a[0]
            a[2],a[3] = a[3],a[2]
            a[4],a[5] = a[5],a[4]
            a[6],a[7] = a[7],a[6]

            outdata += (struct.unpack('>d', a))
        return outdata

    def toString(self, data):
        s = [0]*len(data)
        for i in range(0, len(data), 2):
            s[i] = data[i+1]
            s[i+1] = data[i]
        
        b = bytes(s).decode("utf-8").replace("\00","")

        return b


kv = kvHostLink('192.168.0.31')
data = kv.mode('1')
print(data)
data = kv.er()
print(data)
data = kv.errclr()
print(data)
data = kv.unittype()
print(data)
data = kv.settime()
print(data)
data = kv.set('MR0')
print(data)
data = kv.reset('MR1')
print(data)
data = kv.sts('MR10', 5)
print(data)
data = kv.rss('MR10', 4)
print(data)
data = kv.read('DM0.U')
print(data)
data = kv.reads('DM0.S', 4)
print(data)
data = kv.write('DM0.U', '2')
print(data)
data = kv.writs('DM1.S', 4, '1 2 3 4')
print(data)
