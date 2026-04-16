import time
from socket import *
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
        s.settimeout(2)

        s.sendto(command, self.addr)
        rcvdata = s.recv(BUFSIZE)

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

    def mws(self, addresses):
        rcv = self.sendrecive(('MWS ' + addresses + '\r').encode())
        return rcv

    def mwr(self):
        rcv = self.sendrecive(('MWR\r').encode())
        return rcv

if __name__ == "__main__":
    kv = kvHostLink('192.168.250.32')
    data = kv.mode('1')
    print(data)						# b'OK\r\n'
    data = kv.unittype()
    print(data)						# b'57\r\n'
    data = kv.errclr()
    print(data)						# b'OK\r\n'
    data = kv.er()
    print(data)						# b'000\r\n'
    data = kv.settime()
    print(data)						# b'OK\r\n'
    data = kv.set('MR0')
    print(data)						# b'OK\r\n'
    data = kv.reset('MR1')
    print(data)						# b'OK\r\n'
    data = kv.sts('MR10', 5)
    print(data)						# b'OK\r\n'
    data = kv.rss('MR10', 4)
    print(data)						# b'OK\r\n'
    data = kv.read('DM0.U')
    print(data)						# b'00002\r\n'
    data = kv.reads('DM0.S', 4)
    print(data)						# b'+00002 +00001 +00002 +00003\r\n'
    data = kv.write('DM0.U', '2')
    print(data)						# b'OK\r\n'
    data = kv.writs('DM1.S', 4, '1 2 3 4')
    print(data)						# b'OK\r\n'
    data = kv.mws('DM0.H DM1.S DM2.L DM4.U DM5.D')
    print(data)						# b'OK\r\n'
    data = kv.mwr()
    print(data)						# b'0002 +00001 +0000196610 00004 0605955594\r\n'

