

# s = 'aaabca'
# a: 4, b: 1, c: 1

# s = 'aabc'
# for sym in s:
#     count = 0
#     for sub_sym in s:
#         if sub_sym == sym:
#             count+=1
#     print(sym, count)

# Итераций: 4
# O(N) = N**2


# s = 'aab'
# for sym in set(s):
#     count = 0
#     for sub_sym in s:
#         if sub_sym == sym:
#             count+=1
#     print(sym, count)

# Итераций: 6
# O(N) = M * N = N ** 2

s = 'aab'
syms_counter = {}
for sym in s:
    syms_counter[sym] = syms_counter.get(sym, 0) + 1

print(syms_counter)

# Итераций: 3
# O(N) = N














# print(set('aaaaaabccc'))

