def miniMaxSum(arr):
    total = sum(arr)
    # 全体から最大値を引いたものが最小の合計、最小値を引いたものが最大の合計
    print(total - max(arr), total - min(arr))

#　セット
def pairs(k, arr):
    # 配列をセットに変換（検索を爆速にするため！）
    num_set = set(arr)
    count = 0
    
    # ループは1重だけでOK！
    for x in arr:
        # x + k という数字がセットの中に存在するかどうかを一瞬で判定
        if (x + k) in num_set:
            count += 1
    return count

#　スタック
def isBalanced(s):
    # あなたが言った「閉じ括弧リスト」を用意
    expected_brackets = []
    
    # 開き括弧が来たときに、どの閉じ括弧を予測するかという辞書（ルールブック）
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        # 1. もし文字が「開き括弧」だったら
        if char in pairs:
            # そのペアの「閉じ括弧」をリストの一番最後に追加する（append）
            expected_brackets.append(pairs[char])
            
        # 2. 開き括弧ではない（＝閉じ括弧である）場合
        else:
            # もし「リストが空（比較対象がない）」または「リストの一番最後と違う文字」なら NO
            # （※ Pythonでリストの一番最後は [-1] で取得できます）
            if not expected_brackets or char != expected_brackets[-1]:
                return "NO"
            
            # 一致した場合は、その「閉じ括弧」は無事にペアが成立したので、
            # リストの一番最後から取り出して消す（pop）
            expected_brackets.pop()
            
    # 3. 最後に閉じ括弧リストが空になっていないと NO、空なら YES
    if len(expected_brackets) == 0:
        return "YES"
    else:
        return "NO"
    
#　しゃくとり法（ポインタ）
def minSubArrayLen(target, arr):
    min_len = float('inf')
    current_sum = 0
    left = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum >= target:
            current_length = right - left + 1
            if current_length < min_len:
                min_len = current_length
            current_sum -= arr[left]
            left += 1
    if min_len == float('inf'):
        return 0
    else:
        return min_len

#　カダネのアルゴリズム
def maxSubArray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        num = arr[i]
        current_sum = max(num, current_sum + num)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
def maxSubArrayElements(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    start = 0     
    end = 0       
    temp_start = 0  
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i 
        else:
            current_sum = current_sum + arr[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return arr[start : end + 1]

#　辞書操作
def groupAnagrams(strs):
    anagram_map = {}
    for s in strs:
        sorted_key = "".join(sorted(s))
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
        anagram_map[sorted_key].append(s)
    return list(anagram_map.values())

def solve_largest_subsequence(s):
    # 各文字が最後に出現する位置を記録
    last_occurrence = {char: i for i, char in enumerate(s)}
    stack = []
    seen = set() # スタックに入っているか管理
    
    for i, char in enumerate(s):
        if char in seen:
            continue
            
        # スタックの頂上(直前の文字)よりも、今の文字(char)の方が強くて(大きくて)、
        # かつ、スタックの頂上の文字が「まだ後でも出てくる」なら、頂上を捨てる
        while stack and char > stack[-1] and i < last_occurrence[stack[-1]]:
            removed_char = stack.pop()
            seen.remove(removed_char)
            
        stack.append(char)
        seen.add(char)
        
    return "".join(stack)

print(solve_largest_subsequence("aabcb")) 

def countBinarySubstrings(s):
    # 1. 連続する文字の数をグループ化する
    # 例: "00111001" -> [2, 3, 2, 1]
    groups = []
    count = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count) # 最後のグループを追加
    
    # 2. 隣り合うグループの小さい方の数を足していく
    ans = 0
    for i in range(1, len(groups)):
        ans += min(groups[i-1], groups[i])
        
    return ans

print(countBinarySubstrings("00111001")) 

#　ハトの巣原理
def solution(A):
    num_set = set(A)
    for i in range(1, len(A) + 2):
        if i not in num_set:
            return i
    return 1

def solution_binary(S):
    S = S.lstrip('0')
    if not S:
        return 0
    ones = S.count('1')
    zeros = S.count('0')
    return (ones * 2) + zeros -1

def solution_frogs(blocks):
    N = len(blocks)
    if N == 0:
        return 0
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if i > 0 and blocks[i-1] >= blocks[i]:
            L[i] = L[i-1]
        else:
            L[i] = i
    for i in range(N - 1, -1, -1):
        if i < N - 1 and blocks[i+1] >= blocks[i]:
            R[i] = R[i+1]
        else:
            R[i] = i
    max_dist = 0
    for i in range(N):
        dist = R[i] - L[i] + 1
        if dist > max_dist:
            max_dist = dist
    return max_dist

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        H = int(next(iterator))
        W = int(next(iterator))
        N = int(next(iterator))
    except StopIteration:
        return
    stamps = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for _ in range(H):
            stamps[i].append(next(iterator))
    R = int(next(iterator))
    C = int(next(iterator))
    B = []
    for r in range(R):
        for h in range(H):
            line_parts = []
            for c in range(C):
                stamp_idx = B[r][c]
                line_parts.append(stamps[stamp_idx][h])
            print("".join(line_parts))

if __name__ == '__main__':
    solve()
    

