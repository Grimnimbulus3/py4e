#Alters Assignment 2_3 to add in overtime
Hrs = input("Enter Hours:")
Rate = input("Enter Rate:")
Hrs_float = float(Hrs)
Rate_Float= float(Rate)
HRS_overtime = Hrs_float-40
if Hrs_float<=40:
    Pay = Hrs_float*Rate_Float
elif Hrs_float>40:
    Pay = (40*Rate_Float)+(HRS_overtime*Rate_Float*1.5)
else:
    print("weird number")
Pay_string = str(Pay)
print("Pay: "+Pay_string)
