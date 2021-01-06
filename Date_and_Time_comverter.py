#要件
    #数値で表される日付を、カレンダー表記にする。
#設計
    #数値での日付表記は０埋めされていて桁数が変わらないため、日時等に相当する値はスライスで指定する。

def date_time(time: str) -> str:
    #replace this for solution
    month_list = [0, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 
    day = str(int(time[0:2]))
    month = month_list[int(time[3:5])]
    year = str(int(time[6:10]))
    hour = str(int(time[11:13]))
    minute = str(int(time[14:16]))
    h = " hour" if int(hour) == 1 else " hours"
    m = " minute" if int(minute) == 1 else " minutes"

    return " ".join([day, month, year + " year", hour + h, minute + m] )

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

#所感
    #datetime関数を使いたかったが、まだよくわからなかった。
    #力技の記述だったが、datetime関数を使わないコードの中では綺麗な方だった。
