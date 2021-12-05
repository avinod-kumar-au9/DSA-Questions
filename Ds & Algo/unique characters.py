
def uniqu(unique):
    lisa=[]

    for i in unique:
        if i in lisa:
            return False

        else:
            lisa.append(i)
    return True

print(uniqu("aabbc"))