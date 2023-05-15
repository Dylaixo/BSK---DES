import main
import number_systems


def test(msg, key):
    t1 = main.encrypt_wrapper(msg, key, decrypt=False)
    t2 = main.encrypt_wrapper(
        number_systems.binary_to_string(t1),
        key,
        decrypt=True)
    print("---------------")
    print(f"message used: {msg}")
    print(f"encypted file {number_systems.binary_to_string(t1)}")
    print(f"decrypted file {number_systems.binary_to_string(t2)}")
    print("---------------")


test('eoeoeoeoeoeoeoeo', 'ABCDEFGH')
test('test123test123', 'ABCDEFGH')
test('ABCDEFGHIJKLMNOPR', 'ABCDEFGH')
test('TESTESTEST123123123', 'ABCDEFGH')
