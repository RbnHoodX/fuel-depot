"""Efficiency and loss calculations for fuel operations."""


def transfer_efficiency(delivered, dispatched):
    """Calculate the efficiency of a fuel transfer as a percentage."""
    if dispatched <= 0:
        raise ValueError("dispatched amount must be positive")
    return (delivered / dispatched) * 100


def evaporation_loss(volume, temperature, duration, coefficient=0.001):
    """Estimate fuel lost to evaporation over time."""
    if volume < 0 or temperature < 0 or duration < 0:
        raise ValueError("all values must be non-negative")
    return volume * coefficient * temperature * duration


def pipeline_loss(volume, distance, loss_per_km=0.002):
    """Estimate fuel lost during pipeline transport."""
    if distance < 0:
        raise ValueError("distance must be non-negative")
    return volume * loss_per_km * distance


def net_delivery(gross_amount, loss_amount):
    """Calculate net fuel delivered after accounting for losses."""
    return max(0, gross_amount - loss_amount)


def utilization_rate(used, available):
    """Calculate what fraction of available fuel was used."""
    if available <= 0:
        return 0.0
    return min(1.0, used / available)


def cost_per_unit(total_cost, units_delivered):
    """Calculate the cost per unit of fuel delivered."""
    if units_delivered <= 0:
        raise ValueError("units_delivered must be positive")
    return total_cost / units_delivered


def batch_efficiency(deliveries):
    """Calculate average efficiency across multiple deliveries.

    deliveries: list of (delivered, dispatched) tuples.
    """
    if not deliveries:
        return 0.0
    total_delivered = sum(d for d, _ in deliveries)
    total_dispatched = sum(s for _, s in deliveries)
    if total_dispatched <= 0:
        return 0.0
    return (total_delivered / total_dispatched) * 100
