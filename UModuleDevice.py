from pyModbusTCP.client import ModbusClient
import time
class Device:
	def __init__(self,name,host):
		self.name = name
		self.host = host
	#Prepare request
	def prepareUmoduleRequest(self):
		o = ModbusClient(host=self.host, port=502, unit_id=2, auto_open=True);
		return o
	#Fetching data
	def getVolts(self,c):
		response = c.read_holding_registers(36869,6);
		R = response[1] * 0.01
		S = response[3] * 0.01
		T = response[5] * 0.01
		volts= [R,"/",S,"/",T];
		return volts;
	def checkVoltStatus(self,volts):
		avg= round((volts[0] + volts[2] + volts[4])/ 3)
		if(volts[0]<=220 or volts[2]<=220 or volts[4]<=220):
			result = "Voltaj 220 altinda !";
			return result
		elif(volts[0]>=240 or volts[2]>=240 or volts[4]>=240):
			result= "Voltaj 220 ustunde !"
			return result
		else:
			result= "Normal Voltaj"
			return result
	
	def prepareSmoduleRequest(self,host,uid):
		o = ModbusClient(host=self.host,port=502,unit_id=uid,auto_open=True);
		return o

	def getCurrents(self,c,register):
		response = c.read_holding_registers(register,2);
		return response;
	def SModuleCurrents(self,c,linyeler):
		i=0
		linye_akim = []
		while(i<len(linyeler)):
			response = c.read_holding_registers(linyeler[i],1);
			linye_akim.append(response)
			i+=1
		return linye_akim
