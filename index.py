import time
randomArrayToBeSorted=[3,45,6,8534,243,23544,56546,465,5436,45,6745,634,56,45,3,4356,43,5,5453,5674,3,34,34124,25,3,5467,7,76876,3,45,2,234,5]

def defaultSort(array):
    return sorted(array)

def timeit(function,name):
    #Check if it works
    if not defaultSort(randomArrayToBeSorted) == function(randomArrayToBeSorted):
        raise ValueError("Sort does not work")
    
    currentTime=time.time()
    for i in range(1000000):
        function(randomArrayToBeSorted)
    finish=(time.time()-currentTime)/1000000
    print(f"{name} did it in a average time of {finish} seconds")


def insertionSort(array):
    index=1
    for  index,a in enumerate(array):
        for index2,b in enumerate(array[:index]):
            if b>a:
                array[index], array[index2] = array[index2], array[index]
        index+=1
    return array

def selectionSort(array):
    for  index,a in enumerate(array):
        smallestNumber=100000000000000000000000000000
        indexOfSmallestNumber=0
        for index2,a in enumerate(array[index:]):
            if a<smallestNumber:
                smallestNumber=a
                indexOfSmallestNumber=index2
        array[index] , array[indexOfSmallestNumber] = array[indexOfSmallestNumber], array[index]
    return array
        



timeit(defaultSort,"default sort")
timeit(insertionSort,"insertion sort")