#要件
    #与えられたitemsリストをborderの値までの部分で切り取りたい。
    #borderの値が見つからない場合、リストはそのまま。
    #リストが空の場合も、リストはそのまま。
#設計
    #for文でitemsリストとborderの値を照合する。
    #borderがヒットしなければ、そのままselectionのリストに加える。
    #borderがヒットした場合、borderもselectionのリストに加えて処理を終了する。
from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    # your code here
    selection = []
    
    for i in items:
        if i != border:
            selection.append(i)
        else:
            selection.append(i)
            break

    return selection

if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
#所感
    #スライスとfor文のどちらが適切かを問うような問題だった。