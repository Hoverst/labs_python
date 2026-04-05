def monotony_check(nums):

    if len(nums) <= 2:
        return True
        
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            is_increasing = False
            
        if nums[i] > nums[i-1]:
            is_decreasing = False
            
        if is_increasing == False and is_decreasing == False:
            return False
    
    return True

