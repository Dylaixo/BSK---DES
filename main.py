import permutacje
import number_systems
import slide


def encrypt(msg, key, decript):
    msg_bin = number_systems.sting_to_bin(msg)
    msg = permutacje.permute(msg_bin, permutacje.initial_permutation, 64)
    msg_L = msg[0:32]
    msg_P = msg[32:64]
    key_bin = number_systems.sting_to_bin(key)
    key = permutacje.permute(key_bin, permutacje.PC1, 64)
    key_C = key[0:28]
    key_D = key[28:56]
    slide_C = slide.slide_to_left(key_C)
    slide_D = slide.slide_to_left(key_D)
    subkeys = []
    for s_C, s_D in zip(slide_C, slide_D):
        subkey = s_C + s_D
        subkey = permutacje.permute(subkey, permutacje.PC2, 56)
        subkeys.append(subkey)
    if decript is True:
        subkeys = subkeys[::-1]
    for subkey in subkeys:
        tmp_P = msg_P
        msg_P = permutacje.permute(msg_P, permutacje.expansion_table, 32)
        xor_return = number_systems.xor(subkey, msg_P)
        xor_list = [xor_return[i * 6:i * 6 + 6] for i in
                    range(0, int(len(xor_return) / 6))]
        sbox_res = permutacje.sbox_permute(xor_list)
        msg_P = permutacje.permute(sbox_res, permutacje.permutation_funcion, 32)
        msg_P = number_systems.xor(msg_P, msg_L)
        msg_L = tmp_P

    return permutacje.permute(msg_P + msg_L, permutacje.final_perm, 64)


def encrypt_wrapper(msg: str, key: str, decrypt=False):
    output = ''
    while len(msg) > 8:
        tmp = msg[0:8]
        msg = msg[8:]
        output = output + encrypt(tmp, key, decrypt)
    output = output + encrypt(msg, key, decrypt)
    return output


eo = encrypt_wrapper('ABCDEFGHABCDEFGHABCDEFGH', 'key1key1')
e = int(eo, 2)
print(number_systems.binary_to_string(
    encrypt_wrapper(
        number_systems.binary_to_string(eo),
        'key1key1',
        decrypt=True)))
