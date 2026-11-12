print("Python program to calculate the total mobile data used by a student in one day")
brdata =(int(input("Enter the browsing data: ")))
vstrdata =(int(input("Enter the vedio streaming data: ")))
clsdata  =(int(input("Enter the vedio streaming data: ")))

Total =(brdata+vstrdata+clsdata)
print("Total data used: ",Total)

rem =(2000-Total)
print("Remaining data : ",rem)
