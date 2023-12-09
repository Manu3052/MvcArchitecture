from jose import JWTError

from src.infra.providers import verify_access_token


class AuthenticationMiddleware:
    """
    Class that handles the authentication of API points.
    """

    def verify_token(self, token: str) -> str:
        """
        Verify the token validly

        Args:
            token (str): Receives the token
        Returns:
            email (str): Returns a string the represents the email
        """
        try:
            email = verify_access_token(token)
        except JWTError:
            return None
        return email
