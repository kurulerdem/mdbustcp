# TCP baglantisi
from pyModbusTCP.client import ModbusClient
import time
c = ModbusClient(host="172.16.39.207", port=502, unit_id=2, auto_open=True);
regs = c.read_holding_registers(36869, 6);
#while(True):
#	time.sleep(2)
#	print(regs);
#18183 Load 1
#18203 Load 2
#18223 Load 3
