'''F-Fahrenheit
   K-Celsius
   C-Kelvin'''
choice = input("")
num = float(input(""))
kelvin = ''
celsius = ''
fahrenheit = ''
def f_k_c(choice):
    if choice == 'F':
        kelvin = (num + 459.67) * 5/9
        celsius = (num - 32) * 5/9
        return "Celsius is: " + str(celsius) + " , Kelvin is: " + str(kelvin)
    elif choice == 'C':
        kelvin = num + 273.15
        fahrenheit = (num * 9/5) + 32
        return "Fahrenheit is: " + str(fahrenheit) + " , Kelvin is: " + str(kelvin)

result = f_k_c(choice)
print(result)
