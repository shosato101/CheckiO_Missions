#要件
    #とある数Nをインデックスの値として、与えられた配列から要素を取り出せるかを調べる。
        #要素を取り出せた場合、その要素を、とある数Nの値で累乗した値を返す。
        #インデックスエラーの場合、−１を返す。
#設計
    #例外処理の構文を用いる。
def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """

    try:
        array[n]
    except IndexError:
        return -1
    else:
        return array[n] ** n

if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#所感
    #エラーの際は-1を返すとのことだったので最初はfindメソッドを使うのかと思った。
    #しかしながら、読み易さを優先したコーディングを考えているうちに例外処理に行き着いた。
