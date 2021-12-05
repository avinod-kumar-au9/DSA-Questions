
n = int(input("Enter"))

choice=int(input("select 1 for to add and 2 for product"))
def sum1(n):
    sum=0
    
    for i in range(1,n+1):
        sum += i
    return sum
def product1(n):
    product=1
    for j in range(1,n+1):
        product =product * j
    return product

if (choice == 1):
    print(sum1(n))
elif (choice==2):
    print(product1(n))

