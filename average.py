user_input = input("Enter the number of values:")
sum=0
count=0
while user_input !='q':
    sum=sum+int(user_input)
    count+=1
    user_input=input("Enter the number of values:")

if count==0:
    print("No values entered")
else:
    print("Average:"+str(sum/count))
