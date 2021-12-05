def sol(n,coins):

    arr = [1] + [0] *n
    print(arr)

    for coin in coins:
        for i in range(coin, n+1):
            arr[i] += arr[i-coin]

    if n==0:
        return 0

    else:
        return arr[n]

print(sol(8,[1,3,5]))