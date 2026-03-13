"""Search and filtering helpers for depot collections."""


def find_tanks_by_kind(tanks, kind):
    """Return tanks matching the given kind."""
    return [t for t in tanks if t.kind == kind]


def find_tanks_with_fuel(tanks):
    """Return tanks that have a positive fuel level."""
    return [t for t in tanks if t.fuel_level > 0]


def find_empty_tanks(tanks):
    """Return tanks with zero or negative fuel level."""
    return [t for t in tanks if t.fuel_level <= 0]


def find_tank_by_name(tanks, name):
    """Find a single tank by exact name match."""
    for tank in tanks:
        if tank.name == name:
            return tank
    return None


def search_tanks_by_prefix(tanks, prefix):
    """Return tanks whose names start with the given prefix."""
    return [t for t in tanks if t.name.startswith(prefix)]


def filter_dispatches_by_amount(dispatches, min_amount=0, max_amount=None):
    """Filter dispatches within an amount range."""
    results = []
    for d in dispatches:
        if d.amount >= min_amount:
            if max_amount is None or d.amount <= max_amount:
                results.append(d)
    return results


def dispatches_involving(dispatches, tank_name):
    """Return dispatches where the named tank is source or dest."""
    return [
        d for d in dispatches
        if d.source_tank.name == tank_name or d.dest_tank.name == tank_name
    ]


def dispatches_from(dispatches, tank_name):
    """Return dispatches sent from the named tank."""
    return [d for d in dispatches if d.source_tank.name == tank_name]


def dispatches_to(dispatches, tank_name):
    """Return dispatches received by the named tank."""
    return [d for d in dispatches if d.dest_tank.name == tank_name]
