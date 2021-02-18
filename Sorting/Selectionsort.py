def Selection_sort(List):
    # The Number of elements in the List
    Length = len(List)
    
    for i in range(Length): # Iterate over all elements
        min_index = i
        for j in range(i+1, Length): # Limit the range of 'j' to i+1 since the first i elements are sorted.
            if(List[j] < List[min_index]):
                min_index = j
        
        # After finding the minimum element in the unsorted half
        # Perform the swap
        List[i], List[min_index] = List[min_index] , List[i]
    
    return List # Return the sorted list




if __name__ == '__main__':
    l = [4,1,5,6,8]
    print("Before Sorting:",l)
    Selection_sort(l)
    print("After Sorting:",l)
    
    l = [5,1,4,2,8,9,5]
    print("Before Sorting:",l)
    Selection_sort(l)
    print("After Sorting:",l)
