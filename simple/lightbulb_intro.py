# 要件
    # 電球の点灯時間を合計する
        # 点灯、消灯はスイッチで切り替わる。
        # 最初は消灯の状態から始まる。
        # 電球のスイッチを押した時間の履歴は、els[]に格納されている。
    # 総点灯時間の単位は秒(second)とする。
# 設計
    # 変数switchの値で、点灯と消灯の状態を判断する。
    # els[]からdatetimeの値が渡される度に、switchの値をon,offと交互に切り替える。
    # onの条件下のみ、経過時間を点灯時間(lighting_time)に加算する。

from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    switch = "off"
    lighting_time = 0

    for i in els:
        if switch == "off":
            switch = "on"
            dt1 = i
        elif switch == "on":
            switch = "off"
            turn_on = i - dt1
            lighting_time += turn_on.total_seconds()
            
    return lighting_time
    
    


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 12, 10 , 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

# 所感
    # 変数をどこに置くかで迷った。
    # 設計の流れを、コードで忠実に表現することに努めた。