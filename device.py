from pyModbusTCP.client import ModbusClient
import time
class Device:
	def __init__(self,name,host):
		self.name = name
		self.host = host
	#Prepare request
	def prepareUmoduleRequest(self):
		o = ModbusClient(host=self.host, port=502, unit_id=2, auto_open=True);
		return o;
	#Fetching data
	def getVolts(self,c):
		response = c.read_holding_registers(36869,6);
		R = response[1] * 0.01
		S = response[3] * 0.01
		T = response[5] * 0.01
		volts= [R,S,T];
		return volts;
	def checkVoltStatus(self,volts):
		avg= round((volts[0] + volts[1] + volts[2])/ 3)
		if(volts[0]<=220 or volts[1]<=220 or volts[2]<=220):
			result = "Voltaj 220 altinda !";
			return result
		elif(volts[0]>=240 or volts[1]>=240 or volts[2]>=240):
			result= "Voltaj 220 ustunde !"
			return result
		else:
			result= "Normal Voltaj"
			return result
	
	def prepareSmoduleRequest(self,host,uid):
		o = ModbusClient(host=self.host,port=502,unit_id=uid,auto_open=True);
		return o;

	def getCurrents(self,c,register):
		response = c.read_holding_registers(register,2);
		return response;