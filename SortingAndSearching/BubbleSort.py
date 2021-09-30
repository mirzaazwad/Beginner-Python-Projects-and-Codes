#BubbleSort
array=[1, 2, 3, 2, 1, 5, 3, 6, 3, 8, 2, 9, 4]
n=len(array)-1
while True:
    NoMoreSwaps=True
    for i in range(n):
        if array[i]>array[i+1]:
            tmp=array[i]
            array[i]=array[i+1]
            array[i+1]=tmp
            NoMoreSwaps=False
    n-=1
    if NoMoreSwaps==True:
        break
