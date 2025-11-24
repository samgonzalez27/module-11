"""Additional validation unit tests for `CalculationCreate`."""

import pytest

from pydantic import ValidationError

from app.schemas import CalculationCreate


def test_missing_a_field_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(b=1, type="add")


def test_missing_b_field_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(a=1, type="add")


def test_non_numeric_operands_raise():
    with pytest.raises(ValidationError):
        CalculationCreate(a="one", b=2, type="add")
    with pytest.raises(ValidationError):
        CalculationCreate(a=1, b="two", type="add")
