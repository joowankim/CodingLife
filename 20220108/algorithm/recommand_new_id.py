# 프로그래머스 - 신규 아이디 추천


def to_lower_case(new_id):
    return new_id.lower()


def remove_invalid_characters(new_id):
    valid_characters = ""
    for character in new_id:
        added = ""
        if character == '-' or \
                character == '_' or \
                character == '.' or \
                '0' <= character <= '9' or \
                'a' <= character <= 'z':
            added = character
        valid_characters += added
    return valid_characters


def integrate_period(new_id):
    integrated_period_id = ""
    previous_character = ""
    for character in new_id:
        if character != '.':
            integrated_period_id += character
        elif character == '.' and previous_character != '.':
            integrated_period_id += '.'
        previous_character = character
    return integrated_period_id


def trim_periods(new_id):
    return new_id.strip('.')


def handle_empty_id(new_id):
    if new_id == "":
        return "a"
    return new_id


def leave_fifteen_characters(new_id):
    return trim_periods(new_id[:15])


def handle_short_id(new_id):
    id_length = len(new_id)
    if id_length < 3:
        last_character = new_id[-1]
        return new_id + last_character * (3 - id_length)
    return new_id


def solution(new_id):
    step_one = to_lower_case(new_id)
    step_two = remove_invalid_characters(step_one)
    step_three = integrate_period(step_two)
    step_four = trim_periods(step_three)
    step_five = handle_empty_id(step_four)
    step_six = leave_fifteen_characters(step_five)
    step_seven = handle_short_id(step_six)
    return step_seven


assert to_lower_case("...!@BaT#*..y.abcdefghijklm") == "...!@bat#*..y.abcdefghijklm"
assert to_lower_case("z-+.^.") == "z-+.^."
assert to_lower_case("=.=") == "=.="
assert to_lower_case("123_.def") == "123_.def"
assert to_lower_case("abcdefghijklmn.p") == "abcdefghijklmn.p"

assert remove_invalid_characters("...!@bat#*..y.abcdefghijklm") == "...bat..y.abcdefghijklm"
assert remove_invalid_characters("z-+.^.") == "z-.."
assert remove_invalid_characters("=.=") == "."
assert remove_invalid_characters("123_.def") == "123_.def"
assert remove_invalid_characters("abcdefghijklmn.p") == "abcdefghijklmn.p"

assert integrate_period("...bat..y.abcdefghijklm") == ".bat.y.abcdefghijklm"
assert integrate_period("z-..") == "z-."
assert integrate_period(".") == "."
assert integrate_period("123_.def") == "123_.def"
assert integrate_period("abcdefghijklmn.p") == "abcdefghijklmn.p"

assert trim_periods(".bat.y.abcdefghijklm") == "bat.y.abcdefghijklm"
assert trim_periods("z-.") == "z-"
assert trim_periods(".") == ""
assert trim_periods("123_.def") == "123_.def"
assert trim_periods("abcdefghijklmn.p") == "abcdefghijklmn.p"

assert handle_empty_id("bat.y.abcdefghijklm") == "bat.y.abcdefghijklm"
assert handle_empty_id("") == "a"

assert leave_fifteen_characters("bat.y.abcdefghijklm") == "bat.y.abcdefghi"
assert leave_fifteen_characters("z-") == "z-"
assert leave_fifteen_characters("a") == "a"
assert leave_fifteen_characters("abcdefghijklmn.p") == "abcdefghijklmn"

assert handle_short_id("bat.y.abcdefghi") == "bat.y.abcdefghi"
assert handle_short_id("z-") == "z--"
assert handle_short_id("a") == "aaa"

assert solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
assert solution("z-+.^.") == "z--"
assert solution("=.=") == "aaa"
assert solution("123_.def") == "123_.def"
assert solution("abcdefghijklmn.p") == "abcdefghijklmn"
