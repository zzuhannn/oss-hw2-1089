def digit_sum(n):
    """n 의 각 자리 숫자를 모두 더한다.  예) digit_sum(1234) -> 10"""
    total = 0
    for ch in str(n):
        total += int(ch)
    return total


def lucky_number(n):
    """한 자리 수가 될 때까지 digit_sum 을 반복한다.  예) 1234 -> 10 -> 1"""
    while n >= 10:
        n = digit_sum(n)
    return n
