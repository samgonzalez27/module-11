"""Pydantic schemas for user input/output.

- `UserCreate` for incoming user creation payloads (contains `password`).
- `UserRead` for returning user data to clients (omits `password_hash`).

This file uses Pydantic v2 conventions (`model_config = ConfigDict(from_attributes=True)`)
so schemas can be created with `.model_validate()` or `.model_validate()` from
ORM objects/dicts.
"""
from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict
from typing import Literal


# allowed operation types for calculations
CalcType = Literal["add", "subtract", "multiply", "divide"]


class UserCreate(BaseModel):
    """Schema for user creation requests.

    Includes the plain-text `password` field which will be hashed before
    storing in the database.
    """

    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    """Schema for returning user data to clients.

    This deliberately omits any password or password_hash fields.
    """

    id: int
    username: str
    email: EmailStr
    created_at: datetime | None = None

    # enable ORM-style population (Pydantic v2)
    model_config = ConfigDict(from_attributes=True)



class CalculationCreate(BaseModel):
    """Schema for creating a Calculation."""

    a: float
    b: float
    type: CalcType


class CalculationRead(BaseModel):
    """Schema for reading Calculation objects from ORM."""

    id: int
    a: float
    b: float
    type: CalcType
    result: float | None = None

    model_config = ConfigDict(from_attributes=True)
