# utils/jwt.py
# Simple test implementation for metadata extraction

import time

class JWTUtil:
    @staticmethod
    def generate_token(payload: dict):
        """
        Fake token generator (for testing metadata extraction only).
        """
        return f"fake-jwt-token-for-{payload.get('user')}-{int(time.time())}"

    @staticmethod
    def verify_token(token: str):
        """
        Fake token validation (for test only).
        """
        return token.startswith("fake-jwt-token")
