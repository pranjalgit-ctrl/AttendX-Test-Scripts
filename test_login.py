import unittest


def login(username, password):
    if username == "student01" and password == "AttendX@123":
        return "Login successful"
    return "Invalid username or password"


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("student01", "AttendX@123"),
            "Login successful"
        )

    def test_invalid_password(self):
        self.assertEqual(
            login("student01", "wrong123"),
            "Invalid username or password"
        )

    def test_empty_credentials(self):
        self.assertEqual(
            login("", ""),
            "Invalid username or password"
        )


if __name__ == "__main__":
    unittest.main()
