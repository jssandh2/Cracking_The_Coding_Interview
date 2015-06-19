# In this problem, we are given an array of unsorted numbers. Our job is to return a tulpe of indeces, such that, 
# if the array was sorted between these indices, the array would be sorted. In addition, thie distance between the indices, i.e.,
# | (right - left) | -> should be minimum. So, we need to find the smallest contiguous subarray to sort, such that the whole
# array would be sorted as a result

def find_min_dis_indices(array_numbers):
  left_break = array_numbers[0]   # Default initializations. These are the indices to return, if we have to sort the whole array
  right_break = array_numbers[len(array_numbers) - 1]
  left_index = 0
  right_index = len(array_numbers) - 1
  for i in range(len(array_numbers)/2):   # Traverse half the array, and find out where the sorting is broken on the left & right
    if i < (len(array_numbers) - i - 1):
      for j in range(2):
        if j == 0:
          if array_numbers[i] < array_numbers[i + 1]:
            left_index = i + 1
            left_break = array_numbers[i + 1]
        else:
          if i > len(array_numbers)/2:
            if array_numbers[len(array_numbers) - i - 1] < array_numbers[len(array_numbers) - i -2]:
              right_break = array_numbers[len(array_numbers) - i - 2]
              right_index = len(array_numbers) - i -2
  max_subarray = 0
  min_subarray = array_numbers[0]
  for j in range(left_index, right_index + 1):    # Find the maximum values of the unsorted component
    if array_numbers[j] > max_subarray:
      max_subarray = array_numbers[j]
  for j in range(left_index, right_index + 1):    # Find the maximum values of the unsorted component
    if array_numbers[j] < min_subarray: 
      min_subarray = array_numbers[j]
  boolean_left = True
  boolean_right = True
  index_left = 0
  index_right = len(array_numbers) - 1
  for j in range(len(array_numbers)):     # Find the indices where the minimum and maximum should be inserted, these are the indices we need
    for k in range(2):
      if k == 0:
        if min_subarray <= array_numbers[j] and boolean_left:
          boolean_left = False
          index_left = j
      else:
        if max_subarray < array_numbers[j] and boolean_right:
          boolean_right = True
          index_right = j - 1
  return (index_left, index_right)
  
# Author = Jus
    
        
