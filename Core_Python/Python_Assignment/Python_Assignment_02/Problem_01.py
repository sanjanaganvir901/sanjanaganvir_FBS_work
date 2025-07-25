# Time entered in hh,mm,sec into seconds

h = int(input("Enter a Hrs :"))
m = int(input("Enter a min :"))
s = int(input("Enter a sec :"))

seconds = h * 3600 + m * 60 + s
print("The time entered seconds is :",seconds)