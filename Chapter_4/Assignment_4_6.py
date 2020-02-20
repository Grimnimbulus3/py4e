#rewrites the Pay script to be a function
#Hrs = input("Enter Hours:")
#Rate = input("Enter Rate:")
def computepay(hours, rate):
    try:
        Hrs_float = float(hours)
        Rate_Float= float(rate)
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
    Pay_output = "Pay: "+Pay_string
    return Pay_output

Pay_output=computepay(45, 10)
print(Pay_output)
