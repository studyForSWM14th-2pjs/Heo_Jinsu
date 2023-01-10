def solution(numbers, target):
    global answer

    answer = 0
    find_method(numbers, target, 0, sum(numbers))
    return answer

def find_method(numbers, target, idx, total):
    global answer

    if total == target:
        answer += 1
    if idx < len(numbers) and total > target:
        # print(f'\nCurrent Index: {idx}')
        # print(f'Current Total: {total}')
        # print(f'Current Num: {numbers[idx]}')
        # print(f'-> Next Total: {total - 2*numbers[idx]}')

        find_method(numbers, target, idx+1, total-2*numbers[idx])
        find_method(numbers, target, idx+1, total)

# answer == 5
# numbers = [1,1,1,1,1]
# target = 3

# answer == 2
# numbers = [4,1,2,1]
# target = 4

# answer == 2
numbers = [5,2,4,3]
target = 4

print(solution(numbers, target))
