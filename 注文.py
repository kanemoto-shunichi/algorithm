# ステップ1、客席の端末から料理番号、注文数を入力。在庫数を確認
# ステップ2、レンジの空き状況を監視、調理完了したら報告
# ステップ3、完成した料理をどの席に運ぶべきか確認
# ステップ4、会計を押すことで、会計を申請すべて提供されたか確認。すべて提供されていたら代金の合計を表示。そうでない場合もう少し席で待つよう表示。

import sys
from collections import deque

def order_check(input_data):
    iterator = iter(input_data)
    try:
        A = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return
    if not A == 1:
        return
    menu = []
    for _ in range(M):
        row = []
        for _ in range(3):
            row.append(int(next(iterator)))
        menu.append(row)
    while True:
        try:
            text = next(iterator)
            T = int(next(iterator))
            D = int(next(iterator))
            N = int(next(iterator))

            if text == "order":
                for info in menu:
                    if info[0] == D:
                        if info[1] >= N:
                            info[1] -= N
                            for _ in range(N):
                                print(f"received order {T} {D}")
                        else:
                            print(f"sold out {T}")
                        break
        except StopIteration:
            break

def order_cook(input_data):
    iterator = iter(input_data)
    try:
        A = int(next(iterator))
        M = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return
    if not A == 2:
        return
    menu = []
    for _ in range(M):
        row = []
        for _ in range(3):
            row.append(int(next(iterator)))
        menu.append(row)
    microwave = []
    cook_wait = deque([])
    while True:
        try:
            text = next(iterator)
            if text == "received":
                word = next(iterator)
                T = int(next(iterator))
                D = int(next(iterator))
                if len(microwave) < K:
                    microwave.append(D)
                    print(f"{D}")
                else:
                    cook_wait.append(D)
                    print("wait")
            else:
                D = int(next(iterator))
                if len(cook_wait) > 0:
                    microwave.remove(D)
                    microwave.append(cook_wait[0])
                    print(f"ok {cook_wait[0]}")
                    cook_wait.popleft()
                else:
                    microwave.remove(D)
                    print("ok")
        except StopIteration:
            break

def serving_order(input_data):
    iterator = iter(input_data)
    try:
        A = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return
    if not A == 3:
        return
    menu = []
    for _ in range(M):
        row = []
        for _ in range(3):
            row.append(int(next(iterator)))
        menu.append(row)
    serving_wait = deque([])
    while True:
        try:
            text = next(iterator)
            if text == "received":
                word = next(iterator)
                T = int(next(iterator))
                D = int(next(iterator))
                serving_wait.append((T, D))
            else:
                D = int(next(iterator))
                for info in serving_wait:
                    if info[1] == D:
                        wait_T = info[0]
                        wait_D = info[1]
                        serving_wait.remove(info)
                        print(f"ready {wait_T} {wait_D}")
                        break
        except StopIteration:
            return

def bill_order(input_data):
    iterator = iter(input_data)
    try:
        A = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return
    if not A == 4:
        return
    menu = []
    for _ in range(M):
        row = []
        for _ in range(3):
            row.append(int(next(iterator)))
        menu.append(row)
    
    while True:
        try:
            text = next(iterator)
            if text == "received":
                word = next(iterator)
                T = int(next(iterator))
                D = int(next(iterator))
                serving_wait.append((T, D))
            else:
                D = int(next(iterator))
                for info in serving_wait:
                    if info[1] == D:
                        wait_T = info[0]
                        wait_D = info[1]
                        wait.remove(info)
                        print(f"ready {wait_T} {wait_D}")
                        break
        except StopIteration:
            return


if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    A = int(input_data[0])
    if A == 1:
        order_check(input_data)
    elif A == 2:
        order_cook(input_data)
    elif A == 3:
        serving_order(input_data)
    else:
        bill_order(input_data)
