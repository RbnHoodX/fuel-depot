"""Load depot data from serialized formats."""

import json


def load_json(text):
    """Parse a JSON string into a Python object."""
    return json.loads(text)


def extract_tank_names(data):
    """Extract tank names from a serialized depot dict."""
    tanks = data.get("tanks", [])
    return [t["name"] for t in tanks]


def extract_dispatch_count(data):
    """Count dispatches in a serialized depot dict."""
    return len(data.get("dispatches", []))


def extract_total_amount(data):
    """Sum all dispatch amounts from a serialized depot dict."""
    dispatches = data.get("dispatches", [])
    return sum(d.get("amount", 0) for d in dispatches)


def validate_depot_data(data):
    """Validate the structure of a serialized depot dict.

    Returns a list of error strings (empty if valid).
    """
    errors = []
    if "tanks" not in data:
        errors.append("missing 'tanks' key")
    elif not isinstance(data["tanks"], list):
        errors.append("'tanks' must be a list")

    if "dispatches" not in data:
        errors.append("missing 'dispatches' key")
    elif not isinstance(data["dispatches"], list):
        errors.append("'dispatches' must be a list")

    if "tanks" in data and isinstance(data["tanks"], list):
        for i, tank in enumerate(data["tanks"]):
            if "name" not in tank:
                errors.append(f"tank at index {i} missing 'name'")
            if "kind" not in tank:
                errors.append(f"tank at index {i} missing 'kind'")

    return errors


def rebuild_tank_map(data):
    """Build a name-to-spec dict from serialized tank data."""
    result = {}
    for tank in data.get("tanks", []):
        name = tank.get("name")
        if name:
            result[name] = {
                "kind": tank.get("kind", "standard"),
                "fuel_level": tank.get("fuel_level", 0),
            }
    return result
