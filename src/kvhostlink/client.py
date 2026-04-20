from socket import *
import datetime

BUFSIZE = 4096

class kvHostLink:
    addr = ()
    destfins = []
    srcfins = []
    port = 8501
    
    def __init__(self, host, timeout=2.0):
        self.addr = host, self.port
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.settimeout(timeout)

    def __del__(self):
        self.s.close()

    def sendrecive(self, command):
        self.s.sendto(command, self.addr)
        rcvdata = self.s.recv(BUFSIZE)

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
