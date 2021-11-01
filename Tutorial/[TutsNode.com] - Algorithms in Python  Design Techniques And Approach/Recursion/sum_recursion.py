"""
time complexity = O(n)
space complexity = O(n)
"""
def recursive_sum(arr):
    ## base case  is equal to the last element of the array that should only be one.
    if len(arr) == 1:
        """
        In the base case return the only element in the array.
        """
        return arr[0]
    else:
        """
        recursively add the first element of the given array to the recursive sum of the remaining array elements.
        """
        return arr[0] + recursive_sum(arr[1:])





