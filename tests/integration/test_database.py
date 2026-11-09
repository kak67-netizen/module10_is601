import pytest
from sqlalchemy.exc import IntegrityError

from app.auth.security import hash_password
from app.database import SessionLocal
from app.models.user import User


def test_create_user():
    db = SessionLocal()

    # Clean up in case the test was previously run
    db.query(User).filter(
        User.username == "integrationuser"
    ).delete()
    db.commit()

    user = User(
        username="integrationuser",
        email="integration@example.com",
        password_hash=hash_password("SecurePass123")
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    assert user.id is not None
    assert user.username == "integrationuser"
    assert user.email == "integration@example.com"
    assert user.password_hash != "SecurePass123"

    db.delete(user)
    db.commit()
    db.close()


def test_duplicate_username_rejected():
    db = SessionLocal()

    db.query(User).filter(
        User.username == "duplicateuser"
    ).delete()
    db.commit()

    user1 = User(
        username="duplicateuser",
        email="first@example.com",
        password_hash=hash_password("SecurePass123")
    )

    user2 = User(
        username="duplicateuser",
        email="second@example.com",
        password_hash=hash_password("SecurePass456")
    )

    db.add(user1)
    db.commit()

    db.add(user2)

    with pytest.raises(IntegrityError):
        db.commit()

    db.rollback()

    db.query(User).filter(
        User.username == "duplicateuser"
    ).delete()
    db.commit()
    db.close()


def test_duplicate_email_rejected():
    db = SessionLocal()

    db.query(User).filter(
        User.email == "duplicate@example.com"
    ).delete()
    db.commit()

    user1 = User(
        username="userone",
        email="duplicate@example.com",
        password_hash=hash_password("SecurePass123")
    )

    user2 = User(
        username="usertwo",
        email="duplicate@example.com",
        password_hash=hash_password("SecurePass456")
    )

    db.add(user1)
    db.commit()

    db.add(user2)

    with pytest.raises(IntegrityError):
        db.commit()

    db.rollback()

    db.query(User).filter(
        User.email == "duplicate@example.com"
    ).delete()
    db.commit()
    db.close()