"""Password hashing utilities using Passlib.

Provides a small, object-oriented wrapper `PasswordHasher` and convenience
module-level helpers `hash_password` and `verify_password` for ease of use in
the rest of the application.
"""
from __future__ import annotations

from passlib.context import CryptContext


class PasswordHasher:
    """Encapsulates password hashing behavior.

    Uses `passlib`'s `CryptContext` to support bcrypt and allow future upgrades
    while keeping a single place to change hashing policy.
    """

    def __init__(self, schemes: list[str] | None = None, deprecated: str | None = None):
        if schemes is None:
            schemes = ["bcrypt"]
        self._pwd_context = CryptContext(schemes=schemes, deprecated=deprecated)

    def hash(self, raw_password: str) -> str:
        """Hash a raw password and return the encoded hash."""
        return self._pwd_context.hash(raw_password)

    def verify(self, raw_password: str, hashed: str) -> bool:
        """Verify a raw password against the stored hash."""
        return self._pwd_context.verify(raw_password, hashed)


# Module-level default hasher and helpers
_default_hasher = PasswordHasher()


def hash_password(raw_password: str) -> str:
    return _default_hasher.hash(raw_password)


def verify_password(raw_password: str, hashed: str) -> bool:
    return _default_hasher.verify(raw_password, hashed)
