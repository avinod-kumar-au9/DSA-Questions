lisa=[1,5,2,3]
#subsets are
# 12,13
# 1,5
# 4,7,8,10
# 10,11

lil=[]
count=1
for i in range(0,len(lisa)):
    for j in range(i+1,i+2):
        if j<len(lisa):
        
            if lisa[i]<lisa[j]:
                count+=1
            if j==len(lisa)-1:
                lil.append(count)
                
            if lisa[i]>=lisa[j]:
                lil.append(count)
                count=1

print(max(lil))





