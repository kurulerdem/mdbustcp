from pyModbusTCP.client import ModbusClient
from device import *
from math import *
import time
from datetime import datetime
# TCP baglantisi
#c = ModbusClient(host="172.16.39.201", port=502, unit_id=2, auto_open=True);
#regs = c.read_holding_registers(36869, 6);
#volt1 = regs[1] * 0.01
#volt2 = regs[3] * 0.01
#volt3 = regs[5] * 0.01

#avg= round((volt1 + volt2 + volt3 )/ 3)
#if(avg>200):
#	print("OK")
#	print(avg);
#else:
#	print("ERROR")
#	print(avg);


#Veri cekme	
#def fetch_s1():
#	while(True):
#		if (regs):
#			print(regs);
#		else:
#			print('Veri Alinamadi');
#fetch_s1()
#
#

def start():
	while(True):
		d1 = Device("S1","172.16.39.247")

#prepare volts values 
		r1v = d1.prepareUmoduleRequest()
		volts = d1.getVolts(r1v)
		statusv = d1.checkVoltStatus(volts)

#prepare currents values

		r1a = d1.prepareSmoduleRequest(d1.host,21)
		currents = d1.getCurrents(r1a,18183)
		print("---------Bolge----------")
		print(d1.name)
		print("-----RST Degerleri------")
		print(volts)
		print("--------DURUM-----------")
		print(statusv)
		print("-----AKIM DEGERLERI-----")
		print(currents)
		print("""              


		""")
		time.sleep(2)
#d2 = Device('S2',"172.16.39.201",2,18444,2);
#r2 = d2.prepareRequest(d2.host,d2.unit_id)
#result2 = d2.getResponse(r2,d2.register,d2.quantity);
#print(result2)
#time.sleep(10);
def currentTest():
	while(True):
		d1 = Device("Apron","172.16.39.247")
		r1 = d1.prepareSmoduleRequest(d1.host,21)
		currents = d1.getCurrents(r1,18223)
		print(currents)
		time.sleep(2)
#currentTest()
#create device

start()

