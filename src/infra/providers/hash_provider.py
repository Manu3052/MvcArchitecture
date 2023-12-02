from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def hash_generate(text: str) -> str:
    """
    This function is responsible for receiving an text and encrypting it using CryptContext

    Params:
        text (str): This params receives an string

    Returns:
        hash (str): Returns an encrypted information
    """
    hash = pwd_context.hash(text)
    return hash


def verify_hash(password_hash, hash) -> bool:
    """
    This function is responsible for receiving an string which represents an encrypted information and returning

    Params:
        password_hash (str): Receives the information encrypted
        hash (str): Receives the hash
    Returns:
        result (bool): Returns a boolean with true of false for the veracity of the hash
    """
    result = pwd_context.verify(password_hash, hash)
    return result
