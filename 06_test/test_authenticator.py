import pytest
from authenticator import Authenticator

def test_register_success():
    auth = Authenticator()
    auth.register("user01","pass01")
    assert "user01" in auth.users
    assert auth.users["user01"] == "pass01"

def test_register_failure():
    auth = Authenticator()
    auth.register("user01","pass01")
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        auth.register("user01","pass02")

def test_login_success():
    auth = Authenticator()
    auth.register("user01","pass01")
    message = auth.login("user01","pass01")
    assert message == "ログイン成功"

def test_login_failure():
    auth = Authenticator()
    auth.register("user01","pass01")
    # passが間違い
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        auth.login("user01","passNG")
    # userが存在しない
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        auth.login("userNG","pass01")