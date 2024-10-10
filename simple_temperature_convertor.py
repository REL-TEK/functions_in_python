def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(temperature)
print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")