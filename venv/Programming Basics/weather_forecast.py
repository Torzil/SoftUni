import requests
print("------------------- Welcome to the Simple Weather Forecast app! -------------------")
print("Input the name of the city you want to see the weather forecast for and hit 'Enter'!\n")
city_name = input("Enter the name of the city: ")

print("\n\n")

url = f"https://wttr.in/{city_name}"

try:
    data = requests.get(url)
    result = data.text
except:
    result = "Error Occurred"

print(result)
