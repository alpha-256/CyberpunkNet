payRate1 = input("How much per hour do you make on job A? >>> ")
payRate2 = input("How much per hour do you make on job B? >>> ")
totalHour = input("How many hours did you work in total? >>> ")

def arrangeEquation():
    print(payRate1, "t + (", totalHour, "- t ) *", payRate2 )

arrangeEquation()
