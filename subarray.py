def max_subarray_sum(arr):
    
    max_so_far = float('-inf')
    max_ending_here = 0

    # Traverse through the array
    for num in arr:
        max_ending_here += num
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

# Get input from the user
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("Maximum subarray sum is", max_subarray_sum(arr))
