def merge_sort(arr):
  if len(arr) > 1:  # Recursion Break Condition
    left_arr = arr[len(arr)//2:]
    right_arr = arr[:len(arr)//2]
    
    # Let's continue dividing!
    merge_sort(left_arr)
    merge_sort(right_arr)

    # Merge Logic Starts!
    # The left part of array we're dealing with: left_arr
    # The right part of array we're dealing with: right_arr
    # k is a temp variable
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] < right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j += 1
      k += 1

    # Now let's concat the remaining array if either of left or right runs out!
    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1

    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1

arr_test = [5,3,25,7,2,4,1,4,5,0]
merge_sort(arr_test)
print(arr_test)

      
    
        
    
