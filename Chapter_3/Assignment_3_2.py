#Alter assignment_3_1 to include a try and except clause to handle bad inputs
Hrs = input("Enter Hours:")
Rate = input("Enter Rate:")
try:
    Hrs_float = float(Hrs)
    Rate_Float= float(Rate)
except:
    print("Error, please enter numeric input")
    quit()
HRS_overtime = Hrs_float-40
if Hrs_float<=40:
    Pay = Hrs_float*Rate_Float
elif Hrs_float>40:
    Pay = (40*Rate_Float)+(HRS_overtime*Rate_Float*1.5)
else:
    print("weird number")
    Pay_string = str(Pay)
    print("Pay: "+Pay_string)
