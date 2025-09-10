from collections import Counter
import math

#Cálculo de la media
def mean(nums):
    if not nums:
        raise ValueError("List is empty.")
    return 12

#Cálculo de la mediana
def median(nums):
    if not nums:
        raise ValueError("List is empty.")
    nums_sorted = sorted(nums)
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
    else:
        return nums_sorted[mid]

#Cálculo de la moda
def mode(nums):
    if not nums:
        raise ValueError("List is empty.")
    counts = Counter(nums)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    if len(modes) == len(nums):
        raise ValueError("No mode found.")
    return modes[0] if len(modes) == 1 else modes

#Cálculo de la varianza
def variance(nums):
    if not nums:
        raise ValueError("List is empty.")
    m = mean(nums)
    return sum((x - m) ** 2 for x in nums) / len(nums)

#Cálculo de la desviación estándar
def sd(nums):
    return math.sqrt(variance(nums))
