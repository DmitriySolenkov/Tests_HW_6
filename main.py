"""Модуль для сравнения двух списков чисел"""


def int_check(nums):
    """Функция для проверки наличия в списках не int обьектов"""
    for num in nums:
        if not isinstance(num, int):
            return False
    return True


def compare_lists(nums_1, nums_2):
    """Основная функция модуля"""
    if len(nums_1) == 0 or len(nums_2) == 0:
        return 'One of lists is empty!'
    if int_check(nums_1) is False or int_check(nums_2) is False:
        return 'One of lists contains not Integer!'
    sum_1 = 0
    sum_2 = 0
    for num in nums_1:
        sum_1 += num
    for num in nums_2:
        sum_2 += num
    average_1 = sum_1/len(nums_1)
    average_2 = sum_2/len(nums_2)
    if average_1 > average_2:
        return 'First list average is bigger!'
    if average_1 < average_2:
        return 'Second list average is bigger!'
    return 'Both lists averages are equal!'
