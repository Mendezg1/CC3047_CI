def media(nums):
    if not nums:
        raise ValueError("La lista no puede estar vacía")
    return sum(nums) / len(nums)