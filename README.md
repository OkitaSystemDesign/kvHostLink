# kvhostlink.py
KEYENCE HostLink Communication for UDP/IP

# Constructor
kvhostlink(host)

# Functions
### hostlink.mode(mode)
Change Mode  
0 = PROGRAM  
1 = RUN  
Retrun: EtherNet/IP Unit Response

### hostlink.unittype()
Checks PLC model  
Retrun: EtherNet/IP Unit Response

### hostlink.errclr()
Removes the error in CPU unit  
Retrun: EtherNet/IP Unit Response

### hostlink.er()
Confirm Error No  
Retrun: EtherNet/IP Unit Response

### hostlink.settime()
Set up time of the CPU unit  
Send the date and time of your computer
Retrun: EtherNet/IP Unit Response

### hostlink.set(address)
Forced Set
address = R00000-199915, B0000-7FFF, MR00000-399915, LR00000-99915, CR0000-7915, T0000-3999, C0000-3999, CTC0-3, VB0000-F9FF 
Retrun: EtherNet/IP Unit Response

### hostlink.reset(address)
Forced Reset
address = R00000-199915, B0000-7FFF, MR00000-399915, LR00000-99915, CR0000-7915, T0000-3999, C0000-3999, CTC0-3, VB0000-F9FF 
Retrun: EtherNet/IP Unit Response

### hostlink.sts(address)
Continuous Forced Set
address = R00000-199915, B0000-7FFF, MR00000-399915, LR00000-99915, CR0000-7915, VB0000-F9FF 
num = number of written data
Retrun: EtherNet/IP Unit Response

### hostlink.rss(address, num)
Continuous Forced Reset
address = R00000-199915, B0000-7FFF, MR00000-399915, LR00000-99915, CR0000-7915, VB0000-F9FF 
num = number of written data
Retrun: EtherNet/IP Unit Response


### hostlink.write(memAddres, data)
Memory Area Write  
memAddress = D0-D32767, E0_0-EF_32767, W0-511, 0-6143  
data = bytes()  
Return: fins responce

### fins.toInt16(data)
Convert to 16bit data  
### fins.toInt32(data)
Convert to 32bit data  
### fins.toInt64(data)
Convert to 64bit data  
### fins.toUInt16(data)
Convert to Unsigned 16bit data  
### fins.toUInt32(data)
Convert to Unsigned 32bit data  
### fins.toUInt64(data)
Convert to Unsigned 64bit data  
### fins.toFloat(data)
Convert to Float data  
### fins.toDouble(data)
Convert to Double data  

 return: list
 

# Example
```
finsudp = fins('192.168.250.1', '0.1.0', '0.10.0')
data = finsudp.read('E0_30000", 10)
print(finsudp.toInt16(data))
rcv = finsudp.write('E0_0', data)
print(rcv)
```
