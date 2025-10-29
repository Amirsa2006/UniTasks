year=int(input("Please Enter your birthdate:"))
current_year=2025
age=current_year-year
hoursOfLife=age*365*24
minutesOfLife=age*365*24*60
secondsOfLife=age*365*24*60*60
print(f"Your age to hour:{hoursOfLife}")
print(f"Your age to minute:{minutesOfLife}")
print(f"Your age to hour:{secondsOfLife}")


# خواندن عدد دو رقمی از کاربر
number = input("Please enter a number")

# بررسی اینکه آیا عدد دو رقمی است
if len(number) == 2 and number.isdigit():
    # استخراج رقم اول و دوم
    digit1 = int(number[0])
    digit2 = int(number[1])
    
    # محاسبه توان‌ها
    result1 = digit1 ** digit2
    result2 = digit2 ** digit1
    
    # نمایش نتایج
    print(f"{digit1} B Tavaneh {digit2} is equal to: {result1}")
    print(f"{digit2} B Tavaneh {digit1} is equal to: {result2}")
else:
    print("Please enter a vaild number")


