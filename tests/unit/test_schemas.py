
import pytest
from pydantic import ValidationError

from app.schemas.user import UserCreate, UserRead


def test_valid_user_create():
    user = UserCreate(
        username="testuser",
        email="test@example.com",
        password="SecurePass123"
    )

    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="testuser",
            email="invalid-email",
            password="SecurePass123"
        )


def test_short_username():
    with pytest.raises(ValidationError):
        UserCreate(
            username="ab",
            email="test@example.com",
            password="SecurePass123"
        )


def test_short_password():
    with pytest.raises(ValidationError):
        UserCreate(
            username="testuser",
            email="test@example.com",
            password="123"
        )


def test_user_read_excludes_password():
    user = UserRead(
        id=1,
        username="testuser",
        email="test@example.com"
    )

    data = user.model_dump()

    assert "password" not in data
    assert "password_hash" not in data
