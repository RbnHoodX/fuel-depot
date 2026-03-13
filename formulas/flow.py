"""Flow rate calculations for fuel transfers."""

import math


def flow_rate(volume, duration):
    """Calculate flow rate in units per second."""
    if duration <= 0:
        raise ValueError("duration must be positive")
    return volume / duration


def pressure_drop(length, diameter, velocity, friction=0.02):
    """Estimate pressure drop in a pipe using Darcy-Weisbach approximation."""
    if diameter <= 0:
        raise ValueError("diameter must be positive")
    return friction * (length / diameter) * (velocity ** 2) / 2


def reynolds_number(velocity, diameter, viscosity=1e-6):
    """Calculate the Reynolds number for flow characterization."""
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    return velocity * diameter / viscosity


def is_turbulent(velocity, diameter, viscosity=1e-6):
    """Determine if flow is turbulent (Reynolds > 4000)."""
    re = reynolds_number(velocity, diameter, viscosity)
    return re > 4000


def volume_from_cylinder(radius, height):
    """Calculate the volume of a cylindrical tank."""
    if radius < 0 or height < 0:
        raise ValueError("dimensions must be non-negative")
    return math.pi * radius ** 2 * height


def fill_time(volume, rate):
    """Estimate time to fill a given volume at a constant flow rate."""
    if rate <= 0:
        raise ValueError("rate must be positive")
    return volume / rate


def optimal_pipe_diameter(flow_target, max_velocity=3.0):
    """Calculate minimum pipe diameter for a target flow rate."""
    if flow_target <= 0:
        raise ValueError("flow_target must be positive")
    area = flow_target / max_velocity
    return 2 * math.sqrt(area / math.pi)
