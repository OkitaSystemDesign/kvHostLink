from kvhostlink import kvHostLink

try:
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

except Exception as e:
    print(e)
