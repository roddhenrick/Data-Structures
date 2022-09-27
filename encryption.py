import math


def encryption(inp):
    def shift_3(str: str):
        line_lst = [x for x in str.split('\n')]
        line_lst = map(
            lambda y: ''.join(
                [chr(ord(x) + 3) if x.isalpha() else x for x in y])[::-1],
            line_lst[1:]
        )
        return list(line_lst)

    def unshift_1(lines: list):
        heads = list(
            map(
                lambda k: k[:math.ceil(
                    len(k) / 2)] if len(k) % 2 == 0 else k[:math.ceil(len(k) / 2) - 1],
                lines
            )
        )

        tails = list(
            map(
                lambda y: y[math.ceil(
                    len(y) / 2):] if len(y) % 2 == 0 else y[math.ceil(len(y) / 2) - 1:],
                lines
            )
        )

        tails_unshift_1 = map(lambda z: ''.join(
            [chr(ord(x) - 1) for x in z]), tails)
        zipped = zip(heads, tails_unshift_1)
        return list(map(lambda m: ''.join(list(m)), zipped))

    lst_lines = unshift_1(shift_3(inp))

    output = '\n'.join(lst_lines)
    return output

str = '''4
Texto #3
abcABC1
vxpdylY .ph
vv.xwfxo.fd'''

print(encryption(str))
