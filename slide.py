import permutacje

key_slide_16 = [
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    1
]

def slide_to_left(input):
    output = []
    for i in key_slide_16:
        tmp = input[i:]
        input = tmp + input[:i]
        output.append(input)
    return output

