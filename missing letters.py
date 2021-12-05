def removeDuplicates( nums,nums1) :
    lisa=sorted(list(set()))
    for i in nums1:
        if i in nums:
            nums.remove(i)
        else:
            lisa.append(i)

    return lisa

print(removeDuplicates([1,2,3],[1,1,1,1,2,3,4]))