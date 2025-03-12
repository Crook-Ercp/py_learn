def calculate_bmi(weight, height):
    bmi= weight/(height**2)
    if bmi<18.5:
        return "Underweight"
    elif bmi>=18.5 and bmi<24.9:
        return "Normal"
    elif bmi>=25 and bmi<29.9:
        return "Overweight"
    else:
        return "Obese"
    return bmi

d1=calculate_bmi(10,1.6)
d2=calculate_bmi(70,1.7)
print(d1)
print(d2)