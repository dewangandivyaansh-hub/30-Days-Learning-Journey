print("choose your desired conversion \n")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius \n")

choice=int(input("Enter your choice(1/2/3/4): \n"))

temp=float(input("Enter temperature: \n"))

if choice==1:
    res=(temp*9/5)+32
    print("Temperature in Fahrenheit:",res)
elif choice==2:
    res=(temp-32)*5/9
    print("Temperature in Celsius:",res)
elif choice==3:
    res=temp=273.15
    print("Temperature in Kelvin:",res)
elif choice==4:
    res=temp-273.15
    print("Temperature in Celsius:",res)
else:
    print("\n Oops, looks like you gave an invalid choice.")
