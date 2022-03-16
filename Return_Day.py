start_day = int(input("please enter your starting day number "))
stay =int(input("How long will your stay be "))
stay= stay % 7
rem = start_day + stay

if rem==0:
    print("Monday")
elif rem==1:
    print("Tuesday")
elif rem==2:
    print("Wednesday")
elif rem==3:
    print("Thursday")
elif rem==4:
    print("Friday")
elif rem==5:
    print("saturday")
elif rem==6:
    print("Sunday")
else:
    print("The input is invalid or out of Range")
