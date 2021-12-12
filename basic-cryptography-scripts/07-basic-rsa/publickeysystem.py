from os import urandom
from gmpy2 import mpz
from gmpy2 import invert, t_mod, mul, powmod

TOTAL_LENGTH = 128
REQUIRED_RANDOM_BYTES = 8

def compute_d(e, N, p, q):
    # d * e mod phi(N) = 1
    # where phi(N) = N - p - q + 1
    phiN = phi(N, p, q)
    d = invert(mpz(e), mpz(phiN))
    x = mul(mpz(d), mpz(e))
    assert t_mod(x, mpz(phiN)) == 1
    return d.digits()


def phi(N, p, q):
    return (mpz(N) - mpz(p) - mpz(q) + 1).digits()


def decrypt(y, d, N):
    return powmod(y, d, N)


def encrypt(x, e, N):
    return powmod(x, e, N)


def decrypt_pipeline(ciphertext, d, N):

    m_decimal = decrypt(mpz(ciphertext), mpz(d), mpz(N))
    m_bytes = int.to_bytes(int(m_decimal), TOTAL_LENGTH, "big")

    assert m_bytes[0] == 2

    for b in range(0, TOTAL_LENGTH):
        if m_bytes[b] == 0:
            return (m_bytes[b+1:]).decode('utf8')

    return None


def generate_hexstring(length):
    zerobyte = bytes(1)
    r = bytearray()
    i = 0
    while i < length:
        x = urandom(1)
        if x != zerobyte:
            r += x
            i += 1
    return r.hex()


def encrypt_pipeline(plaintext, e, N):

    raw = bytes(plaintext, 'utf8')
    assert len(plaintext) < TOTAL_LENGTH - 2 - REQUIRED_RANDOM_BYTES
    length = TOTAL_LENGTH - len(raw) - 2
    random_hexstring = generate_hexstring(length)

    final_bytes = bytes.fromhex('02' + random_hexstring + '00') + raw
    final_decimal = mpz(int.from_bytes(final_bytes, 'big'))

    ciphertext = str(encrypt(final_decimal, mpz(e), mpz(N)))
    return ciphertext

