# 要件:
    # リスト内で同じ数字が連続している箇所を、一文字に圧縮する。
# 設計:
    # for文で連続部分を探し、連続を排除したリストを作る。 

from typing import Iterable


def compress(items: list) -> Iterable:
    comp_items = []  # 連続部分を排除したリスト。 

    if items == []:  # リストが空であれば、そのまま返す。
        return items
    else:
        x = items[0]
        comp_items.append(x)

    for i in items:
        if x != i:
            comp_items.append(i)
            x = i
        else:
            x = i
    return comp_items


if __name__ == '__main__':
    print("Example:")
    print(list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])) == [5, 4, 5, 6, 5, 7, 8, 0]
    assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 所感
    # 組み込み関数ではなく、for文の応用を問われる良い問題だった。