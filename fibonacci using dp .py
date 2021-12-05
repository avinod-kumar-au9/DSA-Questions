def fib(no,dp):   #using memoisation(recursion)-top down approach

    if no==1:
        return 0
    if no==2:
        return 1

    if dp[no] != -1:
        return dp[no]
    dp[no]=fib(no-1,dp) +   fib(no-2,dp)
    return dp[no]

def fibi(no):  # using recursion

    if no==1:
        return 0
    if no==2:
        return 1

    return fibi(no-1) +   fibi(no-2) 

def fib_tabular(no):   #using tabular form(bottow up approach)

    dp= [0] * (no + 1) 
     

    dp[1]= 0
    dp[2]= 1
    for i in range(3,no +1):
        dp[i]=dp[i-1] + dp[i-2]
    
    return dp[no]
    



no=5
dp= [-1] * (no +1)
print(fib(no,dp))
# print(fibi(no))
print(fib_tabular(no))