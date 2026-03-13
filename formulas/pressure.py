"""Pressure calculations for the fuel distribution system."""


def hydrostatic_pressure(density, height, gravity=9.81):
    """Calculate hydrostatic pressure at a given depth."""
    if density < 0 or height < 0:
        raise ValueError("density and height must be non-negative")
    return density * gravity * height


def gauge_to_absolute(gauge_pressure, atmospheric=101325):
    """Convert gauge pressure to absolute pressure in Pascals."""
    return gauge_pressure + atmospheric


def absolute_to_gauge(absolute_pressure, atmospheric=101325):
    """Convert absolute pressure to gauge pressure."""
    return absolute_pressure - atmospheric


def pressure_at_depth(surface_pressure, density, depth, gravity=9.81):
    """Calculate total pressure at a given depth below the surface."""
    return surface_pressure + hydrostatic_pressure(density, depth, gravity)


def is_overpressure(current, max_allowed):
    """Check if current pressure exceeds the maximum allowed."""
    return current > max_allowed


def relief_valve_flow(pressure_diff, coefficient=0.61, area=0.01):
    """Estimate flow through a relief valve given pressure differential."""
    if pressure_diff <= 0:
        return 0.0
    return coefficient * area * (2 * pressure_diff) ** 0.5


def tank_bottom_pressure(fuel_level, fuel_density=800):
    """Calculate pressure at the bottom of a tank from fuel level."""
    return hydrostatic_pressure(fuel_density, fuel_level)
