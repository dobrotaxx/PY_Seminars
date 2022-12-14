#2. В файле дана строка с данными 2 3 5 6 7. Добавить недостающий элемент в файл.
# 2 3 5 6 7 -> 2 3 4 5 6 7
with open('For_task02.txt', 'r') as data:
    nums = list(map(int, data.read().split()))
print(nums)

for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] > 1:
        nums.insert(i, nums[i - 1] + 1)
print(nums)

with open('For_task02.txt', 'w') as data:
    data.write(' '.join(list(map(str, nums))))
