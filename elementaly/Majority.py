# 要件
    # ブール値を複数格納したリストの中に、真偽どちらの値が多く含まれているかを調べる。
# 設計
    # for-if文を用いて、真と偽の処理回数をカウントする。
    # カウントしたら、どちらが多いかを比較する。

def is_majority(items: list) -> bool:
    # your code here
    t = 0
    f = 0

    for i in items:
        if i:
            t += 1
        else:
            f += 1
    
    if f < t :
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 所感
    # for文とif文の理解度を確認するような課題だった。