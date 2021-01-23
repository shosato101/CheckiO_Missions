# 要件
    # サンプルデータの中央値を求める。
# 設計
    # 中央値を取るため、サンプルデータを整列する。
    # サンプルデータの数が偶数、奇数かを調べる。
    # 中央値の求め方をコードで表現する。
from typing import List
import numpy as np

def checkio(data: List[int]) -> [int, float]:

    # 引数を前処理する。
    data.sort()  

    if len(data) % 2 == 0:  #データの数が偶数個の場合
        split_data = list(np.array_split(data, 2))
        median_raw = (split_data[0][-1] + split_data[1][0]) / 2
        median = round(median_raw, 2)  #小数点以下の値を持ち得るため。
    else:  #データの数が奇数個の場合
        median_index = (len(data) - 1) / 2
        median_raw = data[int(median_index)]
        median = round(median_raw, 2)  #戻り値の型を揃えるため。
    
    return median

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 所感
    # わかり易い名前を変数等につけるように意識した。