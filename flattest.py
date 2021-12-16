# TCP baglantisi
from pyModbusTCP.client import ModbusClient
import time
c = ModbusClient(host="172.16.39.201", port=502, unit_id=13, auto_open=True);
regs = c.read_holding_registers(18183, 6);
liste =[]
for x in range (0,5):
	liste.append(x)


print(type(liste))

for y in liste:
	if(y < 3.2):
		print('Ok')
	else:
		print('Problem')
#18183 Load 1
#18203 Load 2
#18223 Load 3
