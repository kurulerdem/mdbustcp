from tkinter import *
from  tkinter import ttk
from pyModbusTCP.client import ModbusClient
from device import *
from math import *
import time
from datetime import datetime
ws  = Tk()
ws.title('Iga Socomec')
ws.geometry('1000x1000')
ws['bg'] = 'white'

#Style

style = ttk.Style()
style.theme_use("clam")
style.configure('W.TButton',font=('Verdana', 14 ))
soco_frame = Frame(ws)
soco_frame.pack()
socomeclist = ttk.Treeview(soco_frame,height=25)


#Device1
d1 = Device("S00","172.16.39.200")
r1 = d1.prepareUmoduleRequest()
volts = d1.getVolts(r1)
status = d1.checkVoltStatus(volts)
r1a = d1.prepareSmoduleRequest(d1.host,21)
currents = d1.getCurrents(r1a,18183)

#Device2
d2 = Device("S01","172.16.39.201")
r2 = d2.prepareUmoduleRequest()
volts2 = d2.getVolts(r2)
status2 = d2.checkVoltStatus(volts2)
r1a2 = d1.prepareSmoduleRequest(d2.host,21)
currents2 = d2.getCurrents(r1a2,18183)

#Device3
d3 = Device("S03","172.16.39.203")
r3 = d3.prepareUmoduleRequest()
volts3 = d3.getVolts(r3)
status3 = d3.checkVoltStatus(volts3)
r1a3 = d3.prepareSmoduleRequest(d3.host,21)
currents3 = d3.getCurrents(r1a3,18183)

#Device4
d4 = Device("S04","172.16.39.204")
r4 = d4.prepareUmoduleRequest()
volts4 = d4.getVolts(r4)
status4 = d4.checkVoltStatus(volts4)
r1a4 = d4.prepareSmoduleRequest(d4.host,11)
currents4 = d4.getCurrents(r1a4,18183)

#Device5
d5 = Device("S05","172.16.39.205")
r5 = d5.prepareUmoduleRequest()
volts5 = d5.getVolts(r5)
status5 = d5.checkVoltStatus(volts5)
r1a5 = d5.prepareSmoduleRequest(d5.host,21)
currents5 = d5.getCurrents(r1a5,18183)

#Device6
d6 = Device("S06","172.16.39.206")
r6 = d6.prepareUmoduleRequest()
volts6 = d6.getVolts(r6)
status6 = d6.checkVoltStatus(volts6)
r1a6 = d6.prepareSmoduleRequest(d6.host,11)
currents6 = d6.getCurrents(r1a6,18183)

#Device7
d7 = Device("S07","172.16.39.207")
r7 = d7.prepareUmoduleRequest()
volts7 = d7.getVolts(r7)
status7 = d7.checkVoltStatus(volts7)
r1a7 = d7.prepareSmoduleRequest(d7.host,11)
currents7 = d7.getCurrents(r1a7,18183)

#Device8
d8 = Device("S08","172.16.39.208")
r8 = d8.prepareUmoduleRequest()
volts8 = d8.getVolts(r8)
status8 = d8.checkVoltStatus(volts8)
r1a8 = d8.prepareSmoduleRequest(d8.host,11)
currents8 = d8.getCurrents(r1a8,18183)


#Device9
d9 = Device("S11","172.16.39.211")
r9 = d9.prepareUmoduleRequest()
volts9 = d9.getVolts(r9)
status9 = d9.checkVoltStatus(volts9)
r1a9 = d9.prepareSmoduleRequest(d9.host,11)
currents9 = d9.getCurrents(r1a9,18183)

#Device10
d10 = Device("S12","172.16.39.212")
r10 = d10.prepareUmoduleRequest()
volts10 = d10.getVolts(r10)
status10 = d10.checkVoltStatus(volts10)
r1a10 = d10.prepareSmoduleRequest(d10.host,11)
currents10 = d10.getCurrents(r1a10,18183)

#Device11
d11 = Device("S13","172.16.39.213")
r11 = d11.prepareUmoduleRequest()
volts11 = d11.getVolts(r11)
status11 = d11.checkVoltStatus(volts11)
r1a11 = d11.prepareSmoduleRequest(d11.host,11)
currents11 = d11.getCurrents(r1a11,18183)

#Device12
d12 = Device("S14","172.16.39.214")
r12 = d12.prepareUmoduleRequest()
volts12 = d12.getVolts(r12)
status12 = d12.checkVoltStatus(volts12)
r1a12 = d12.prepareSmoduleRequest(d12.host,11)
currents12 = d12.getCurrents(r1a12,18183)

#Device13
d13 = Device("S15","172.16.39.214")
r13 = d13.prepareUmoduleRequest()
volts13 = d13.getVolts(r13)
status13 = d13.checkVoltStatus(volts13)
r1a13 = d13.prepareSmoduleRequest(d13.host,11)
currents13 = d13.getCurrents(r1a13,18183)
#Device14
d14 = Device("S16","172.16.39.216")
r14 = d14.prepareUmoduleRequest()
volts14 = d14.getVolts(r14)
status14 = d14.checkVoltStatus(volts14)
r1a14 = d14.prepareSmoduleRequest(d14.host,11)
currents14 = d14.getCurrents(r1a14,18183)
#Device15
d15 = Device("S17","172.16.39.217")
r15 = d15.prepareUmoduleRequest()
volts15 = d15.getVolts(r15)
status15 = d15.checkVoltStatus(volts15)
r1a15 = d15.prepareSmoduleRequest(d15.host,13)
currents15 = d15.getCurrents(r1a15,18203)

#Device16
d16 = Device("S27","172.16.39.227")
r16 = d16.prepareUmoduleRequest()
volts16 = d16.getVolts(r16)
status16 = d16.checkVoltStatus(volts16)
r1a16 = d16.prepareSmoduleRequest(d16.host,11)
currents16 = d16.getCurrents(r1a16,18183)

#Device 17
#d17 = Device("S29","172.16.39.229")
#r17 = d17.prepareUmoduleRequest()
#volts17 = d17.getVolts(r17)
#status17 = d17.checkVoltStatus(volts17)
#r1a17 = d17.prepareSmoduleRequest(d17.host,11)
#currents17 = d17.getCurrents(r1a17,18183)

#Device 18
d18 = Device("S30","172.16.39.230")
r18 = d18.prepareUmoduleRequest()
volts18 = d18.getVolts(r18)
status18 = d18.checkVoltStatus(volts18)
r1a18 = d18.prepareSmoduleRequest(d18.host,11)
currents18 = d18.getCurrents(r1a18,18183)


#Device 19
#d19 = Device("S34","172.16.39.234")
#r19 = d19.prepareUmoduleRequest()
#volts19 = d19.getVolts(r19)
#status19 = d19.checkVoltStatus(volts19)
#r1a19 = d19.prepareSmoduleRequest(d19.host,11)
#currents19 = d19.getCurrents(r1a19,18183)

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

#insert devices..
socomeclist.insert(parent='',index='end',iid=1,text='',values=('1',d1.name,currents,volts[0:5], status))
socomeclist.insert(parent='',index='end',iid=2,text='',values=('2',d2.name,currents2,volts2[0:5], status2))
socomeclist.insert(parent='',index='end',iid=3,text='',values=('3',d3.name,currents3,volts3[0:5], status3))
socomeclist.insert(parent='',index='end',iid=4,text='',values=('4',d4.name,currents4,volts4[0:5], status4))
socomeclist.insert(parent='',index='end',iid=5,text='',values=('5',d5.name,currents5,volts5[0:5], status5))
socomeclist.insert(parent='',index='end',iid=6,text='',values=('6',d6.name,currents6,volts6[0:5], status6))
socomeclist.insert(parent='',index='end',iid=7,text='',values=('7',d7.name,currents7,volts7[0:5], status7))
socomeclist.insert(parent='',index='end',iid=8,text='',values=('8',d8.name,currents8,volts8[0:5], status8))
socomeclist.insert(parent='',index='end',iid=9,text='',values=('9',d9.name,currents9,volts9[0:5], status9))
socomeclist.insert(parent='',index='end',iid=10,text='',values=('10',d10.name,currents10,volts10[0:5], status10))
socomeclist.insert(parent='',index='end',iid=11,text='',values=('11',d11.name,currents11,volts11[0:5], status11))
socomeclist.insert(parent='',index='end',iid=12,text='',values=('12',d12.name,currents12,volts12[0:5], status12))
socomeclist.insert(parent='',index='end',iid=13,text='',values=('13',d13.name,currents13,volts13[0:5], status13))
socomeclist.insert(parent='',index='end',iid=14,text='',values=('14',d14.name,currents14,volts14[0:5], status14))
socomeclist.insert(parent='',index='end',iid=15,text='',values=('15',d15.name,currents15,volts15[0:5], status15))
socomeclist.insert(parent='',index='end',iid=16,text='',values=('16',d16.name,currents16,volts16[0:5], status16))
#socomeclist.insert(parent='',index='end',iid=17,text='',values=('17',d17.name,currents17,volts17[0:5], status17))
socomeclist.insert(parent='',index='end',iid=18,text='',values=('18',d18.name,currents18,volts18[0:5], status18))
#socomeclist.insert(parent='',index='end',iid=19,text='',values=('19',d19.name,currents19,volts19[0:5], status19))



#add child
socomeclist.insert(parent='',index='end',iid=31,text='',values=('--> Smodule1',d18.name,currents18,volts18[0:5], status18))
socomeclist.move('31','1','1')

socomeclist.pack()


def remove_all():
	for record in socomeclist.get_children():
		socomeclist.delete(record)
		
	

	
#Device1
	d1 = Device("S00","172.16.39.200")
	r1 = d1.prepareUmoduleRequest()
	volts = d1.getVolts(r1)
	status = d1.checkVoltStatus(volts)
	r1a = d1.prepareSmoduleRequest(d1.host,21)
	currents = d1.getCurrents(r1a,18183)

#Device2
	d2 = Device("S01","172.16.39.201")
	r2 = d2.prepareUmoduleRequest()
	volts2 = d2.getVolts(r2)
	status2 = d2.checkVoltStatus(volts2)
	r1a2 = d1.prepareSmoduleRequest(d2.host,21)
	currents2 = d2.getCurrents(r1a2,18183)

#Device3
	d3 = Device("S03","172.16.39.203")
	r3 = d3.prepareUmoduleRequest()
	volts3 = d3.getVolts(r3)
	status3 = d3.checkVoltStatus(volts3)
	r1a3 = d3.prepareSmoduleRequest(d3.host,21)
	currents3 = d3.getCurrents(r1a3,18183)

#Device4
	d4 = Device("S04","172.16.39.204")
	r4 = d4.prepareUmoduleRequest()
	volts4 = d4.getVolts(r4)
	status4 = d4.checkVoltStatus(volts4)
	r1a4 = d4.prepareSmoduleRequest(d4.host,11)
	currents4 = d4.getCurrents(r1a4,18183)

#Device5
	d5 = Device("S05","172.16.39.205")
	r5 = d5.prepareUmoduleRequest()
	volts5 = d5.getVolts(r5)
	status5 = d5.checkVoltStatus(volts5)
	r1a5 = d5.prepareSmoduleRequest(d5.host,21)
	currents5 = d5.getCurrents(r1a5,18183)

#Device6
	d6 = Device("S06","172.16.39.206")
	r6 = d6.prepareUmoduleRequest()
	volts6 = d6.getVolts(r6)
	status6 = d6.checkVoltStatus(volts6)
	r1a6 = d6.prepareSmoduleRequest(d6.host,11)
	currents6 = d6.getCurrents(r1a6,18183)

#Device7
	d7 = Device("S07","172.16.39.207")
	r7 = d7.prepareUmoduleRequest()
	volts7 = d7.getVolts(r7)
	status7 = d7.checkVoltStatus(volts7)
	r1a7 = d7.prepareSmoduleRequest(d7.host,11)
	currents7 = d7.getCurrents(r1a7,18183)

#Device8
	d8 = Device("S08","172.16.39.208")
	r8 = d8.prepareUmoduleRequest()
	volts8 = d8.getVolts(r8)
	status8 = d8.checkVoltStatus(volts8)
	r1a8 = d8.prepareSmoduleRequest(d8.host,11)
	currents8 = d8.getCurrents(r1a8,18183)


#Device9
	d9 = Device("S11","172.16.39.211")
	r9 = d9.prepareUmoduleRequest()
	volts9 = d9.getVolts(r9)
	status9 = d9.checkVoltStatus(volts9)
	r1a9 = d9.prepareSmoduleRequest(d9.host,11)
	currents9 = d9.getCurrents(r1a9,18183)

#Device10
	d10 = Device("S12","172.16.39.212")
	r10 = d10.prepareUmoduleRequest()
	volts10 = d10.getVolts(r10)
	status10 = d10.checkVoltStatus(volts10)
	r1a10 = d10.prepareSmoduleRequest(d10.host,11)
	currents10 = d10.getCurrents(r1a10,18183)

#Device11
	d11 = Device("S13","172.16.39.213")
	r11 = d11.prepareUmoduleRequest()
	volts11 = d11.getVolts(r11)
	status11 = d11.checkVoltStatus(volts11)
	r1a11 = d11.prepareSmoduleRequest(d11.host,11)
	currents11 = d11.getCurrents(r1a11,18183)

#Device12
	d12 = Device("S14","172.16.39.214")
	r12 = d12.prepareUmoduleRequest()
	volts12 = d12.getVolts(r12)
	status12 = d12.checkVoltStatus(volts12)
	r1a12 = d12.prepareSmoduleRequest(d12.host,11)
	currents12 = d12.getCurrents(r1a12,18183)

#Device13
	d13 = Device("S15","172.16.39.214")
	r13 = d13.prepareUmoduleRequest()
	volts13 = d13.getVolts(r13)
	status13 = d13.checkVoltStatus(volts13)
	r1a13 = d13.prepareSmoduleRequest(d13.host,11)
	currents13 = d13.getCurrents(r1a13,18183)
#Device14
	d14 = Device("S16","172.16.39.216")
	r14 = d14.prepareUmoduleRequest()
	volts14 = d14.getVolts(r14)
	status14 = d14.checkVoltStatus(volts14)
	r1a14 = d14.prepareSmoduleRequest(d14.host,11)
	currents14 = d14.getCurrents(r1a14,18183)
#Device15
	d15 = Device("S17","172.16.39.217")
	r15 = d15.prepareUmoduleRequest()
	volts15 = d15.getVolts(r15)
	status15 = d15.checkVoltStatus(volts15)
	r1a15 = d15.prepareSmoduleRequest(d15.host,13)
	currents15 = d15.getCurrents(r1a15,18203)

#Device16
	d16 = Device("S27","172.16.39.227")
	r16 = d16.prepareUmoduleRequest()
	volts16 = d16.getVolts(r16)
	status16 = d16.checkVoltStatus(volts16)
	r1a16 = d16.prepareSmoduleRequest(d16.host,11)
	currents16 = d16.getCurrents(r1a16,18183)

	#Device 17
	#d17 = Device("S29","172.16.39.229")
	#r17 = d17.prepareUmoduleRequest()
	#volts17 = d17.getVolts(r17)
	#status17 = d17.checkVoltStatus(volts17)
	#r1a17 = d17.prepareSmoduleRequest(d17.host,11)
	#currents17 = d17.getCurrents(r1a17,18183)

	#Device 18
	d18 = Device("S30","172.16.39.230")
	r18 = d18.prepareUmoduleRequest()
	volts18 = d18.getVolts(r18)
	status18 = d18.checkVoltStatus(volts18)
	r1a18 = d18.prepareSmoduleRequest(d18.host,11)
	currents18 = d18.getCurrents(r1a18,18183)


	#Device 19
	#d19 = Device("S34","172.16.39.234")
	#r19 = d19.prepareUmoduleRequest()
	#volts19 = d19.getVolts(r19)
	#status19 = d19.checkVoltStatus(volts19)
	#r1a19 = d19.prepareSmoduleRequest(d19.host,11)
	#currents19 = d19.getCurrents(r1a19,18183)

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

	#insert devices..
	socomeclist.insert(parent='',index='end',iid=1,text='',values=('1',d1.name,currents,volts[0:5], status))
	socomeclist.insert(parent='',index='end',iid=2,text='',values=('2',d2.name,currents2,volts2[0:5], status2))
	socomeclist.insert(parent='',index='end',iid=3,text='',values=('3',d3.name,currents3,volts3[0:5], status3))
	socomeclist.insert(parent='',index='end',iid=4,text='',values=('4',d4.name,currents4,volts4[0:5], status4))
	socomeclist.insert(parent='',index='end',iid=5,text='',values=('5',d5.name,currents5,volts5[0:5], status5))
	socomeclist.insert(parent='',index='end',iid=6,text='',values=('6',d6.name,currents6,volts6[0:5], status6))
	socomeclist.insert(parent='',index='end',iid=7,text='',values=('7',d7.name,currents7,volts7[0:5], status7))
	socomeclist.insert(parent='',index='end',iid=8,text='',values=('8',d8.name,currents8,volts8[0:5], status8))
	socomeclist.insert(parent='',index='end',iid=9,text='',values=('9',d9.name,currents9,volts9[0:5], status9))
	socomeclist.insert(parent='',index='end',iid=10,text='',values=('10',d10.name,currents10,volts10[0:5], status10))
	socomeclist.insert(parent='',index='end',iid=11,text='',values=('11',d11.name,currents11,volts11[0:5], status11))
	socomeclist.insert(parent='',index='end',iid=12,text='',values=('12',d12.name,currents12,volts12[0:5], status12))
	socomeclist.insert(parent='',index='end',iid=13,text='',values=('13',d13.name,currents13,volts13[0:5], status13))
	socomeclist.insert(parent='',index='end',iid=14,text='',values=('14',d14.name,currents14,volts14[0:5], status14))
	socomeclist.insert(parent='',index='end',iid=15,text='',values=('15',d15.name,currents15,volts15[0:5], status15))
	socomeclist.insert(parent='',index='end',iid=16,text='',values=('16',d16.name,currents16,volts16[0:5], status16))
	#socomeclist.insert(parent='',index='end',iid=17,text='',values=('17',d17.name,currents17,volts17[0:5], status17))
	socomeclist.insert(parent='',index='end',iid=18,text='',values=('18',d18.name,currents18,volts18[0:5], status18))
	#socomeclist.insert(parent='',index='end',iid=19,text='',values=('19',d19.name,currents19,volts19[0:5], status19))



	#add child
	socomeclist.insert(parent='',index='end',iid=31,text='',values=('31',d18.name,currents18,volts18[0:5], status18))
	socomeclist.move('31','1','1')
	socomeclist.pack()

def update_ui():
	return

exit = ttk.Button(ws, text='KAPAT', style='W.TButton', command=ws.destroy).pack(pady=10)
update_button = ttk.Button(ws,text="Guncelle", style='W.TButton', command=remove_all)
update_button.pack()


ws.resizable(False,False)
ws.mainloop()



