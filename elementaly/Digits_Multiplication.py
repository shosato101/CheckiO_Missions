# 要件
    # 0以外の各桁数の数字の積を求める。
# 設計
    # list()で一文字ずつ切り分け、for文で0を除外する。
    
def checkio(number: int) -> int:
    num = 1
    
    for i in list(str(number)):
        if int(i) == 0:
            continue
        else:
            num = num * int(i)
            
    return num


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# 所感
    # 扱っている変数のデータ型をしっかり把握する大切さを実感した。