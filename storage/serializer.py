"""Serialize depot objects to portable formats."""

import json


def tank_to_dict(tank):
    """Convert a Tank to a plain dict."""
    return {
        "name": tank.name,
        "kind": tank.kind,
        "fuel_level": tank.fuel_level,
    }


def dispatch_to_dict(dispatch):
    """Convert a Dispatch to a plain dict."""
    return {
        "id": dispatch.id,
        "dest_tank": dispatch.dest_tank.name,
        "source_tank": dispatch.source_tank.name,
        "amount": dispatch.amount,
        "note": dispatch.note,
    }


def depot_to_dict(depot):
    """Convert a full Depot to a nested dict."""
    return {
        "tanks": [tank_to_dict(t) for t in depot.tanks()],
        "dispatches": [dispatch_to_dict(d) for d in depot.log_entries()],
    }


def depot_to_json(depot, indent=2):
    """Serialize a Depot to a JSON string."""
    return json.dumps(depot_to_dict(depot), indent=indent)


def tanks_to_json(tanks, indent=2):
    """Serialize a list of tanks to JSON."""
    return json.dumps([tank_to_dict(t) for t in tanks], indent=indent)


def dispatches_to_json(dispatches, indent=2):
    """Serialize a list of dispatches to JSON."""
    return json.dumps([dispatch_to_dict(d) for d in dispatches], indent=indent)
