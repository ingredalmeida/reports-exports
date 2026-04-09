import bcrypt

from app.core.exceptions import PasswordHashError

def password_hash(password: str) -> str:
    if not isinstance(password, str):
        raise PasswordHashError("Password must be a string")
    
    try:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        stored_hash = hashed_password.decode("utf-8")
        return stored_hash
    except (ValueError, TypeError) as e:
        raise PasswordHashError("Failed to hash password") from e

def password_check(entered_password: str, stored_hash: str) -> bool:
    try:
        password_bytes = entered_password.encode("utf-8")
        hashed_bytes = stored_hash.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    except (ValueError, TypeError):
        return False