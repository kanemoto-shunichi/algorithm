import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    idx = 0
    length = len(s)
    def parse():
        nonlocal idx
        counts = {chr(i): 0 for i in range(97, 123)}
        while idx < length:
            if s[idx] == ')':
                idx += 1
                break
            num = 0
            has_num = False
            while idx < length and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1
                has_num = True
            if not has_num:
                num = 1
            if idx < length and s[idx] == '(':
                idx += 1
                sub_counts = parse()

                for k, v in sub_counts.items():
                    counts[k] += v * num 
            elif idx < length and s[idx].isalpha():
                counts[s[idx]] += num
                idx += 1
        return counts
    result = parse()
    for i in range(97, 123):
        char = chr(i)
        print(f"{char} {result[char]}")

if __name__ == "__main__":
    solve()
