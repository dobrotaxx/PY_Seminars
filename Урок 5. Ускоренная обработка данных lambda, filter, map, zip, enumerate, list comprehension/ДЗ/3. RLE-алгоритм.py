# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import re

users_string = input('Введите строку для кодирования: ')


def Encode(decoded_string):
    encoded_string = ''
    char = decoded_string[0]
    i = 1
    while True:
        chars = ''
        if char == decoded_string[i]:
            while i < len(decoded_string) and decoded_string[i] == decoded_string[i - 1]:
                chars = chars + char
                char = decoded_string[i]
                i += 1
            if i == len(decoded_string):
                if decoded_string[i - 1] == decoded_string[i - 2]:
                    encoded_string = encoded_string + str(len(chars) + 1) + decoded_string[i - 1]
                break
            else:
                if decoded_string[i - 1] == decoded_string[i - 2]:
                    encoded_string = encoded_string + str(len(chars) + 1) + decoded_string[i - 1]

        else:
            chars = ''
            while i < len(decoded_string) and decoded_string[i] != decoded_string[i - 1]:
                if i == 1:
                    chars = chars + char
                char = decoded_string[i]
                chars = chars + char
                i += 1
            if i == len(decoded_string):
                if decoded_string[i - 1] != decoded_string[i - 2]:
                    encoded_string = encoded_string + str(len(chars) + 128) + chars
                break
            else:
                if decoded_string[i - 1] != decoded_string[i - 2] and decoded_string[i - 2] != decoded_string[i - 3]:
                    chars = chars[:-1]
                    encoded_string = encoded_string + str(len(chars) + 128) + chars

    return encoded_string


def Decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    nums = re.findall(r'\d+', encoded_string)
    j = 0
    i = 0
    while i < len(encoded_string):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
            i += 1
        else:
            if int(nums[j]) > 128:
                nums[j] = int(nums[j]) - 128
                while int(nums[j]) > 0:
                    decoded_string += encoded_string[i]
                    i += 1
                    nums[j] = int(nums[j]) - 1
                i += 1
                if j == len(nums) - 1:
                    j = j
                else:
                    j += 1
            else:
                while int(nums[j]) > 0:
                    decoded_string += encoded_string[i]
                    nums[j] = int(nums[j]) - 1
                i += 1
                if j == len(nums) - 1:
                    j = j
                else:
                    j += 1
    print(decoded_string)
    return decoded_string


print(Encode(users_string))
Decode(Encode(users_string))
