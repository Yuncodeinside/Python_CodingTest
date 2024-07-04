
def solution(letter):
    morse_code_dict = {
          '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z'
    }
    
    #letter를 공백 단위로 분리함
    words = letter.split(' ')
    print(words)
    
    decode_message = ''.join(morse_code_dict[code] for code in words)
    print(morse_code_dict[code] for code in words)
    return decode_message

print(solution(".... . .-.. .-.. ---"))  # 출력: "hello"