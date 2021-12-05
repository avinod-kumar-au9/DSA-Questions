
# string=[6, 2, 5, 2, 2,6, 6]
# d={}
# [x for x in string]
# =dict.get(d,0)+1

arr=[4,4,2,5,6,6,6]
r={}
for i in arr:
    r[i]=arr.count(i)

print(r)


temp = min(r.values()) 
res = [i for i in r if r[i] == temp]
print(res)
print(temp)

 
