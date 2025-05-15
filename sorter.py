import logging
from exceptions import InvalidDimensionError, InvalidInputTypeError

# Constants for sorting criteria
VOLUME_THRESHOLD = 1_000_000  # cm³
DIMENSION_THRESHOLD = 150     # cm
MASS_THRESHOLD = 20           # kg

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_inputs(width: float, height: float, length: float, mass: float) -> None:
    """
    Validates that all inputs are valid numbers and non-negative.
    """
    if not all(isinstance(x, (int, float)) for x in (width, height, length, mass)):
        raise InvalidInputTypeError("All inputs must be numbers (int or float).")
    if any(x <= 0 for x in (width, height, length)):
        raise InvalidDimensionError("Dimensions must be positive numbers.")
    if mass < 0:
        raise InvalidDimensionError("Mass must be non-negative.")

def is_bulky(width: float, height: float, length: float) -> bool:
    """
    Determines if a package is bulky based on volume or dimension.
    """
    volume = width * height * length
    return volume >= VOLUME_THRESHOLD or max(width, height, length) >= DIMENSION_THRESHOLD

def is_heavy(mass: float) -> bool:
    """
    Determines if a package is heavy based on mass.
    """
    return mass >= MASS_THRESHOLD

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package into one of the categories: REJECTED, SPECIAL, or STANDARD.
    """
    try:
        validate_inputs(width, height, length, mass)
        bulky = is_bulky(width, height, length)
        heavy = is_heavy(mass)
        logger.info(f"Sorting package: width={width}, height={height}, length={length}, mass={mass}, bulky={bulky}, heavy={heavy}")

        # Decision tree: REJECTED if both bulky and heavy, SPECIAL if either, STANDARD otherwise
        if bulky and heavy:
            return "REJECTED"
        elif bulky or heavy:
            return "SPECIAL"
        else:
            return "STANDARD"
    except (InvalidInputTypeError, InvalidDimensionError) as e:
        logger.error(f"Invalid input: {str(e)}")
        raise