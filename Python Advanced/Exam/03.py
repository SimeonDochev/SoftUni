def math_operations(*args, **kwargs):
    nums = list(args)
    idx = 1
    while nums:
        current_num = nums.pop(0)
        if idx == 1:
            kwargs['a'] += current_num
        elif idx == 2:
            kwargs['s'] -= current_num
        elif idx == 3:
            if current_num == 0:
                idx += 1
                if idx == 5:
                    idx = 1
                continue
            kwargs['d'] = kwargs['d'] / current_num
        elif idx == 4:
            kwargs['m'] *= current_num
        idx += 1
        if idx == 5:
            idx = 1

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
