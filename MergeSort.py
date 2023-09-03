def merge_sort(nums): 
    if len(nums) > 1: 
        mid = len(nums)//2
        left = nums[:mid] 
        right = nums[mid:]
        merge_sort(left) 
        merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i+=1
            else: 
                nums[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            nums[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            nums[k] = right[j] 
            j+=1
            k+=1
    return nums        
            
def GetInts():
    entered_list = input("Введите список чисел, разделенных пробелом: ").split()
    num_list = [int(i) for i in entered_list]
    print("Список чисел: ", num_list)
    return num_list
            
print(f"Отсортированный список: {merge_sort(GetInts())}")