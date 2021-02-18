def Insertion_sort(List):
    # The number of elements in the List
    Length = len(List)
    
    for i in range(1,Length): # Iterate over elements from 1..Length
        
        Current_element = List[i]
        j = i-1
        
        # Now move all elements before the current element to one position forward in the List
        while( j >= 0 and List[j] > Current_element):
            List[j + 1] = List[j]
            j -= 1
        
        # After moving all elements that are greater than the current element
        # Place the current element before them.
        List[j + 1] = Current_element
        
    return l

if __name__ == '__main__':
    l = [4,1,5,6,8]
    print("Before Sorting:",l)
    print("After Sorting:",Insertion_sort(l))
    l = [5,1,4,2,8,9,5]
    print("Before Sorting:",l)
    print("After Sorting:",Insertion_sort(l))
