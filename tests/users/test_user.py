from ecommerce.app.users import User

def test_user_creation():
    u = User("alice")
    assert u.username == "alice"
