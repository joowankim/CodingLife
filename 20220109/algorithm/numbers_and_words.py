# 프로그래머스 - 숫자 문자열과 영단어
# onetwo를 ['one', 'two']로 나눌 수 있는가?
# 12three를 ['1', '2', 'three']나 ['12', 'three']로 나눌 수 있나?


to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def solution(s):
    answer = ""
    number = ""
    for c in s:
        if "0" <= c <= "9":
            answer += c
            continue
        number += c
        if number in to_number.keys():
            answer += to_number[number]
            number = ""
    return int(answer)


assert solution("one4seveneight") == 1478
assert solution("23four5six7") == 234567
