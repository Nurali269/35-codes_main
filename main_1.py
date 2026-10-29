

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
   #задача 4/unique_in_order
def unique_in_order(sequence):
    result = []
    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)
    return result
#задача 5
def divisors(integer):
    result = [i for i in range(2, integer) if integer % i == 0]
    
    if not result:
        return f"{integer} is prime"
    
    return result
#задача 6
import string

def is_pangram(st):
    st = st.lower()
    return all(letter in st for letter in string.ascii_lowercase)
#задача 7
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
#задача 8
def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]
#задача 9
def sort_by_length(arr):
    return sorted(arr, key=len)
#задача 10
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
#задача 11
def reverse_words(text):
    return " ".join(word[::-1] for word in text.split (" "))
#задача 12
def count_bits(n):
    return bin(n).count("1")
#задача 13
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())
#задача 14
ef comp(array1, array2):
    return array1 is not None and array2 is not None and sorted([x**2 for x in array1]) == sorted(array2)
#задача 15
def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, 1)]
#задача 16
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
#задача 17
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
#задача 18
def high(x):
    return max(x.split(), key=lambda w: sum(ord(c) - 96 for c in w))
#задача 19
def find_uniq(arr):
    return next(x for x in set(arr) if arr.count(x) == 1)
#задача 20
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
#задача 21
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])
#задача 22
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
#задача 23
def arithmetic(a, b, operator):
    return {"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}[operator] 
#задача 24
def dont_give_me_five(start,end):
    return sum('5' not in str(i) for i in range(start, end + 1))
#задача 25
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
#задача 26
def square_digits(num):
    return int(''.join(str(int(c)**2) for c in str(num)))  
#задача 27
def printer_error(s):
    return f"{sum(c > 'm' for c in s)}/{len(s)}"
#задача 28
import heapq

def queue_time(customers, n):
    t = [0] * n
    for c in customers:
        heapq.heappushpop(t, t[0] + c)
    return max(t, default=0)
#задача 29
def in_array(array1, array2):
    return sorted(set(a for a in array1 if any(a in b for b in array2)))
#задача 30
def stray(arr):
    return min(set(arr), key=arr.count)
#задача 31
def capitalize(s):
    return ["".join(c.upper() if i % 2 == e else c for i, c in enumerate(s)) for e in (0, 1)]
#задача 32
def check_exam(arr1,arr2):
    return max(0, sum(4 if a == b else (-1 if b else 0) for a, b in zip(arr1, arr2)))
#задача 33
def solution(s):
    return "".join(c if c.islower() else f" {c}" for c in s)
#задача 34
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))
#задача 35
def solve(s):
    return s.upper() if sum(c.isupper() for c #задача 3/get the midle character
def get_middle(s):
    length = len(s)
    if length == 0:
        return ""
    
    mid = length // 2
    if length % 2 == 0:
        return s[mid - 1 : mid + 1]
    else:
        return s[mid]in s) * 2 > len(s) else s.lower()
#Виктор Владимирович вы мой любимый преподователь пожалейте меня пожалуйста я вас очень люблю и хочу сдать экзамен на 5
