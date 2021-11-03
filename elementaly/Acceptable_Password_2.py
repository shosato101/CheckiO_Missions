# Taken from mission Acceptable Password I

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
