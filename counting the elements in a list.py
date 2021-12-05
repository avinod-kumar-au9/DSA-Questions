T = int(input())


for j in range(0,T):
    list1=[]
    N = int(input())
    arr = list(map(int,input().split()))
    X = int(input())
    for i in arr:
        if i<=X:
            list1.append(i)

    print(len(list1))






