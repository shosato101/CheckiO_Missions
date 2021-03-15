# 要件
    # リスト内の数字を昇順に整理したい。
    # 整列の際、出現頻度の高い数字を先頭に優先したい。
# 設計
    # リストをソートする。
    # ソートしたリストを、lambda式を使って重複数の多い要素を先頭に配置する。


def frequency_sorting(numbers):

    return sorted(sorted(numbers), key=lambda x: numbers.count(x), reverse=True)



if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 所感
    # 最初は関数を作って整列させようとしていたが、とても煩雑になった。
    # 調べてみると、こういったソート手順の際にlambda式を使えばいいとわかった。
    # sorted関数のkey指定をもっと使いこなしていきたい。
