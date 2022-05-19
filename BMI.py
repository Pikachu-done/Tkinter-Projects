Height = float(input("Enter your Height in centimeters: "))
Weight = float(input("Enter your weight in Kg: "))
Height = Height/100
BMI = Weight/(Height*Height)
print(f"Your Body Mass Index is {BMI}")

if BMI>0:
    if BMI <= 16:
        print("You are Severly UnderWeigth.")
    elif BMI <= 18.5:
        print("You are Under Weight. ")
    elif BMI <= 25:
        print("You are Healthy.")
    elif BMI <= 30:
        print("You are Over Weigth. ")
else:
    print("Enter Valid Details.")

    