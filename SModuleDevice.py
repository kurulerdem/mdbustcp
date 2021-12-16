from pyModbusTCP.client import ModbusClient
import time
import numpy as np
class SModule:
	def __init__(self,name,host,uid):
		self.name = name
		self.host = host
		self.uid = uid
	#Prepare request
	def createSModule(self):
		o = ModbusClient(host=self.host, port=502, unit_id=self.uid, auto_open=True);
		return o

	def getSModuleCurrents(self,c,register):
		i=0
		linye_akim = []
		while(i<len(register)):
			response = c.read_holding_registers(register[i],1);
			linye_akim.append(response)
			i+=1
		list(np.float_(linye_akim))
		return linye_akim


	def getSModuleStatus(self,linye_degerler,limit):
		for deger in linye_degerler:
			if deger < limit:
				return 'NO'
			else:
				return 'OK'
		
		