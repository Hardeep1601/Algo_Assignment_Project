
import sys

# A utility function to get the
# maximum of two integers
def maxNum(a, b):
    return a if (a > b) else b

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces
def cutRod(price, length):
    if(length <= 0):
        return 0
    max_val = -sys.maxsize -1

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(0, length):
        hold = price[i] + cutRod(price, length - i - 1)
        max_val = maxNum(max_val, hold)
    return max_val

# Driver code
n = int(input('Enter the length of rod: '))

arr = []
for i in range(n):
    arr.append(int(input('Enter the price of a rod of length {} in: '.format(i+1))))

# arr = [3, 7, 2, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr, size))






#
#
# def cut_rod_helper(p, n, r, s):
#     q = 0
#     for i in range(1, n + 1):
#         temp = p[i] + r[n - i]
#         if q < temp:
#             q = temp
#             s[n] = i
#     return q
#
# def cut_rod(p, n):
#     r = [-1]*(n + 1)
#     s = [-1]*(n + 1)
#     r[0] = 0
#     for i in range(1, n + 1):
#         r[i] = cut_rod_helper(p, i, r, s)
#     return r, s
#
#
#
# n = int(input('Enter the length of the rod in inches: '))
#
# # p[i] is the price of a rod of length i
# # p[0] is not needed, so it is set to None
# p = [None]
# for i in range(1, n + 1):
#     price = input('Enter the price of a rod of length {} in: '.format(i))
#     p.append(int(price))
#
# r, s = cut_rod(p, n)
# print('The maximum revenue that can be obtained:', r[n])
# print('The rod needs to be cut into length(s) of ', end='')
# while n > 0:
#     print(s[n], end=' ')
#     n -= s[n]