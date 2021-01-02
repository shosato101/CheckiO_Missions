#要件
    #リストを整理して、最後尾の要素を先頭に移動する。
    #要素数が1以下、もしくはリストが空の場合、そのままの値を返す。
#設計
    #sortした後、最後尾をスライスで分割して先頭に結合する。

def replace_last(line: list) -> list:
    # your code here
    return line[-1:] + line[:-1]


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

#所感
    #これくらいのレベルならすぐに解けるようになった。