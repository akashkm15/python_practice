# kilometers to miles

def kilo_to_miles(km):
    print(f"{km}km converted into {km/1.609}miles")
def miles_to_kilo(miles):
    print(f"{miles}mile converted into {miles1 * 1.609}miles")

option=int(input("chooose the option\n1.kilometers to miles\n2.miles to kilometers\n"))

if option==1:
    kilo=float(input("Enter the value in kilometers: "))
    kilo_to_miles(kilo)
elif option==2:
    mile = float(input("Enter the value in miles: "))
    miles_to_kilo(mile)
else:
    print("Enter the valid option(1 or 2)")