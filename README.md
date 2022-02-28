# kvhostlink.py
KEYENCE HostLink Communication for UDP/IP

# Constructor
kvhostlink(host)

# Functions
### .mode(mode)
Change Mode  
0 = PROGRAM  
1 = RUN  
Retrun: EtherNet/IP Unit Response

### .unittype()
Checks PLC model  
Retrun: EtherNet/IP Unit Response

### .errclr()
Removes the error in CPU unit  
Retrun: EtherNet/IP Unit Response

### .er()
Confirm Error No  
Retrun: EtherNet/IP Unit Response

### .settime()
Set up time of the CPU unit  
Send the date and time of your computer
Retrun: EtherNet/IP Unit Response

### .set(address)
Forced Set
address = R0-199915, B0-7FFF, MR0-399915, LR0-99915, CR0-7915, T0-3999, C0-3999, CTC0-3, VB0-F9FF  
Retrun: EtherNet/IP Unit Response

### .reset(address)
Forced Reset  
address = R0-199915, B0-7FFF, MR0-399915, LR0-99915, CR0-7915, T0-3999, C0-3999, CTC0-3, VB0-F9FF  
Retrun: EtherNet/IP Unit Response

### .sts(address)
Continuous Forced Set  
address = R0-199915, B0-7FFF, MR0-399915, LR0-99915, CR0-7915, VB0-F9FF  
num = number of written data  
Retrun: EtherNet/IP Unit Response

### .rss(address, num)
Continuous Forced Reset  
address = R0-199915, B0-7FFF, MR0-399915, LR0-99915, CR0-7915, VB0-F9FF  
num = number of written data  
Retrun: EtherNet/IP Unit Response

### .read(addresssuffix)
Data Read  
addresssuffix = DeviceType + DeviceNo + DataFormat  
 .e.g. MR0, DM0.U  
Return: EtherNet/IP Unit Response

### .reads(addresssuffix, num)
Consecutive Data Read  
addresssuffix = DeviceType + DeviceNo + DataFormat  
 .e.g. MR0, DM0.U  
num = number of read data  
Return: EtherNet/IP Unit Response (Data1 + 0x20 + Data2 + 0x20 ...)  

### .write(addresssuffix, data)
Write Data  
addresssuffix = DeviceType + DeviceNo + DataFormat  
 .e.g. MR0, DM0.U  
data = byte()  
Return: EtherNet/IP Unit Response

### .writes(addresssuffix, data)
Write Consecutive Data  
addresssuffix = DeviceType + DeviceNo + DataFormat  
 .e.g. MR0, DM0.U  
data = byte() (data1 + 0x20 + data2 + 0x20 ...) 
Return: EtherNet/IP Unit Response  

 
# Example
```
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
```
