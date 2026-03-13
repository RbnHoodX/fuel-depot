"""Aggregation helpers for depot data."""


def total_fuel_in_depot(tanks):
    """Sum fuel levels across all tanks."""
    return sum(t.fuel_level for t in tanks)


def total_dispatched(dispatches):
    """Sum all dispatch amounts."""
    return sum(d.amount for d in dispatches)


def average_dispatch_amount(dispatches):
    """Calculate the average dispatch amount."""
    if not dispatches:
        return 0.0
    return total_dispatched(dispatches) / len(dispatches)


def max_dispatch(dispatches):
    """Return the dispatch with the largest amount, or None."""
    if not dispatches:
        return None
    return max(dispatches, key=lambda d: d.amount)


def min_dispatch(dispatches):
    """Return the dispatch with the smallest amount, or None."""
    if not dispatches:
        return None
    return min(dispatches, key=lambda d: d.amount)


def group_by_source(dispatches):
    """Group dispatches by source tank name."""
    groups = {}
    for d in dispatches:
        name = d.source_tank.name
        groups.setdefault(name, []).append(d)
    return groups


def group_by_dest(dispatches):
    """Group dispatches by destination tank name."""
    groups = {}
    for d in dispatches:
        name = d.dest_tank.name
        groups.setdefault(name, []).append(d)
    return groups


def count_by_tank(dispatches):
    """Count how many dispatches each tank is involved in."""
    counts = {}
    for d in dispatches:
        src = d.source_tank.name
        dst = d.dest_tank.name
        counts[src] = counts.get(src, 0) + 1
        counts[dst] = counts.get(dst, 0) + 1
    return counts


def running_total(dispatches, tank_name):
    """Calculate running fuel balance for a tank across dispatches.

    Returns a list of cumulative totals after each dispatch.
    """
    totals = []
    cumulative = 0
    for d in dispatches:
        if d.dest_tank.name == tank_name:
            cumulative += d.amount
        elif d.source_tank.name == tank_name:
            cumulative -= d.amount
        totals.append(cumulative)
    return totals
