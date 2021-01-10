#要件
    #テキストの単語の並びと、単語リスト内の単語の表示順序が同一かを調べる。
    #テキストの単語が単語リスト内にない場合、Falseを返す。
    #単語リストに単語が重複して入っている場合、Falseを返す。
    #デキストが空の場合、Falseを返す。
    #単語リストとテキストの文字列は、単語として一致するようにする。
    #テキストの単語が単語リストにない場合、Falseを返す。
#設計
    #テキストを単語単位に分割し、単語リストとの一致を診断する。(単語の一致確認)
    #set関数で処理した単語リストと、元の単語リストの要素数の一致を調べる。(単語リストの重複確認)
    #for文を使って、単語リストでテキストを検索する。
        #find関数で位置を拾い、単語がない場合はFalse,ある場合はcheckリストにappendする。
    #sortしたcheckリストが、元のcheckリストと等しいかを調べる。(順序の一致確認)
        

def words_order(text: str, words: list) -> bool:
    # your code here
    check = []
    
    for i in set(words):
        if i not in text.split():
            return False
    
    if len(set(words)) == len(words):        
        for i in words:
            a = text.find(i)
            if a == -1:
                return False
            else:
                check.append(a)
    else:
        return False
            
    if sorted(check) == check:
        return True
    else:
        return False       
            
if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

#所感
    #要件と設計をしっかり書き下すことで処理の順序に見通しがつき、コーディングが成功した。
    #構文の基礎をもっと理解すれば、行数を半分ほどに減らせそうだった。