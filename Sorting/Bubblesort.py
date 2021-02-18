def Bubble_sort(List):
    # Number of elements the array has.
    Length = len(List)
    
    # Traverse through all elements
    for i in range(Length):
        # Every outer loop leaves element {i} in place
        for j in range(0, Length - i - 1):
            # If the current element is less than the next element
            if (List[j] > List[j+1]):
                # Perform the Swap
                List[j] , List[j+1] = List[j+1] , List[j]
    return List

# If no Swaps happen in the inner loop we know that the list is fully sorted.
# Thus we can optimize it 
def Bubble_sort_opt(List):
    # Number of elements the array has.
    Length = len(List)
    Swapped = False
    # Traverse through all elements
    for i in range(Length):
        # Every outer loop leaves element {i} in place
        for j in range(0, Length - i - 1):
            # If the current element is less than the next element
            if (List[j] > List[j+1]):
                # Perform the Swap
                List[j] , List[j+1] = List[j+1] , List[j]
                Swapped = True
        if not Swapped: # Check if a swap didn't happen
            break # Break the outer loop if so.
    return List


if __name__ == "__main__":
    l = [4,1,5,6,8]
    print("Before Sorting:",l)
    Bubble_sort(l)
    print("After Sorting:",l)
    
    l = [5,1,4,2,8,9,5]
    print("Before Sorting:",l)
    Bubble_sort_opt(l)
    print("After Sorting:",l)
    