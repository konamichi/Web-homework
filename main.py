# the first
def palindrom(n):
    n_list = [int(a) for a in str(n)]
    return n_list == list(reversed(n_list))


print(palindrom(46327))
print(palindrom(1991))


# the second
def lists(nums):
    div_2 = [num for num in nums if num % 2 == 0]
    div_3 = [num for num in nums if num % 3 == 0]
    div_5 = [num for num in nums if num % 5 == 0]
    return div_2, div_3, div_5


num_lst = [346, 111, 190, 9, 45, 920, 333]
div_2, div_3, div_5 = lists(num_lst)

print('Делятся на 2: ' + str(div_2))
print('Делятся на 3: ' + str(div_3))
print('Делятся на 5: ' + str(div_5))


# the third
def reverse(n):
    n_str = [a for a in str(n)]
    n_str.reverse()
    if n < 0:
        n_str.insert(0, n_str.pop())
    return int(''.join(n_str))


print(reverse(1394))
print(reverse(-9991))


# the fourth
def newton(num, e=0.001):
    el = float(num)
    prev_x = num

    while True:
        new_x = 0.5 * (prev_x + el / prev_x)
        if abs(new_x - prev_x) < e:
            break
        prev_x = new_x
    return new_x


print(newton(847))
print(newton(109))


def is_prime(num):
    if num % 2 == 0:
        return num == 2
    x = 3
    while x * x <= num and num % x != 0:
        x += 2
    return x * x > num


print(is_prime(int(input("Enter a number: "))))
