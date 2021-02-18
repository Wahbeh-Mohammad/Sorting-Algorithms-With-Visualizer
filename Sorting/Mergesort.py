def Merge_Sort(List):
    Length = len(List)
    if Length > 1:
        # Finding the midpoint
        Mid = Length//2
        
        # Dividing the list into two sub lists
        L = List[:Mid]
        R = List[Mid:]
    
        # Recursivly call Merge_Sort to divide each
        # Sub-list
        Merge_Sort(L)
        Merge_Sort(R)
        
        i = j = k = 0
        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                List[k] = L[i]
                i += 1
            else:
                List[k] = R[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(L):
            List[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            List[k] = R[j]
            j += 1
            k += 1
        
        return List

if __name__ == '__main__':
    l = [4,1,5,6,8]
    print("Before Sorting:",l)
    print("After Sorting:",Merge_Sort(l))