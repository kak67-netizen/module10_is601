
from app.auth.security import hash_password, verify_password


def test_hash_password():
    password = "SecurePassword123"
    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_verify_correct_password():
    password = "SecurePassword123"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_wrong_password():
    password = "SecurePassword123"
    hashed = hash_password(password)

    assert verify_password("WrongPassword", hashed) is False


def test_unique_password_hashes():
    password = "SecurePassword123"

    hash1 = hash_password(password)
    hash2 = hash_password(password)

    assert hash1 != hash2
