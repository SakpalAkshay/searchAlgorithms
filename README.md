# searchAlgorithms
Binary search is a search algorithm used to find the position of a target element within a sorted array. It works by repeatedly dividing the search interval in half and comparing the middle element with the target value. If the middle element is equal to the target, the search is successful. If the middle element is greater than the target, the search continues in the lower half of the interval. If the middle element is less than the target, the search continues in the upper half. This process is repeated until the target is found or the search interval becomes empty. Binary search is efficient for large datasets as it eliminates half of the remaining elements at each step, resulting in a logarithmic time complexity.

# binary search through recursion
high-level explanation of how binary search works through recursion:

Base Case: The binary search function needs a base case to stop the recursion. In this case, the base case is when the search range becomes empty (i.e., the low index becomes greater than the high index), indicating that the element is not present in the array.

Divide and Conquer: The array is divided into two halves: a left half and a right half. The middle element of the current range is calculated.

Comparison: Compare the middle element with the target element. If they are equal, the search is successful, and the middle index is returned.

Recursive Steps: If the middle element is greater than the target, the binary search function is called recursively on the left half of the range (from low to middle - 1). If the middle element is smaller than the target, the function is called recursively on the right half of the range (from middle + 1 to high).

Repeat: Steps 2-4 are repeated on the smaller subranges until the base case is reached or the target element is found.

Recursion allows the binary search algorithm to efficiently narrow down the search range by half with each recursive call, leading to a time complexity of O(log n), where n is the number of elements in the array. This is much more efficient than linear search, which has a time complexity of O(n) for a sorted array.
