# models/user.py
# Basic UserModel to test 'depends_on' metadata extraction

class UserModel:
    def __init__(self, username: str = None, email: str = None):
        self.username = username
        self.email = email

    def save(self):
        """
        Dummy save method for demonstration.
        """
        return f"User {self.username} saved."

    def to_dict(self):
        return {"username": self.username, "email": self.email}
