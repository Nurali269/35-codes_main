

def high_and_low(numbers):
    nums = [int(x)for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"
    #задача 2
    def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *=int(digit)
            n = product
            count += 1
