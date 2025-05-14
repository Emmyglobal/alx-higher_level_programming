#!/usr/bin/python3
def remove_char_at(str, n):
    ans = ""
    if n >= 0 and n <= len(str):
        for i in range(len(str) - 1):
            if i == n:
                str = str.replace(str[i], "")
            ans += str[i]
        return ans
    else:
        return str