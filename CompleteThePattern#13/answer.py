# encode: utf-8
'''
1     1     1
 2   2 2   2
  3 3   3 3
   4     4
  3 3   3 3
 2   2 2   2
1     1     1
'''


def pattern(n, x=1):
    if n < 0:
        return ""
    msg = u""
    total_white = ((n * 2) - 1)
    for i in xrange(1, n + 1):
        msg += create_str(i, n, total_white, x)
    for i in reversed(range(1, n)):
        msg += create_str(i, n, total_white, x)
    return msg


def create_str(i, n, total_white, times):
    msg = ""
    bf_af_white_space = i - 1
    middle_white_space = total_white - (i * 2)
    for x in range(1, times + 1):
        msg += " " * bf_af_white_space
        if i > 9:
            msg += str(i % 10)
        else:
            msg += str(i)
        if middle_white_space > 0:
            msg += " " * middle_white_space
            if i > 9:
                msg += str(i % 10)
            else:
                msg += str(i)
        msg += " " * bf_af_white_space
    msg += "\n"
    return msg

print pattern(25)
