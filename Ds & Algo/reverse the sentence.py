"""Question:
reverse the sentence and remove the front and back spaces of the sentence
"""



def reverse_the_sentence(sen):
    
    return " ".join((sen).split()[::-1])  
    """ this is a single line answer for question, 
    as we dont use builtin functions.so we are doing below code
    
        OR
    """

    word=" "
    res=[]
    cnt=""
    
    final=""
    for i in sen:
        if i not in word:
            cnt+=i
        if i in word and cnt not in word:
            res.append(cnt)
            cnt=""
    if cnt not in word:
        res.append(cnt)
    
    for i in range(len(res)-1,-1,-1):
        final+=(res[i])
        final+=" "
        
    return final
    
    
 
if __name__ == "__main__":
    print(reverse_the_sentence("   how are you   "))