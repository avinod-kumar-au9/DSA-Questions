class Heap:
    def __init__(self,arr):
        self.arr=arr


def delete_element():
    max_ele= arr[0]

    arr[0], arr[len(arr)-1]=arr[len(arr)-1],arr[0]
    arr.pop()
    heapify(0)
    return max_ele


def heapify(idx):
    
    left =2 *idx +1
    right=2 *idx +2
    max_idx=idx


    if left <=len(arr)-1 and arr[max_idx] > arr[left]:
        max_idx=left
    
    if right <=len(arr)-1 and arr[max_idx] > arr[right]:
        max_idx=right

    if max_idx != idx:
        arr[max_idx],arr[idx]=arr[idx],arr[max_idx]
        heapify(max_idx)

def build_heapify():

    start_idx= (len(arr)//2)-1

    for idx in range(len(arr),-1,-1):
        heapify(idx)
    print("min heap is",arr)

def heap_sort():

    for i in range(len(arr)):
        print("heap_sorting",delete_element())


if __name__ == "__main__":
    
    arr=[4,7,2,1,6]

    build_heapify()

    heap_sort()
