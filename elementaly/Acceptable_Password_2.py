# Taken from mission Acceptable Password I
# 要件
    # 入力されたパスワードが6文字以上かを判定する。
    # かつ、数字を一文字以上含んでいるかを判定する。
# 設計
    # パスワードの文字をint()にて処理し、正常に処理された回数が1以上であるかを判定する。
    # パスワードの長さが6文字以上、かつ、int型に変換できる文字を含んでいるかを判定する。

def is_acceptable_password(password: str) -> bool:
    # your code here
    dig = 0

    for i in list(password):
        try:
            int(i)
            dig += 1
        except ValueError:
            continue

    if len(password) > 6 and dig > 0:
        return True
    
    return False

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 所感
    # 引数は全てstr型で渡されるので、最初は戸惑った。
    # 例外処理で正常に処理された回数をカウントするやり方でやってみたが、今回の案件で最適だったのかは疑問。