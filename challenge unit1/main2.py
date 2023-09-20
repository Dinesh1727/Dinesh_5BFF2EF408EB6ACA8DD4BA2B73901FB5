def LeapYear(year):
return bool(year%4==0 and year%100!=0 or year%400==0)
year=int(input("Enter a year:"))
print(Leap Year(year))
if Leap Year(year):
print("{} is Leap Year.".format(year))
else:
print("{} isNot a Leap Year.".format(year))