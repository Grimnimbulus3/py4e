#converts celsius input into Fahrenheit output
Celsius_temp=input("Enter a temperature in Celsius:")
Celsius_temp_int = int(Celsius_temp)
Fahrenheit_temp = (Celsius_temp_int*1.8)+32
Fahrenheit_temp_str = str(Fahrenheit_temp)
print(Celsius_temp+" degrees Celsius is equal to "+Fahrenheit_temp_str+" degrees Fahrenheit")
