

# nums=[1,2,3,1]

# l=0
# r = len(nums)-1
def ret(nums):
        l= 0
        r = (len(nums))-1
        while l <= r:
                mid=(l+r)//2

                if mid==0:
                        if mid+1 < len(nums) and nums[mid]>nums[mid+1]:
                                return mid
                        else:
                                l=mid+1

                elif mid == (len(nums))-1:
                        if mid - 1 < len(nums) and nums[mid]> nums[mid-1]:
                                return mid
                        else:
                                r=mid-1
                elif mid -1 >=0 and mid+1<len(nums) and nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                        return mid
                elif mid+1 < len(nums) and nums[mid] < nums[mid-1]:
                        l=mid+1
                elif mid-1 >=0 and nums[mid] < nums[mid-1]:
                        r=mid-1
        return -1

if __name__=='__main__':
        
        nums=[1,2,3,1]
        
        

        print(ret(nums))