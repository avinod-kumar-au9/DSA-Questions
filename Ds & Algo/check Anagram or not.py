""" Question
Given two strings,check they are anagram or not.
ex : "d g","ogd"
    " vinod","noivd"
    "public relations"," latipublic reons"
"""

def Anagram(s1,s2):


    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    if len(s1)!=len(s2):
        return False

    count=dict()


    for i in s1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1

    for i in s2:
        if i in count:
            count[i]-=1
        else:
            count[i]=1

    if i in count:
        if count[i] !=0:
            return False

    return True
    

if __name__ == "__main__":
    
    s1= "public relations"
    s2=" latipublic reons"


    
    print(Anagram(s1,s2))
