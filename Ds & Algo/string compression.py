"""
Question:
string compression
ex:
inp:"AAAaaa" ,out: A3a3
inp: "AABB", out: A2B2

"""

# this aproach will work even string in jigzag
sta="AA"


cnt=0
lisa=[]
straw=""
for i in range(len(sta)):
    if sta[i] not in lisa:
        # print(sta[i])
        
        for j in range(0,len(sta)):
            
                if sta[i] in sta.upper():
                    if sta[i]==sta[j]:
                        lisa.append(sta[i])
                        cnt+=1
                if sta[i] in sta.lower():
                    if sta[i]==sta[j]:
                        lisa.append(sta[i])
                        cnt+=1
                
                
        straw+=sta[i]
        straw+=str(cnt)
        
        cnt=0


print(straw)

#---------------------

# This approach doesnt work ,if string is in zigjag

r= ""
l=len(sta)

if l==0:
    print("")

if l==1:
    print(sta+"1")

last = sta[0]
cnt=1
i=1

while i<l:
    if sta[i] ==sta[i-1]:
        cnt+=1
    else:
        r= r+ sta[i-1] + str(cnt)
        cnt=1

    i+=1

r=r+sta[i-1] + str(cnt)

print(r)
