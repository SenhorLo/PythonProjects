def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        for j in range (0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                

lista = [64,21,42,54,67,12,56,15]

bubble_sort(lista)
print("lista ordenada:", lista)