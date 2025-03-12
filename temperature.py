""" employees_temperature = {
    "E001": 36.5,
    "E002": 36.7,
    "E003": 36.6,
    "E004": 36.8,
    "E005": 36.9,
    "E006": 37.0,
    "E007": 36.4,
    "E008": 36.5,
    "E009": 36.6,
    "E010": 36.7,
    "E011": 36.8,
    "E012": 36.9,
    "E013": 38.0,
    "E014": 36.4,
    "E015": 36.5,
    "E016": 36.6,
    "E017": 36.7,
    "E018": 36.8,
    "E019": 36.9,
    "E020": 37.0
}
for id,temp in employees_temperature.items():
    if temp>=37.5:
        print ("Employee ID:",id," has a fever.")


 """
sum=0
value1=int(input("Enter the first value:"))
for i in range(1,value1+1):
    sum+=i
print("The sum of the first",value1,"numbers is:",sum)
