# 要件
    # 与えられた配列を二分割する。
    # 要素が奇数の場合、最初の配列に過半数分を格納する。
    # 要素が０の場合、実行結果に空のリスト２つを返す。

# 設計
    # 空のリストを二つ用意する。(list1,list2)
    # for文にて、配列の要素をlist1から格納していく。
    # 処理回数が総要素数の半数、及び過半数に達した後、格納先をlist2へと変更する。
    # list1,list2の処理結果を返す。

def split_list(items: list) -> list:
    list1 = []
    list2 = []
    lists = [list1, list2]
    count = 0

    for i in items:
        count += 1
        if (len(items) + 1) - count >= count:
            list1.append(i)
        else:
            list2.append(i)
    return lists


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 所感
    # 配列の要素数が３の場合に要件未達成になってしまうことへの対策として、要素数に+1の冗長性を持たせた。
    # 切り捨て除算とスライスの位置の把握ができると、もっと簡潔になりそうだった。
