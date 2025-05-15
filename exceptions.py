class InvalidDimensionError(ValueError):
    """Raised when input dimensions or mass are invalid (negative or zero)."""
    pass

class InvalidInputTypeError(ValueError):
    """Raised when input types are invalid (not numbers)."""
    pass