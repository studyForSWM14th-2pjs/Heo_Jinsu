zero_nums = [-1 for _ in range(41)]
one_nums = [-1 for _ in range(41)]

# T: The number of test case
T: int = int(input())

# N: Input number
for _ in range(T):
    N= int(input())
    
    idx = 0

    if zero_nums[N] < 0:
        while idx <= N:
            if idx == 0 and zero_nums[idx] < 0:
                zero_nums[idx] = 1
                one_nums[idx] = 0
            elif idx == 1 and one_nums[idx] < 0:
                zero_nums[idx] = 0
                one_nums[idx] = 1
            else:
                if zero_nums[idx] < 0:
                    zero_nums[idx] = zero_nums[idx-1] + zero_nums[idx-2]
                    one_nums[idx] = one_nums[idx-1] + one_nums[idx-2]
            idx += 1

    print(zero_nums[N], one_nums[N])