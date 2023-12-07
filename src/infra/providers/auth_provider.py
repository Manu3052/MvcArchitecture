from datetime import datetime, timedelta

from jose import jwt

SECRET_KEY = "chave-secreta"
ALGORITHM = "HS256"
EXPIRES_IN_MINUTES = 30


def create_access_token(data: dict) -> str:
    """
    This function is responsible for generating the access token

    Params:
        data (dict): Receive a dictionary with the data

    Return:
        token_jwt (str): Returns a string with the token generate
    """
    data = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)

    data.update({"exp": expiration})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt


def verify_access_token(token: str):
    """
    This function is responsible for verifying the token

    Params:
        token (str): Receive a string that represents the token.

    Returns:
        sub (dict): Returns a dict with the valid data
    """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    sub = payload.get("sub")
    return sub
