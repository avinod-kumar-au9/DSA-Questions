def upperbound(a, x):
    left = 0
    right = len(a)
    ans=0
    if left <= right:
        for i in range(len(a)):
            mid = (left + right)//2
            if a[mid] == x:
                if mid + 1 < right and a[mid] == a[mid+1]:
                    ans = mid+1
                    left=mid+1
                else:
                    ans=mid  
                    break
            elif a[mid] > x:
                ans = mid
                right = mid-1   
            elif a[mid] < x:  
                left = mid+1     
        print(ans)

#-----------------------------

def lowerbound(a, x):
    left = 0
    right = len(a)
    ans=0
    if left <= right:
        for i in range(len(a)):
            mid = (left + right)//2
            if a[mid] == x:
                if mid - 1 < right and a[mid] == a[mid-1]:
                    ans = mid-1
                    right=mid-1
                else:
                    ans=mid  
                    break
            elif a[mid] > x:
                right = mid-1   
            elif a[mid] < x: 
                ans = mid 
                left = mid+1     
        print(ans)