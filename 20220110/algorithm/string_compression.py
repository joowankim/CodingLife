# 프로그래머스 - 문자열 압축
#
# n개 단위로 압축한 것 중 가장 짧은 길이
# 1. 문자열 압축하기
#       1.1. 반복되는 문자열 길이를 순차적으로 늘려가며 각 길이일 때 문자열 압축하기
#       1.2. i개 단위로 문자열 압축하기
# 2. 최소 길이 문자열의 길이 반환하기


def compress(length, s):
    compressed = ""
    repeated = s[:length]
    cnt = 1
    for i in range(length, len(s), length):
        if repeated == s[i:i+length]:
            cnt += 1
        else:
            if cnt > 1:
                compressed += str(cnt) + repeated
            else:
                compressed += repeated
            repeated = s[i:i+length]
            cnt = 1
    if cnt > 1:
        compressed += str(cnt) + repeated
    else:
        compressed += repeated
    return compressed


def compressed_lengths(s):
    return [len(compress(i, s)) for i in range(1, len(s))]


def solution(s):
    if len(s) == 1:
        return 1
    return min(compressed_lengths(s))


assert compress(1, "aabbaccc") == "2a2ba3c"
assert compress(1, "abcabcdede") == "abcabcdede"
assert compress(2, "abcabcdede") == "abcabc2de"
assert compress(3, "abcabcdede") == "2abcdede"

assert compressed_lengths("aabbaccc") == [7, 8, 8, 8, 8, 8, 8]
assert compressed_lengths("abcabcdede") == [10, 9, 8, 10, 10, 10, 10, 10, 10]
assert compressed_lengths("xababcdcdababcdcd") == [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]

assert solution("aabbaccc") == 7
assert solution("ababcdcdababcdcd") == 9
assert solution("abcabcdede") == 8
assert solution("abcabcabcabcdededededede") == 14
assert solution("xababcdcdababcdcd") == 17
assert solution("a") == 1
assert solution("ab") == 2
