#要件
    #リスト内の全ての要素が同一かを調べる。
#設計思想
    #リストの全要素が先頭要素と一致するかを調べる。
    
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    for i in elements:
        if elements[0] != i:
            return False
    return True
    


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

#所感
    #組み込み関数all()を使ったやり方が、簡潔で美しかった。
    #return all(elements[0] == i for i in elements)