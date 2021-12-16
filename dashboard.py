from tkinter import *
from  tkinter import ttk
from pyModbusTCP.client import ModbusClient
from UModuleDevice import *
from SModuleDevice import *
from math import *
import time
from datetime import datetime
import os
import numpy as np
ws  = Tk()
ws.title('Iga Socomec')
ws.geometry('1000x1600')
#Style
ws['bg'] = 'white'
style = ttk.Style()

style.configure('W.TButton',font=('Verdana', 11 ))
style.configure('Frame',bg="blue",font=('Verdana', 12 ))
soco_frame = Frame(ws)
myscrollbar=Scrollbar(soco_frame,orient="vertical")
myscrollbar.pack(side="right",fill="y")
soco_frame.pack()
socomeclist = ttk.Treeview(soco_frame,style="W.TButton", height=25)
socomeclist.tag_configure('OK', background='#F3F0D7',font=('Verdana',11),foreground='black')
socomeclist.tag_configure('NO', background='#FF7878',font=('Verdana',11),foreground='black')



#prepare header
socomeclist['columns'] = ('device_id', 'device_area','device_amper', 'device_voltage', 'device_status')
socomeclist.column("#0" ,width=10)
socomeclist.column("device_id")
socomeclist.column("device_area",anchor=CENTER)
socomeclist.column("device_amper",anchor=CENTER)
socomeclist.column("device_voltage",anchor=CENTER)
socomeclist.column("device_status",anchor=CENTER)

socomeclist.heading("#0",text="",anchor=CENTER)
socomeclist.heading("device_id",text="Id",anchor=W)
socomeclist.heading("device_area",text="Bolge",anchor=CENTER)
socomeclist.heading("device_amper",text="Akim",anchor=CENTER)
socomeclist.heading("device_voltage",text="RST",anchor=CENTER)
socomeclist.heading("device_status",text="Durum",anchor=CENTER)

linye_registers = [18183,18203,18223]

#Device1 U Module
s00 = Device("S00","172.16.39.200")
a = os.system('ping -c 1 '+ s00.host)
if(a == 0):
	###########-U-MODULE-################

	r1 = s00.prepareUmoduleRequest()
	volts = s00.getVolts(r1)
	status = s00.checkVoltStatus(volts)
	r1a = s00.prepareSmoduleRequest(s00.host,21)
	currents = s00.getCurrents(r1a,18183)
	socomeclist.insert(parent='',index='end',iid=1,text='',values=('1 U Module',s00.name,currents,volts[0:5], status,'PROBLEMLI'))

	#########-S-MODULE-LINYE11################
	s00linye11 = SModule("S00 - Linye11","172.16.39.200",11)
	s00smodule1 = s00linye11.createSModule()
	s00linye11_values= s00linye11.getSModuleCurrents(s00smodule1,linye_registers)
	s00linyeT = s00linye11_values[0]
	smoduldurum00 = s00linye11.getSModuleStatus(s00linyeT,1.3)
	socomeclist.insert(parent='',index='end',iid=301,text='',tags=(smoduldurum00),values=('--> Smodule1',s00linye11.name,s00linye11_values,"------", "---Calisma----"))
	socomeclist.move('301','1','1')

	#########-S-MODULE-LINYE12################
	s00linye12 = SModule("S00 - Linye 12","172.16.39.200",12)
	s00smodule2 = s00linye12.createSModule()
	s00linye12_values= s00linye12.getSModuleCurrents(s00smodule2,linye_registers)
	socomeclist.insert(parent='',index='end',iid=302,text='',tags=('NO'),values=('--> Smodule2',s00linye12.name,s00linye12_values,"------", "---Calisma----"))
	socomeclist.move('302','1','1')
	#########-S-MODULE-LINYE13################
	s00linye13 = SModule("S00 - Linye 13","172.16.39.200",13)
	s00smodule3 = s00linye13.createSModule()
	s00linye13_values= s00linye13.getSModuleCurrents(s00smodule3,linye_registers)
	socomeclist.insert(parent='',index='end',iid=303,text='',tags=('OK'),values=('--> Smodule3',s00linye13.name,s00linye13_values,"------", "---Calisma----"))
	socomeclist.move('303','1','1')
	#########-S-MODULE-LINYE14################
	s00linye14 = SModule("S00 - Linye 14","172.16.39.200",14)
	s00smodule4 = s00linye14.createSModule()
	s00linye14_values= s00linye14.getSModuleCurrents(s00smodule4,linye_registers)
	socomeclist.insert(parent='',index='end',iid=304,text='',tags=('NO'),values=('--> Smodule4',s00linye14.name,s00linye14_values,"------", "---Calisma----"))
	socomeclist.move('304','1','1')
	#########-S-MODULE-LINYE15################
	s00linye15 = SModule("S00 - Linye 15","172.16.39.200",15)
	s00smodule5 = s00linye15.createSModule()
	s00linye15_values= s00linye15.getSModuleCurrents(s00smodule5,linye_registers)
	socomeclist.insert(parent='',index='end',iid=305,text='',tags=('OK'),values=('--> Smodule5',s00linye15.name,s00linye15_values,"------", "---Calisma----"))
	socomeclist.move('305','1','1')
	#########-S-MODULE-LINYE16################
	s00linye16 = SModule("S00 - Linye 16","172.16.39.200",16)
	s00smodule6 = s00linye16.createSModule()
	s00linye16_values= s00linye16.getSModuleCurrents(s00smodule6,linye_registers)
	socomeclist.insert(parent='',index='end',iid=306,text='',tags=('OK'),values=('--> Smodule6',s00linye16.name,s00linye16_values,"------", "---Calisma----"))
	socomeclist.move('306','1','1')
	#########-S-MODULE-LINYE17################
	s00linye17 = SModule("S00 - Linye 17","172.16.39.200",17)
	s00smodule7 = s00linye17.createSModule()
	s00linye17_values= s00linye17.getSModuleCurrents(s00smodule7,linye_registers)
	socomeclist.insert(parent='',index='end',iid=307,text='',tags=('OK'),values=('--> Smodule7',s00linye17.name,s00linye17_values,"------", "---Calisma----"))
	socomeclist.move('307','1','1')
	#########-S-MODULE-LINYE18################
	s00linye18 = SModule("S00 - Linye 18","172.16.39.200",18)
	s00smodule8 = s00linye18.createSModule()
	s00linye18_values= s00linye18.getSModuleCurrents(s00smodule8,linye_registers)
	socomeclist.insert(parent='',index='end',iid=308,text='',tags=('OK'),values=('--> Smodule8',s00linye18.name,s00linye18_values,"------", "---Calisma----"))
	socomeclist.move('308','1','1')
	#########-S-MODULE-LINYE19################
	s00linye19 = SModule("S00 - Linye 19","172.16.39.200",19)
	s00smodule9 = s00linye19.createSModule()
	s00linye19_values= s00linye19.getSModuleCurrents(s00smodule9,linye_registers)
	socomeclist.insert(parent='',index='end',iid=309,text='',tags=('OK'),values=('--> Smodule9',s00linye19.name,s00linye19_values,"------", "---Calisma----"))
	socomeclist.move('309','1','1')
	#########-S-MODULE-LINYE20################
	s00linye20 = SModule("S00 - Linye 20","172.16.39.200",20)
	s00smodule20 = s00linye20.createSModule()
	s00linye20_values= s00linye20.getSModuleCurrents(s00smodule20,linye_registers)
	socomeclist.insert(parent='',index='end',iid=310,text='',tags=('OK'),values=('--> Smodule10',s00linye20.name,s00linye20_values,"------", "---Calisma----"))
	socomeclist.move('310','1','1')
	#########-S-MODULE-LINYE21################
	s00linye21 = SModule("S00 - Linye 21","172.16.39.200",21)
	s00smodule21 = s00linye21.createSModule()
	s00linye21_values= s00linye21.getSModuleCurrents(s00smodule21,linye_registers)
	socomeclist.insert(parent='',index='end',iid=311,text='',tags=('OK'),values=('--> Smodule11',s00linye21.name,s00linye21_values,"------", "---Calisma----"))
	socomeclist.move('311','1','1')
	#########-S-MODULE-LINYE22################
	s00linye22 = SModule("S00 - Linye 22","172.16.39.200",22)
	s00smodule22 = s00linye22.createSModule()
	s00linye22_values= s00linye22.getSModuleCurrents(s00smodule22,linye_registers)
	socomeclist.insert(parent='',index='end',iid=312,text='',tags=('OK'),values=('--> Smodule12',s00linye22.name,s00linye22_values,"------", "---Calisma----"))
	socomeclist.move('312','1','1')
	#########-S-MODULE-LINYE23################
	s00linye23 = SModule("S00 - Linye 23","172.16.39.200",23)
	s00smodule23 = s00linye23.createSModule()
	s00linye23_values= s00linye23.getSModuleCurrents(s00smodule23,linye_registers)
	socomeclist.insert(parent='',index='end',iid=313,text='',tags=('OK'),values=('--> Smodule13',s00linye23.name,s00linye23_values,"------", "---Calisma----"))
	socomeclist.move('313','1','1')
	#########-S-MODULE-LINYE24################
	s00linye24 = SModule("S00 - Linye 24","172.16.39.200",24)
	s00smodule24 = s00linye24.createSModule()
	s00linye24_values= s00linye24.getSModuleCurrents(s00smodule24,linye_registers)
	socomeclist.insert(parent='',index='end',iid=314,text='',tags=('OK'),values=('--> Smodule14',s00linye24.name,s00linye24_values,"------", "---Calisma----"))
	socomeclist.move('314','1','1')
	#########-S-MODULE-LINYE25################
	s00linye25 = SModule("S00 - Linye 25","172.16.39.200",25)
	s00smodule25 = s00linye25.createSModule()
	s00linye25_values= s00linye25.getSModuleCurrents(s00smodule25,linye_registers)
	socomeclist.insert(parent='',index='end',iid=315,text='',tags=('OK'),values=('--> Smodule15',s00linye25.name,s00linye25_values,"------", "---Calisma----"))
	socomeclist.move('315','1','1')
	#########-S-MODULE-LINYE26################
	s00linye26 = SModule("S00 - Linye 26","172.16.39.200",26)
	s00smodule26 = s00linye26.createSModule()
	s00linye26_values= s00linye26.getSModuleCurrents(s00smodule26,linye_registers)
	socomeclist.insert(parent='',index='end',iid=316,text='',tags=('OK'),values=('--> Smodule16',s00linye26.name,s00linye26_values,"------", "---Calisma----"))
	socomeclist.move('316','1','1')
	#########-S-MODULE-LINYE31################
	s00linye31 = SModule("S00 - Linye 31","172.16.39.200",31)
	s00smodule31 = s00linye31.createSModule()
	s00linye31_values= s00linye31.getSModuleCurrents(s00smodule31,linye_registers)
	socomeclist.insert(parent='',index='end',iid=321,text='',tags=('OK'),values=('--> Smodule17',s00linye31.name,s00linye31_values,"------", "---Calisma----"))
	socomeclist.move('321','1','1')
else:
	pass

# #Device2
s01 = Device("S01","172.16.39.201")
a = os.system('ping -c 1 '+ s01.host)
if(a==0):
	r2 = s01.prepareUmoduleRequest()
	volts2 = s01.getVolts(r2)
	status2 = s01.checkVoltStatus(volts2)
	r1a2 = s00.prepareSmoduleRequest(s01.host,21)
	currents2 = s01.getCurrents(r1a2,18183)
	socomeclist.insert(parent='',index='end',iid=2,text='',values=('2 U Module',s01.name,currents2,volts2[0:5], status2))
else:
	pass

#Device3
s03 = Device("S03","172.16.39.203")
a = os.system('ping -c 1 '+ s03.host)
if(a==0):
	r3 = s03.prepareUmoduleRequest()
	volts3 = s03.getVolts(r3)
	status3 = s03.checkVoltStatus(volts3)
	r1a3 = s03.prepareSmoduleRequest(s03.host,21)
	currents3 = s03.getCurrents(r1a3,18183)
	socomeclist.insert(parent='',index='end',iid=3,text='',values=('3 U Module',s03.name,currents3,volts3[0:5], status3))
else:
	pass

#Device4
s04 = Device("S04","172.16.39.204")
a = os.system('ping -c 1 '+ s04.host)
if(a==0):
	r4 = s04.prepareUmoduleRequest()
	volts4 = s04.getVolts(r4)
	status4 = s04.checkVoltStatus(volts4)
	r1a4 = s04.prepareSmoduleRequest(s04.host,11)
	currents4 = s04.getCurrents(r1a4,18183)
	socomeclist.insert(parent='',index='end',iid=4,text='',values=('4 U Module',s04.name,currents4,volts4[0:5], status4))
else:
	pass
#Device5
s05 = Device("S05","172.16.39.205")
a = os.system('ping -c 1 '+ s05.host)
if(a==0):
	r5 = s05.prepareUmoduleRequest()
	volts5 = s05.getVolts(r5)
	status5 = s05.checkVoltStatus(volts5)
	r1a5 = s05.prepareSmoduleRequest(s05.host,21)
	currents5 = s05.getCurrents(r1a5,18183)
	socomeclist.insert(parent='',index='end',iid=5,text='',values=('5 U Module',s05.name,currents5,volts5[0:5], status5))
else:
	pass

#Device6
s06 = Device("S06","172.16.39.206")
a = os.system('ping -c 1 '+ s05.host)
if(a==0):
	r6 = s06.prepareUmoduleRequest()
	volts6 = s06.getVolts(r6)
	status6 = s06.checkVoltStatus(volts6)
	r1a6 = s06.prepareSmoduleRequest(s06.host,11)
	currents6 = s06.getCurrents(r1a6,18183)
	socomeclist.insert(parent='',index='end',iid=6,text='',values=('6 U Module',s06.name,currents6,volts6[0:5], status6))
else:
	pass

#Device7
s07 = Device("S07","172.16.39.207")
a = os.system('ping -c 1 '+ s07.host)
if(a==0):
	r7 = s07.prepareUmoduleRequest()
	volts7 = s07.getVolts(r7)
	status7 = s07.checkVoltStatus(volts7)
	r1a7 = s07.prepareSmoduleRequest(s07.host,11)
	currents7 = s07.getCurrents(r1a7,18183)
	socomeclist.insert(parent='',index='end',iid=7,text='',values=('7 U Module',s07.name,currents7,volts7[0:5], status7))
else:
	pass

#Device8
s08 = Device("S08","172.16.39.208")
a = os.system('ping -c 1 '+ s08.host)
if(a==0):
	r8 = s08.prepareUmoduleRequest()
	volts8 = s08.getVolts(r8)
	status8 = s08.checkVoltStatus(volts8)
	r1a8 = s08.prepareSmoduleRequest(s08.host,11)
	currents8 = s08.getCurrents(r1a8,18183)
	socomeclist.insert(parent='',index='end',iid=8,text='',values=('8 U Module',s08.name,currents8,volts8[0:5], status8))

else:
	pass


#S11
s11 = Device("S11","172.16.39.211")
a = os.system('ping -c 1 '+ s11.host)
if(a==0):
	r9 = s11.prepareUmoduleRequest()
	volts9 = s11.getVolts(r9)
	status9 = s11.checkVoltStatus(volts9)
	r1a9 = s11.prepareSmoduleRequest(s11.host,11)
	currents9 = s11.getCurrents(r1a9,18183)
	socomeclist.insert(parent='',index='end',iid=9,text='',values=('9 U Module',s11.name,currents9,volts9[0:5], status9))
else:
	pass

#S12
s12 = Device("S12","172.16.39.212")
a = os.system('ping -c 1 '+ s12.host)
if(a ==0):	
	r10 = s12.prepareUmoduleRequest()
	volts10 = s12.getVolts(r10)
	status10 = s12.checkVoltStatus(volts10)
	r1a10 = s12.prepareSmoduleRequest(s12.host,11)
	currents10 = s12.getCurrents(r1a10,18183)
	socomeclist.insert(parent='',index='end',iid=10,text='',values=('10 U Module',s12.name,currents10,volts10[0:5], status10))

else:
	pass

#S13
s13 = Device("S13","172.16.39.213")
a = os.system('ping -c 1 '+ s13.host)
if(a==0):
	r11 = s13.prepareUmoduleRequest()
	volts11 = s13.getVolts(r11)
	status11 = s13.checkVoltStatus(volts11)
	r1a11 = s13.prepareSmoduleRequest(s13.host,11)
	currents11 = s13.getCurrents(r1a11,18183)
	socomeclist.insert(parent='',index='end',iid=11,text='',values=('11 U Module',s13.name,currents11,volts11[0:5], status11))
else:
	pass
#S14
s14 = Device("S14","172.16.39.214")
a = os.system('ping -c 1 '+ s14.host)
if(a==0):
	r12 = s14.prepareUmoduleRequest()
	volts12 = s14.getVolts(r12)
	status12 = s14.checkVoltStatus(volts12)
	r1a12 = s14.prepareSmoduleRequest(s14.host,11)
	currents12 = s14.getCurrents(r1a12,18183)
	socomeclist.insert(parent='',index='end',iid=12,text='',values=('12 U Module',s14.name,currents12,volts12[0:5], status12))
else:
	pass
#S15
s15 = Device("S15","172.16.39.215")
a = os.system('ping -c 1 '+ s15.host)
if(a==0):
	r13 = s15.prepareUmoduleRequest()
	volts13 = s15.getVolts(r13)
	status13 = s15.checkVoltStatus(volts13)
	r1a13 = s15.prepareSmoduleRequest(s15.host,11)
	currents13 = s15.getCurrents(r1a13,18183)
	socomeclist.insert(parent='',index='end',iid=13,text='',values=('13 U Module',s15.name,currents13,volts13[0:5], status13))
else:
	pass
#S16
s16 = Device("S16","172.16.39.216")
a = os.system('ping -c 1 '+ s16.host)
if(a==0):
	r14 = s16.prepareUmoduleRequest()
	volts14 = s16.getVolts(r14)
	status14 = s16.checkVoltStatus(volts14)
	r1a14 = s16.prepareSmoduleRequest(s16.host,11)
	currents14 = s16.getCurrents(r1a14,18183)
	socomeclist.insert(parent='',index='end',iid=14,text='',values=('14 U Module',s16.name,currents14,volts14[0:5], status14))
else:
	pass
#S17
s17 = Device("S17","172.16.39.217")
a = os.system('ping -c 1 '+ s17.host)
if(a==0):
	r15 = s17.prepareUmoduleRequest()
	volts15 = s17.getVolts(r15)
	status15 = s17.checkVoltStatus(volts15)
	r1a15 = s17.prepareSmoduleRequest(s17.host,13)
	currents15 = s17.getCurrents(r1a15,18203)
	socomeclist.insert(parent='',index='end',iid=15,text='',values=('15 U Module',s17.name,currents15,volts15[0:5], status15))
else:
	pass

#S27
s27 = Device("S27","172.16.39.227")
a = os.system('ping -c 1 '+ s27.host)
if(a==0):
	r16 = s27.prepareUmoduleRequest()
	volts16 = s27.getVolts(r16)
	status16 = s27.checkVoltStatus(volts16)
	r1a16 = s27.prepareSmoduleRequest(s27.host,11)
	currents16 = s27.getCurrents(r1a16,18183)
	socomeclist.insert(parent='',index='end',iid=27,text='',values=('16 U Module',s27.name,currents16,volts16[0:5], status16))

else:
	pass

#S29
s29 = Device("S29","172.16.39.229")
a = os.system('ping -c 1 '+ s29.host)
if(a==0):
	r17 = s29.prepareUmoduleRequest()
	volts17 = s29.getVolts(r17)
	status17 = s29.checkVoltStatus(volts17)
	r1a17 = s29.prepareSmoduleRequest(s29.host,11)
	currents17 = s29.getCurrents(r1a17,18183)
	socomeclist.insert(parent='',index='end',iid=17,text='',values=('17 U Module',s29.name,currents17,volts17[0:5], status17))

else:
	pass

#S30
s30 = Device("S30","172.16.39.230")
a = os.system('ping -c 1 '+ s30.host)
if(a==0):
	r18 = s30.prepareUmoduleRequest()
	volts18 = s30.getVolts(r18)
	status18 = s30.checkVoltStatus(volts18)
	r1a18 = s30.prepareSmoduleRequest(s30.host,11)
	currents18 = s30.getCurrents(r1a18,18183)
	socomeclist.insert(parent='',index='end',iid=18,text='',values=('18 U Module',s30.name,currents18,volts18[0:5], status18))
else:
	pass

#S34
s34 = Device("S34","172.16.39.234")
a = os.system('ping -c 1 '+ s34.host)
if(a==0):
	r19 = s34.prepareUmoduleRequest()
	volts19 = s34.getVolts(r19)
	status19 = s34.checkVoltStatus(volts19)
	r1a19 = s34.prepareSmoduleRequest(s34.host,11)
	currents19 = s34.getCurrents(r1a19,18183)
	socomeclist.insert(parent='',index='end',iid=19,text='',values=('19 U Module',s34.name,currents19,volts19[0:5], status19))
else:
	pass

s35 = Device("S35","172.16.39.235")
a = os.system('ping -c 1 '+ s35.host)
if(a==0):
	r20 = s35.prepareUmoduleRequest()
	volts20 = s35.getVolts(r20)
	status20 = s35.checkVoltStatus(volts20)
	r1a20 = s35.prepareSmoduleRequest(s35.host,11)
	currents20 = s35.getCurrents(r1a20,18183)
	socomeclist.insert(parent='',index='end',iid=20,text='',values=('20 U Module',s35.name,currents20,volts20[0:5], status20))
else:
	pass

s36 = Device("S36","172.16.39.236")
a = os.system('ping -c 1 '+ s36.host)
if(a==0):
	r21 = s36.prepareUmoduleRequest()
	volts21 = s36.getVolts(r21)
	status21 = s36.checkVoltStatus(volts21)
	r1a21 = s36.prepareSmoduleRequest(s36.host,11)
	currents21 = s36.getCurrents(r1a21,18183)
	socomeclist.insert(parent='',index='end',iid=21,text='',values=('21 U Module',s36.name,currents21,volts21[0:5], status21))
else:
	pass

s37 = Device("S37","172.16.39.237")
a = os.system('ping -c 1 '+ s37.host)
if(a==0):
	r22 = s37.prepareUmoduleRequest()
	volts22 = s37.getVolts(r22)
	status22 = s37.checkVoltStatus(volts22)
	r1a22 = s37.prepareSmoduleRequest(s37.host,11)
	currents22 = s37.getCurrents(r1a22,18183)
	socomeclist.insert(parent='',index='end',iid=22,text='',values=('22 U Module',s37.name,currents22,volts22[0:5], status22))
else:
	pass

s39 = Device("S39","172.16.39.239")
a = os.system('ping -c 1 '+ s39.host)
if(a==0):
	r23 = s39.prepareUmoduleRequest()
	volts23 = s39.getVolts(r23)
	status23 = s39.checkVoltStatus(volts23)
	r1a23 = s39.prepareSmoduleRequest(s39.host,11)
	currents23 = s37.getCurrents(r1a23,18183)
	socomeclist.insert(parent='',index='end',iid=23,text='',values=('23 U Module',s39.name,currents23,volts23[0:5], status23))
else:
	pass

s47 = Device("S47","172.16.39.247")
a = os.system('ping -c 1 '+ s47.host)
if(a==0):
	r24 = s47.prepareUmoduleRequest()
	volts24 = s47.getVolts(r24)
	status24 = s47.checkVoltStatus(volts24)
	r1a24 = s47.prepareSmoduleRequest(s47.host,11)
	currents24 = s47.getCurrents(r1a24,18183)
	socomeclist.insert(parent='',index='end',iid=24,text='',values=('24 U Module',s47.name,currents24,volts24[0:5], status24))
else:
	pass


socomeclist.pack()


def remove_all():
	for record in socomeclist.get_children():
		socomeclist.delete(record)
		
	#Device1
	s00 = Device("S00","172.16.39.200")
	a = os.system('ping -c 1 '+ s00.host)
	if(a == 0):
		r1 = s00.prepareUmoduleRequest()
		volts = s00.getVolts(r1)
		status = s00.checkVoltStatus(volts)
		r1a = s00.prepareSmoduleRequest(s00.host,21)
		currents = s00.getCurrents(r1a,18183)
		socomeclist.insert(parent='',index='end',iid=1,text='',values=('1',s00.name,currents,volts[0:5], status))
	else:
		pass

	# #Device2
	s01 = Device("S01","172.16.39.201")
	a = os.system('ping -c 1 '+ s01.host)
	if(a==0):
		r2 = s01.prepareUmoduleRequest()
		volts2 = s01.getVolts(r2)
		status2 = s01.checkVoltStatus(volts2)
		r1a2 = s00.prepareSmoduleRequest(s01.host,21)
		currents2 = s01.getCurrents(r1a2,18183)
		socomeclist.insert(parent='',index='end',iid=2,text='',values=('2',s01.name,currents2,volts2[0:5], status2))
	else:
		pass

	#Device3
	s03 = Device("S03","172.16.39.203")
	a = os.system('ping -c 1 '+ s03.host)
	if(a==0):
		r3 = s03.prepareUmoduleRequest()
		volts3 = s03.getVolts(r3)
		status3 = s03.checkVoltStatus(volts3)
		r1a3 = s03.prepareSmoduleRequest(s03.host,21)
		currents3 = s03.getCurrents(r1a3,18183)
		socomeclist.insert(parent='',index='end',iid=3,text='',values=('3',s03.name,currents3,volts3[0:5], status3))
	else:
		pass

	#Device4
	s04 = Device("S04","172.16.39.204")
	a = os.system('ping -c 1 '+ s04.host)
	if(a==0):
		r4 = s04.prepareUmoduleRequest()
		volts4 = s04.getVolts(r4)
		status4 = s04.checkVoltStatus(volts4)
		r1a4 = s04.prepareSmoduleRequest(s04.host,11)
		currents4 = s04.getCurrents(r1a4,18183)
		socomeclist.insert(parent='',index='end',iid=4,text='',values=('4',s04.name,currents4,volts4[0:5], status4))
	else:
		pass
	#Device5
	s05 = Device("S05","172.16.39.205")
	a = os.system('ping -c 1 '+ s05.host)
	if(a==0):
		r5 = s05.prepareUmoduleRequest()
		volts5 = s05.getVolts(r5)
		status5 = s05.checkVoltStatus(volts5)
		r1a5 = s05.prepareSmoduleRequest(s05.host,21)
		currents5 = s05.getCurrents(r1a5,18183)
		socomeclist.insert(parent='',index='end',iid=5,text='',values=('5',s05.name,currents5,volts5[0:5], status5))
	else:
		pass

	#Device6
	s06 = Device("S06","172.16.39.206")
	a = os.system('ping -c 1 '+ s05.host)
	if(a==0):
		r6 = s06.prepareUmoduleRequest()
		volts6 = s06.getVolts(r6)
		status6 = s06.checkVoltStatus(volts6)
		r1a6 = s06.prepareSmoduleRequest(s06.host,11)
		currents6 = s06.getCurrents(r1a6,18183)
		socomeclist.insert(parent='',index='end',iid=6,text='',values=('6',s06.name,currents6,volts6[0:5], status6))
	else:
		pass

	#Device7
	s07 = Device("S07","172.16.39.207")
	a = os.system('ping -c 1 '+ s07.host)
	if(a==0):
		r7 = s07.prepareUmoduleRequest()
		volts7 = s07.getVolts(r7)
		status7 = s07.checkVoltStatus(volts7)
		r1a7 = s07.prepareSmoduleRequest(s07.host,11)
		currents7 = s07.getCurrents(r1a7,18183)
		socomeclist.insert(parent='',index='end',iid=7,text='',values=('7',s07.name,currents7,volts7[0:5], status7))
	else:
		pass

	#Device8
	s08 = Device("S08","172.16.39.208")
	a = os.system('ping -c 1 '+ s08.host)
	if(a==0):
		r8 = s08.prepareUmoduleRequest()
		volts8 = s08.getVolts(r8)
		status8 = s08.checkVoltStatus(volts8)
		r1a8 = s08.prepareSmoduleRequest(s08.host,11)
		currents8 = s08.getCurrents(r1a8,18183)
		socomeclist.insert(parent='',index='end',iid=8,text='',values=('8',s08.name,currents8,volts8[0:5], status8))

	else:
		pass


	#S11
	s11 = Device("S11","172.16.39.211")
	a = os.system('ping -c 1 '+ s11.host)
	if(a==0):
		r9 = s11.prepareUmoduleRequest()
		volts9 = s11.getVolts(r9)
		status9 = s11.checkVoltStatus(volts9)
		r1a9 = s11.prepareSmoduleRequest(s11.host,11)
		currents9 = s11.getCurrents(r1a9,18183)
		socomeclist.insert(parent='',index='end',iid=9,text='',values=('9',s11.name,currents9,volts9[0:5], status9))
	else:
		pass

	#S12
	s12 = Device("S12","172.16.39.212")
	a = os.system('ping -c 1 '+ s12.host)
	if(a ==0):	
		r10 = s12.prepareUmoduleRequest()
		volts10 = s12.getVolts(r10)
		status10 = s12.checkVoltStatus(volts10)
		r1a10 = s12.prepareSmoduleRequest(s12.host,11)
		currents10 = s12.getCurrents(r1a10,18183)
		socomeclist.insert(parent='',index='end',iid=10,text='',values=('10',s12.name,currents10,volts10[0:5], status10))

	else:
		pass

	#S13
	s13 = Device("S13","172.16.39.213")
	a = os.system('ping -c 1 '+ s13.host)
	if(a==0):
		r11 = s13.prepareUmoduleRequest()
		volts11 = s13.getVolts(r11)
		status11 = s13.checkVoltStatus(volts11)
		r1a11 = s13.prepareSmoduleRequest(s13.host,11)
		currents11 = s13.getCurrents(r1a11,18183)
		socomeclist.insert(parent='',index='end',iid=11,text='',values=('11',s13.name,currents11,volts11[0:5], status11))
	else:
		pass
	#S14
	s14 = Device("S14","172.16.39.214")
	a = os.system('ping -c 1 '+ s14.host)
	if(a==0):
		r12 = s14.prepareUmoduleRequest()
		volts12 = s14.getVolts(r12)
		status12 = s14.checkVoltStatus(volts12)
		r1a12 = s14.prepareSmoduleRequest(s14.host,11)
		currents12 = s14.getCurrents(r1a12,18183)
		socomeclist.insert(parent='',index='end',iid=12,text='',values=('12',s14.name,currents12,volts12[0:5], status12))
	else:
		pass
	#S15
	s15 = Device("S15","172.16.39.215")
	a = os.system('ping -c 1 '+ s15.host)
	if(a==0):
		r13 = s15.prepareUmoduleRequest()
		volts13 = s15.getVolts(r13)
		status13 = s15.checkVoltStatus(volts13)
		r1a13 = s15.prepareSmoduleRequest(s15.host,11)
		currents13 = s15.getCurrents(r1a13,18183)
		socomeclist.insert(parent='',index='end',iid=13,text='',values=('13',s15.name,currents13,volts13[0:5], status13))
	else:
		pass
	#S16
	s16 = Device("S16","172.16.39.216")
	a = os.system('ping -c 1 '+ s16.host)
	if(a==0):
		r14 = s16.prepareUmoduleRequest()
		volts14 = s16.getVolts(r14)
		status14 = s16.checkVoltStatus(volts14)
		r1a14 = s16.prepareSmoduleRequest(s16.host,11)
		currents14 = s16.getCurrents(r1a14,18183)
		socomeclist.insert(parent='',index='end',iid=14,text='',values=('14',s16.name,currents14,volts14[0:5], status14))
	else:
		pass
	#S17
	s17 = Device("S17","172.16.39.217")
	a = os.system('ping -c 1 '+ s17.host)
	if(a==0):
		r15 = s17.prepareUmoduleRequest()
		volts15 = s17.getVolts(r15)
		status15 = s17.checkVoltStatus(volts15)
		r1a15 = s17.prepareSmoduleRequest(s17.host,13)
		currents15 = s17.getCurrents(r1a15,18203)
		socomeclist.insert(parent='',index='end',iid=15,text='',values=('15',s17.name,currents15,volts15[0:5], status15))
	else:
		pass

	#S27
	s27 = Device("S27","172.16.39.227")
	a = os.system('ping -c 1 '+ s27.host)
	if(a==0):
		r16 = s27.prepareUmoduleRequest()
		volts16 = s27.getVolts(r16)
		status16 = s27.checkVoltStatus(volts16)
		r1a16 = s27.prepareSmoduleRequest(s27.host,11)
		currents16 = s27.getCurrents(r1a16,18183)
	else:
		pass

	#S29
	s29 = Device("S29","172.16.39.229")
	a = os.system('ping -c 1 '+ s29.host)
	if(a==0):
		r17 = s29.prepareUmoduleRequest()
		volts17 = s29.getVolts(r17)
		status17 = s29.checkVoltStatus(volts17)
		r1a17 = s29.prepareSmoduleRequest(s29.host,11)
		currents17 = s29.getCurrents(r1a17,18183)
		socomeclist.insert(parent='',index='end',iid=17,text='',values=('17',s29.name,currents17,volts17[0:5], status17))

	else:
		pass

	#S30
	s30 = Device("S30","172.16.39.230")
	a = os.system('ping -c 1 '+ s30.host)
	if(a==0):
		r18 = s30.prepareUmoduleRequest()
		volts18 = s30.getVolts(r18)
		status18 = s30.checkVoltStatus(volts18)
		r1a18 = s30.prepareSmoduleRequest(s30.host,11)
		currents18 = s30.getCurrents(r1a18,18183)
		socomeclist.insert(parent='',index='end',iid=18,text='',values=('18',s30.name,currents18,volts18[0:5], status18))
	else:
		pass

	#S34
	s34 = Device("S34","172.16.39.234")
	a = os.system('ping -c 1 '+ s34.host)
	if(a==0):
		r19 = s34.prepareUmoduleRequest()
		volts19 = s34.getVolts(r19)
		status19 = s34.checkVoltStatus(volts19)
		r1a19 = s34.prepareSmoduleRequest(s34.host,11)
		currents19 = s34.getCurrents(r1a19,18183)
		socomeclist.insert(parent='',index='end',iid=19,text='',values=('19',s34.name,currents19,volts19[0:5], status19))
	else:
		pass

	s35 = Device("S35","172.16.39.235")
	a = os.system('ping -c 1 '+ s35.host)
	if(a==0):
		r20 = s35.prepareUmoduleRequest()
		volts20 = s35.getVolts(r20)
		status20 = s35.checkVoltStatus(volts20)
		r1a20 = s35.prepareSmoduleRequest(s35.host,11)
		currents20 = s35.getCurrents(r1a20,18183)
		socomeclist.insert(parent='',index='end',iid=20,text='',values=('20',s35.name,currents20,volts20[0:5], status20))
	else:
		pass

	s36 = Device("S36","172.16.39.236")
	a = os.system('ping -c 1 '+ s36.host)
	if(a==0):
		r21 = s36.prepareUmoduleRequest()
		volts21 = s36.getVolts(r21)
		status21 = s36.checkVoltStatus(volts21)
		r1a21 = s36.prepareSmoduleRequest(s36.host,11)
		currents21 = s36.getCurrents(r1a21,18183)
		socomeclist.insert(parent='',index='end',iid=21,text='',values=('21',s36.name,currents21,volts21[0:5], status21))
	else:
		pass

	s37 = Device("S37","172.16.39.237")
	a = os.system('ping -c 1 '+ s37.host)
	if(a==0):
		r22 = s37.prepareUmoduleRequest()
		volts22 = s37.getVolts(r22)
		status22 = s37.checkVoltStatus(volts22)
		r1a22 = s37.prepareSmoduleRequest(s37.host,11)
		currents22 = s37.getCurrents(r1a22,18183)
		socomeclist.insert(parent='',index='end',iid=22,text='',values=('22',s37.name,currents22,volts22[0:5], status22))
	else:
		pass

	s39 = Device("S39","172.16.39.239")
	a = os.system('ping -c 1 '+ s39.host)
	if(a==0):
		r23 = s39.prepareUmoduleRequest()
		volts23 = s39.getVolts(r23)
		status23 = s39.checkVoltStatus(volts23)
		r1a23 = s39.prepareSmoduleRequest(s39.host,11)
		currents23 = s37.getCurrents(r1a23,18183)
		socomeclist.insert(parent='',index='end',iid=23,text='',values=('23',s39.name,currents23,volts23[0:5], status23))
	else:
		pass

	s47 = Device("S47","172.16.39.247")
	a = os.system('ping -c 1 '+ s47.host)
	if(a==0):
		r24 = s47.prepareUmoduleRequest()
		volts24 = s47.getVolts(r24)
		status24 = s47.checkVoltStatus(volts24)
		r1a24 = s47.prepareSmoduleRequest(s47.host,11)
		currents24 = s47.getCurrents(r1a24,18183)
		socomeclist.insert(parent='',index='end',iid=24,text='',values=('24',s47.name,currents24,volts24[0:5], status24))
	else:
		pass


socomeclist.pack()
#Device111.name,currents9,volts9[0:5], status9))

def update_ui():
	return

exit = ttk.Button(ws, text='KAPAT', style='W.TButton', command=ws.destroy).pack(pady=10)
update_button = ttk.Button(ws,text="Guncelle", style='W.TButton', command=remove_all)
update_button.pack()


ws.resizable(False,False)
ws.mainloop()



