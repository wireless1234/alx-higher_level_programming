#!/usr/bin/python3
for i in range(0,99):
    if i != 89 and ((i//10) < (i % 10)):
        print(f'{i // 10}{i % 10},', end =" ")
    elif (i//10) >= (i % 10):
        continue
    else:
        print(f'{i // 10}{i % 10}')
