
def solve(arr):
    ans = 0
    for i in range(0,len(arr)):
        right_blocking_idx = -1
        left_blocking_idx = -1

        for right in range(i+1, len(arr)):
            if arr[i] < arr[right]:
                right_blocking_idx = right
                break

        for left in range(i-1, -1, -1):
            if arr[i] < arr[left]:
                left_blocking_idx = left
                break

        if left_blocking_idx == -1 or right_blocking_idx == -1:
            ans += 0
        else:
            height = min(arr[right_blocking_idx], arr[left_blocking_idx]) - arr[i]
            breadth = abs(right_blocking_idx - left_blocking_idx) - 1
            ans += height * breadth

    return ans

if __name__ == "__main__":
    print(solve([4,2,8]))

