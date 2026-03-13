"""Input validation utilities for the depot system."""


def is_positive(value):
    """Check that a value is a positive number."""
    return isinstance(value, (int, float)) and value > 0


def is_non_negative(value):
    """Check that a value is a non-negative number."""
    return isinstance(value, (int, float)) and value >= 0


def is_valid_name(name):
    """Check that a name is a non-empty string without leading/trailing spaces."""
    if not isinstance(name, str):
        return False
    return len(name.strip()) > 0 and name == name.strip()


def is_valid_kind(kind, valid_kinds=("standard", "reserve")):
    """Check that a tank kind is one of the allowed values."""
    return kind in valid_kinds


def validate_transfer_args(dest_name, source_name, amount):
    """Validate arguments for a transfer operation.

    Returns a list of error strings (empty if valid).
    """
    errors = []
    if not is_valid_name(dest_name):
        errors.append("invalid destination name")
    if not is_valid_name(source_name):
        errors.append("invalid source name")
    if dest_name == source_name:
        errors.append("source and destination must differ")
    if not is_positive(amount):
        errors.append("amount must be positive")
    return errors


def clamp(value, minimum, maximum):
    """Clamp a value to the given range."""
    return max(minimum, min(maximum, value))


def require_positive(value, name="value"):
    """Raise ValueError if value is not positive."""
    if not is_positive(value):
        raise ValueError(f"{name} must be positive")


def require_non_negative(value, name="value"):
    """Raise ValueError if value is negative."""
    if not is_non_negative(value):
        raise ValueError(f"{name} must be non-negative")
