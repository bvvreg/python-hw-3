# Записуэмо в dict число з list і його індекс в list
# Перебираємо list і шукаємо чи є в dist число = різниці між сумою і елементом list
# Якщо є - виводимо list  з індексами елементів

def twoSum(nums, target):
    array = {}
    for i in range(len(nums)):
        if target - nums[i] in array:
            return [array[target - nums[i]],i]
        else:
            array[nums[i]]=i



print(twoSum([1, 2, 3], 4))        # [0, 2]
print('------')
print(twoSum([2, 7, 11, 15], 17))   # [0, 3]
print('------')
print(twoSum([3, 2, 4], 6))        # [1, 2]
print('------')
print(twoSum([3, 3], 6))           # [0, 1]
print('------')
