import ntplib
import os
from time import ctime

os.system("clear")
c = ntplib.NTPClient()
response = c.request('BTHS-LAB-DC.BTHSAcademy.local')
print("Server Time: " + ctime(response.tx_time))
newTime = response.tx_time - 23004
print("Actual Time: " + ctime(newTime) + "\n")
os.system(f"echo Date and Time Succesfully set to && sudo date --set '{ctime(newTime)}'")

