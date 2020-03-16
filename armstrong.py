str=(input("Entr any number: "))
n=int(str)

sum=0
for i in range(len(str)):
    sum+=pow(int(str[i]),len(str))

if(sum==n):
    print("The number is armstrong")

else:
    print("Is not armstrong")