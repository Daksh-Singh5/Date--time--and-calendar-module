import datetime

days =int(input("Enter the number of days you were in vecation:  "))
Place= input("Place did you go \n1.Spain\n2.India\n3.USA\n4.UK \n")
Car= input("Car car you used \n1.BMW\n2.Honda\n")


hotelCost=0
CarCost=0
planeCost=0


Place=Place.lower()
Car=Car.lower()


if Place == "spain":
    planeCost=300
elif Place == "india":
    planeCost=700
elif Place == "usa":
    planeCost=200
elif Place == "uk":
    planeCost=100

if days >40:
    hotelCost = 40*200-100
    CarCost = 40*300-100
elif days >30:
    hotelCost = 40*200-75
    CarCost = 40*300-70
elif days >20:
    hotelCost = 40*200-50
    CarCost = 40*300-45
elif days >10:
    hotelCost = 40*200-10
    CarCost = 40*300-20
else:
    hotelCost = 40*200
    CarCost = 40*300

if Car=="bmw":
    CarCost+=CarCost/50
elif Car=="honda":
    CarCost+=CarCost/20

print(CarCost)
print(planeCost)
print(hotelCost)

def bill(days,flight,carprice,place,hotel):
    print("===================================================================================")
    print("                                TRAVELING BILL                                     ")
    print("===================================================================================")
    print("Date        :",datetime.datetime.now().strftime("%B %d, %Y"))
    print("Duration    :",days)
    print("Destination :",place)
    print("___________________________________________________________________________________")
    print("Car Ride Cost   :",carprice)
    print("Plane Ride Cost",flight)
    print("hotel Ride Cost",hotel)
    print("___________________________________________________________________________________")
bill(days,planeCost,CarCost,Place,hotelCost)