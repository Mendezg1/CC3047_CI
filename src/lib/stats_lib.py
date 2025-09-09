from collections import Counter
import math


def mean(nums):
    if not nums:
        raise ValueError("List is empty.")
    return sum(nums) / len(nums)

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
    
def mode(nums):
    if not nums:
        raise ValueError("List is empty.")
    counts = Counter(nums)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    if len(modes) == len(nums):
        raise ValueError("No mode found.")
    return modes[0] if len(modes) == 1 else modes
    
def variance(nums):
    if not nums:
        raise ValueError("List is empty.")
    m = mean(nums)
    return sum((x - m) ** 2 for x in nums) / len(nums)

def sd(nums):
    return math.sqrt(variance(nums))