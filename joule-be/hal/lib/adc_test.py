from MCP342x import MCP342x
import smbus

import logging

bus = smbus.SMBus(1)

addr68_ch0 = MCP342x(bus, 0x6e, channel=0, resolution=12)
addr68_ch1 = MCP342x(bus, 0x6e, channel=1, resolution=12)
addr68_ch2 = MCP342x(bus, 0x6e, channel=2, resolution=12)
addr68_ch3 = MCP342x(bus, 0x6e, channel=3, resolution=12)

adcs = [addr68_ch0, addr68_ch1, addr68_ch2, addr68_ch3]
r = MCP342x.convert_and_read_many(adcs, samples=1)
print('return values: ')
print(r)