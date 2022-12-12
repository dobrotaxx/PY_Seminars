# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N. 

users_N = int(input('Введите число: '))

nums_from_0_to_N = [i for i in range(0, users_N + 1)]
nums_from_0_to_N[1] = 0
smpl_nums = []
i = 2
while i <= users_N:
    if nums_from_0_to_N[i] != 0:
        smpl_nums.append(nums_from_0_to_N[i])
        for j in range(i, users_N + 1, i):
            nums_from_0_to_N[j] = 0
    i += 1

result = []
i = 0
while i != len(smpl_nums):
    if users_N % smpl_nums[i] == 0:
        users_N /= smpl_nums[i]
        smpl_mult = smpl_nums[i]
        result.append(smpl_mult)
    else:
        i += 1

print(result)
