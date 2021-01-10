#要件
    #06:00から18:00までのあいだで、時刻に対応する太陽の角度を計算する。
    #太陽の角度は、06:00で0度、12:00で90度、18:00で180度とする。
    #角度は少数第二位まで求める。
    #範囲外の時刻である場合、"I don't see the sun!"という文字列を返す。
#設計
    #単位を分に揃える。
    #06:00から18:00までの経過時間の比率と、0度から180度までの角度の比率を対応させる。
    #入力された時刻をもとに、太陽の角度を出力する。
    
def sun_angle(time):
    #replace this for solution
    t_deg = int(time[:2]) * 60 + int(time[3:]) - 360 #timeを分に修正し、360分(6hour)を引いて、06:00以降の時間経過分を算出する。
    t_per = t_deg / 720 #06:00~18:00までの12時間(720min)のうち、時間が何割経過しているかを求める。
    sun_angle = round(180 * t_per, 2)

    if 0 <= t_deg <= 720:
        return sun_angle
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

    #所感
        #スライスの理解度が深まった。
        #関数やライブラリの知識より、要件を立式する力が求められる課題だった。
        #要件定義、問題の抽象化の大切さを体感した。
        #三項演算子で記述してみたい欲求があったが、今回は可読性を損なうだけだと感じて基本形を選んだ。
