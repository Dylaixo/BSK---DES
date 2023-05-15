def string_to_bin_single(input: str):
    output = int(' '.join(format(ord(x), 'b') for x in input))
    return f"{output:08d}"


def binary_to_string_single(bits):
    ascii_code = int(bits, 2)
    return chr(ascii_code)


def sting_to_bin(input: str):
    output = ''
    assert len(input)==8, "wiadomość powinna posiadać 8 znaków"
    for char in input:
        output = output + string_to_bin_single(char)
    return output


def binary_to_string(input):
    bits_list = [input[i:i+8] for i in range(0, len(input), 8)]
    output = ''
    for bits in bits_list:
        output = output + binary_to_string_single(bits)
    return output


def xor_single(input1, input2):
    if input1 != input2:
        return '1'
    return '0'


def xor(input1, input2):
    assert len(input1) == len(input2), "Oba bloku muszą mieć taką samą długość"
    output = ''
    for i1, i2 in zip(input1, input2):
        output = output + xor_single(i1, i2)
    return output
