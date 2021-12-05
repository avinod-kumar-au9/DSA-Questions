
"""
question:
Find the missing integer"""


def finder(arr1,arr2):

    result=0
    for i in arr1+arr2:
        result^=i
        
    return result


if __name__ == "__main__":
    arr1=[7,2,5,3,5,3]
    arr2=[7,2,5,4,6,3,5,3]
    print(finder(arr1,arr2))