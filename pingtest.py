import os
import time
import csv
from tkinter import *
from tkinter import messagebox
ws  = Tk()
file = open("hosts.csv")
csvreader = csv.reader(file)


hosts=[]
error_hosts=[]
for host in csvreader:
	hosts.append(host)

for x in range(1,20):
	response = os.system('ping -c 1 '+hosts[x][2])
	print(hosts[x][2])
	if (response == 0):
		pass
	else:
		arizali = hosts[x][1]
		error_hosts.append(arizali)
#		messagebox.showinfo("showerror", 'Substation %s a erisilemiyor.'%arizali)
#		ws.destroy()
file.close()
if(error_hosts >= 0):
	messagebox.showinfo("Substation Erisim Problemi", 'Substation %s a erisilemiyor.'%error_hosts)
	ws.destroy()
else:
	pass
#hostname = "172.16.39.200"
#response = os.system('ping -c 1 '+hostname)
#time.sleep(2)

#if (response == 0):
#	messagebox.showinfo("showinfo", "Substation Calisiyor")
#	ws.destroy()
#else:
#	messagebox.showinfo("showerror", "Substation'a erisilemiyor.")



ws.mainloop()