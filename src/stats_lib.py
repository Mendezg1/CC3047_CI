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
    
    