def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1
    
    while j <= k:
        # per cada 0 l'envia al principi de la llista i modifica i per no mourel's
        if nums[j] < pivot:
            swap(nums, i, j)
            i = i + 1
            j = j + 1
        # per cada 2, l'envia al final de la llista i modifica i per no mourel's
        elif nums[j] > pivot:
            swap(nums, j, k)
            k = k - 1
        # si es 1, modifica j per a evaluar la seguent
        else:
            j = j + 1 
    return nums       
            
def swap(nums, index1, index2):
    #intercambia de posició
    nums[index1], nums[index2] = nums[index2], nums[index1]
            
if __name__ == '__main__':
    print(dutch_flag_problem([0,1,2,2,1,0,0,2,2,1]))