"""Validation tests for calculation schemas (TDD).

These tests assert cross-field validation such as preventing a divide-by-zero
request at the schema level.
"""

import pytest

from pydantic import ValidationError

from app.schemas import CalculationCreate


def test_reject_zero_divisor_for_divide_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=1, b=0, type="divide")


def test_accept_zero_b_for_non_divide_types():
    cc = CalculationCreate(a=1, b=0, type="add")
    assert cc.b == 0


def test_reject_zero_divisor_case_insensitive_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=1, b=0, type="Divide")
