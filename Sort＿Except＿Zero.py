from typing import Iterable


def except_zero(items):
    """
    0の位置を変えずに、0以外の数値を昇順に整列させる。

    Parameters
    ----------
    items : list
        対象のデータのリスト。

    Returns
    -------
    sorted_items : list
        0の位置を変えずに、0以外の数値を昇順に整列させたリスト。
    """
    
    zeros_index = [i for i, x in enumerate(items) if x == 0]  #処理後のリストに0を復旧するため
    remove_zero_items = ([i for i in items if i * 1 != 0])  #0については処理の最後に追加するため

    sorted_items = sorted(remove_zero_items)
    

    for i in zeros_index:
        sorted_items.insert(i, 0)
        
    return sorted_items

if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete!")
