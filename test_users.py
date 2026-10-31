from models import User


def test_password_is_hashed_and_checkable():
    user = User(username="test", email="test@example.com")
    user.set_password("correct horse")

    assert user.password_hash != "correct horse"
    assert user.check_password("correct horse")
    assert not user.check_password("wrong password")


def test_same_password_produces_different_hashes():
    first = User(username="a", email="a@example.com")
    second = User(username="b", email="b@example.com")

    first.set_password("same password")
    second.set_password("same password")

    assert first.password_hash != second.password_hash