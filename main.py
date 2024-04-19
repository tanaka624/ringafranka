# ひらがな50音リスト
hiragana = [
    "あ","い","う","え","お",
    "か","き","く","け","こ",
    "さ","し","す","せ","そ",
    "た","ち","つ","て","と",
    "な","に","ぬ","ね","の",
    "は","ひ","ふ","へ","ほ",
    "ま","み","む","め","も",
    "や","ゆ","よ",
    "ら","り","る","れ","ろ",
    "わ","を","ん"
]


def decode(input_hiragana):
    output_hiragana = ""
    for char in input_hiragana:
        if char in hiragana:
            index = hiragana.index(char)
            index = (index + 1) % len(hiragana)
            output_hiragana += hiragana[index]
        else:
            output_hiragana += char
    return output_hiragana


print("空文字を入力するとプログラムを終了します")

while True:
    input_hiragana = input("ひらがなを入力してください：")
    if not input_hiragana:
        break
    print("変換後のひらがな: " + decode(input_hiragana))

print("プログラムを終了します")