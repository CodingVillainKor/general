_cho  = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
_jung = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
_jong = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

def decompose_hangul(c):
    c_number = ord(c) - ord("가")
    
    len_jung, len_jong = len(_jung), len(_jong)
    jong_num = c_number % len_jong
    jung_num = (c_number // len_jong) % len_jung
    cho_num  = (c_number // len_jong) // len_jung

    return [_cho[cho_num], _jung[jung_num], _jong[jong_num]]
