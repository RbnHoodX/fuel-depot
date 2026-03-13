"""Lookup tables for fuel specifications and standards."""


FUEL_TYPES = {
    "diesel": {"density": 832, "flash_point": 52, "octane": None, "cetane": 51},
    "gasoline": {"density": 737, "flash_point": -43, "octane": 91, "cetane": None},
    "kerosene": {"density": 810, "flash_point": 38, "octane": None, "cetane": None},
    "jet-a": {"density": 804, "flash_point": 38, "octane": None, "cetane": None},
    "ethanol": {"density": 789, "flash_point": 13, "octane": 108, "cetane": None},
    "biodiesel": {"density": 880, "flash_point": 130, "octane": None, "cetane": 55},
}


def get_fuel_spec(fuel_name):
    """Return the specification dict for a named fuel type."""
    return FUEL_TYPES.get(fuel_name.lower())


def density_for(fuel_name):
    """Return the standard density for a fuel type in kg/m3."""
    spec = get_fuel_spec(fuel_name)
    if spec is None:
        return None
    return spec["density"]


def flash_point_for(fuel_name):
    """Return the flash point in Celsius for a fuel type."""
    spec = get_fuel_spec(fuel_name)
    if spec is None:
        return None
    return spec["flash_point"]


def all_fuel_names():
    """Return sorted list of all known fuel type names."""
    return sorted(FUEL_TYPES.keys())


def fuels_by_density(ascending=True):
    """Return fuel names sorted by density."""
    pairs = [(name, spec["density"]) for name, spec in FUEL_TYPES.items()]
    pairs.sort(key=lambda p: p[1], reverse=not ascending)
    return [name for name, _ in pairs]


def is_known_fuel(name):
    """Check if a fuel type name is in the lookup table."""
    return name.lower() in FUEL_TYPES


def compare_density(fuel_a, fuel_b):
    """Return the difference in density between two fuels."""
    da = density_for(fuel_a)
    db = density_for(fuel_b)
    if da is None or db is None:
        return None
    return da - db
