#要件
    #リスト内のファイルを、ファイル名の拡張子ごとに整列する。
    #拡張子の表記がないファイル名も存在する。
    #並び順は、拡張子表記なし < ファイル名+拡張子 の昇順とする
    #同じ拡張子のファイルは名前順で並べ替える。
#設計
    #最初にファイル名のリストをsortし、一旦整理する。
    #ファイル名について、拡張子を含むものと含まないものとを分ける。
        #ファイル名をrfind(".")を基準にスライスし、左右どちらかの要素が0であれば拡張子の表記なしと判断する。
        #拡張子の表記なしのものは、そのまnameリストに格納する。
        #拡張子ありの物はsplit(".")で分割してリスト型に整形し、末尾の拡張子を扱えるようにしてextリストにまとめる。
        #末尾の拡張子を基準にsortした後、分割を元の形に修正してsorted_extリストにまとめる。
    #処理完了後、拡張子を含まないリストと含むリストを結合する。
    

from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    name = []
    ext = []
    sorted_ext = []
    
    for i in sorted(files):
        if len(i[i.rfind("."):]) == 0 or len(i[:i.rfind(".")]) == 0:
            name.append(i)
        else:
            l = i.split(".")
            ext.append(l)

    for i in sorted(ext, key=lambda val : val[-1]):
        a = ".".join(i)
        sorted_ext.append(a)
 
    return name + sorted_ext

#所感
    #lambda式の理解度をもっと深めたい。
    #assertエラーに一つずつ対応しながら進んだので、実装ではもっと苦労しそうだった。
    #処理内容は簡易にまとめることが出来たと感じる。

if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
