n=11
count = [0]*6
list=[1,2,3,3,4,4,4,5]
for t in list:
    count[t] += 1
print(count.index(max(count)))
print(count)



# def migratoryBirds(arr):
#     l = [arr.count(i) for i in range(1, 6)]
#     print(l)
#     for i in range(len(l)):
#         if l[i]==max(l):
#             return i+1