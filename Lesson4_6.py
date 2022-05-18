from itertools import cycle, count

s_start = int(input('Start number: '))
s_stop = s_start * 2 + 10 + 1

# s.1
for i in count(s_start):
    if i < s_stop:
        print(i)
    else:
        break
del i

# s.2
my_list = [i for i in range(s_stop)]
count = 0
for b in cycle(my_list):
    if count < s_stop + 10:
        print(b)
        count += 1
    else:
        break