import time

array = [219, 231, 283, 90, 134, 213, 254, 61, 281, 136, 45, 29, 108, 235, 
        263, 220, 115, 98, 175, 73, 267, 209, 131, 130, 38, 50, 31, 60, 104, 
        243, 89, 47, 62, 156, 13, 42, 186, 248, 201, 44, 54, 117, 211, 210, 
        23, 118, 93, 247, 282, 264, 30, 85, 207, 295, 84, 182, 11, 111, 176, 
        272, 257, 260, 280, 48, 234, 292, 265, 225, 88, 171, 56, 294, 140, 
        183, 75, 133, 22, 112, 148, 258, 287, 262, 59, 228, 215, 253, 139, 
        162, 58, 181, 230, 72, 236, 49, 293, 240, 268, 15, 110, 34, 159, 249, 
        103, 70, 120, 166, 242, 122, 185, 212, 151, 64, 273, 289, 291, 227, 
        244, 99, 232, 82, 241, 296, 97, 91, 1, 87, 106, 189, 77, 223, 154, 
        216, 114, 203, 67, 100, 25, 173, 199, 168, 266, 74, 218, 277, 19, 
        107, 128, 270, 76, 26, 6, 239, 188, 20, 123, 246, 51, 214, 135, 261, 
        163, 102, 143, 129, 4, 221, 7, 196, 65, 39, 299, 204, 79, 256, 124, 
        27, 286, 157, 147, 57, 178, 78, 52, 233, 68, 105, 170, 208, 206, 83, 
        298, 69, 238, 36, 229, 284, 200, 121, 224, 288]

# 1. BUBBLE SORT
# This algorithm works by repeatedly swapping the adjacent elements 
# if they are in wrong order.
# Read more: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(arr0): 
    t1 = time.time()
    n = len(arr0) 

    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more 
    # than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr0[j] > arr0[j+1] : 
                arr0[j], arr0[j+1] = arr0[j+1], arr0[j]
    
    t2 = round(time.time() - t1, 6)
    print("Result: {0}\n Time used: {1}".format(arr0, t2), end="\n")


# 2. QUICK SORT
# This algorithm picks an element as pivot and partitions the given array 
# around the picked pivot.
# Read more: https://www.geeksforgeeks.org/python-program-for-quicksort/
def quick_sort(arr1):
    done = False

    # This function takes last element as pivot, places the pivot element 
    # at its correct position in sorted array, and places all smaller 
    # (smaller than pivot) to left of pivot and all greater elements to 
    # right of pivot.
    def _partition(arr1,low,high): 
        i = (low-1)         # index of smaller element 
        pivot = arr1[high]  # pivot 
    
        for j in range(low , high): 
    
            # If current element is smaller than or 
            # equal to pivot 
            if   arr1[j] <= pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr1[i],arr1[j] = arr1[j],arr1[i] 
    
        arr1[i+1],arr1[high] = arr1[high],arr1[i+1] 
        return ( i+1 )

    # low  --> Starting index, 
    # high  --> Ending index
    def _sort(arr1,low,high): 
        if low < high: 

            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = _partition(arr1,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            _sort(arr1, low, pi-1) 
            _sort(arr1, pi+1, high)
    
    t1 = time.time()
    if not done:
        n = len(arr1) 
        _sort(arr1,0,n-1)
        done = True

    t2 = round(time.time() - t1, 6)
    print("Result: {0}\n Time used: {1}".format(arr1, t2), end="\n")


# 3. MERGE SORT
# This algorithm divides input array in two halves, calls itself for the 
# two halves and then merges the two sorted halves.
# Read more: https://www.geeksforgeeks.org/merge-sort/
def merge_sort(arr2):
    done = False

    def _sort(arr2): 
        if len(arr2) >1: 
            mid = len(arr2)//2   # Finding the mid of the array 
            L = arr2[:mid]       # Dividing the array elements  
            R = arr2[mid:]       # into 2 halves 
    
            _sort(L) # Sorting the first half 
            _sort(R) # Sorting the second half 
    
            i = j = k = 0
            
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr2[k] = L[i] 
                    i+=1
                else: 
                    arr2[k] = R[j] 
                    j+=1
                k+=1
            
            # Checking if any element was left 
            while i < len(L): 
                arr2[k] = L[i] 
                i+=1
                k+=1
            
            while j < len(R): 
                arr2[k] = R[j] 
                j+=1
                k+=1
    
    t1 = time.time()
    if not done:
        _sort(arr2)
        done = True

    t2 = round(time.time() - t1, 6)
    print("Result: {0}\n Time used: {1}".format(arr2, t2), end="\n")



def main():
    print("Original Array: {0}".format(array), end="\n")
    print("\n[A. Bubble Sort]")
    bubble_sort(array)
    print("\n[B. Quick Sort]")
    quick_sort(array)
    print("\n[C. Merge Sort]")
    merge_sort(array)

if __name__ == "__main__":
    main()