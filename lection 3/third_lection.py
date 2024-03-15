# Функции, рекурсия, алгоритмы

# создать функцию, которая будет суммировать все числа от 1 до n

# def summ_numbers(n, y = 'Hello'):
#     summa =0
#     print(y)
#     for i in range(1, n+1):
#         summa += i
#     return summa
#     print(5)

# print(summ_numbers(5, 'qwwe'))

# функция, которая принимает неограниченное количество аргументов

# def sum_str(*args):
#     res = ' '
#     for i in args:
#         res+=i
#     return res
# print(sum_str('1', 'r', 't'))
# print(sum_str('1', 'r', 't', 't'))

#               Модульность

# def max1(a,b):
#     if a > b:
#         return a
#     return b

# рекурсия 

# пользователь вводит число n, нужно вывести n первых членов последовательности Фибоначчи

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list1= []
# for i in range(1,10):
#     list1.append(fib(i))
# print(list1)
# для рекурсии обязательно указывать базис, строчки 37-38

# Алгоритмы сортировки( быстрая сортировка и сортировка слияния)
# быстрая сотрировка
# def quick_sort(array):
#     if len(array)<=1:
#         return array
#     pivot=array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less)+[pivot]+quick_sort(greater)
# print(quick_sort([1,2,3,43,424,23,34,23,1,23,43]))

# сортирвока слиянием 

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j+= 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [12,23,34,3,4,35,4,545,4,432]
merge_sort(list1)
print(list1)
