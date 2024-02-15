income = int(input("ระบุรายได้ของคุณ: "))
if(income<70000) :
             print("คุณได้ทำบัตรเงิน")
elif(income<100000) :
             print("คุณได้ทำบัตรทอง")
else :
             print("คุณได้ทำบัตร platinum")

a = int(input("ระบุคะแนนจำเต็ม: "))
if(a>=80) :
        print("Grade A")
elif(a>=70) :
        print("Grade B")
elif(a>=60) :
        print("Grade C")
elif(a>=50) :
        print("Grade D")
else :
        print("Grade F")

username = input("Enter your username: ")
password = input("Enter your password: ")

correct_username = "admin"
correct_password = "Ad13n@23t"

if username == correct_username and password == correct_password :
    print("Welcome, admin.")
else:
    print("You are not admin.")


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
