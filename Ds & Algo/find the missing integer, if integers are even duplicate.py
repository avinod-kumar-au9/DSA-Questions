arr=[203, 204, 205, 206, 207, 208, 203, 204, 205, 206]

brr=[203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]


m = max(arr + brr) + 1
list = [0 for _ in range(m)]
for i in arr:
    list[i] += 1
for i in brr:
    list[i] -= 1
print(sorted([item for item in range(len(list)) if list[item] != 0]))