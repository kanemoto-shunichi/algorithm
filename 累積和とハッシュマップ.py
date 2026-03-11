def solution(A, S):
    left = 0
    right = 0
    count = 0
    while True:
        if left == right and A[left] == S:
            left += 1
            right += 1
            count += 1
        else:
            right += 1
            if sum(A[left:right]) > S:
                left += 1
            elif sum(A[left:right]) < S:
                right += 1
            else:
                count += 1
                right += 1
        if right == len(A):
            break
    print(count)

def solution(A, S):
    prefix_counts = {0: 1}
    curr_sum = 0
    count = 0
    for num in A:
        curr_sum += num
        target = curr_sum - S
        if target in prefix_counts:
            count += prefix_counts[target]
        if curr_sum in prefix_counts:
            prefix_counts[curr_sum] += 1
        else:
            prefix_counts[curr_sum] = 1
    return count
    



