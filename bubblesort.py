def main():
    # create a list of numbers
    # numberList = [4,1,3,9,2,6,5,8]

    numberList = list(map(int, input("Enter the numbers to be sorted, separated by spaces: ").split()))

    input("Press Enter to sort the list using bubble sort...")

    print("Original list:", numberList)
    
    # call the bubble sort function
    bubble_sort(numberList)

    print("Sorted list:", numberList)

def bubble_sort(nlist):
    # get the length of the list
    l=len(nlist)
    for i in range (l-1):
        swapped = False
        for j in range(l-1-i):
            if nlist[j] > nlist[j+1]:
                # swap the elements
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        if not swapped:
            break

main()
