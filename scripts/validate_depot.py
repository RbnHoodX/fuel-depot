"""Validate depot integrity by checking invariants."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from depot import Depot


def check_fuel_conservation(depot):
    """Verify that total fuel in equals total fuel out across all dispatches."""
    total_in, total_out = depot.fuel_summary()
    if total_in != total_out:
        return False, f"Mismatch: in={total_in}, out={total_out}"
    return True, "fuel conservation holds"


def check_dispatch_ids_unique(depot):
    """Verify all dispatch IDs are unique."""
    ids = [d.id for d in depot.log_entries()]
    if len(ids) != len(set(ids)):
        return False, "duplicate dispatch IDs found"
    return True, "all dispatch IDs unique"


def check_dispatch_ids_sequential(depot):
    """Verify dispatch IDs are sequential starting from 1."""
    ids = [d.id for d in depot.log_entries()]
    expected = list(range(1, len(ids) + 1))
    if ids != expected:
        return False, f"non-sequential IDs: {ids}"
    return True, "dispatch IDs are sequential"


def check_tank_names_unique(depot):
    """Verify all tank names are unique."""
    names = [t.name for t in depot.tanks()]
    if len(names) != len(set(names)):
        return False, "duplicate tank names found"
    return True, "all tank names unique"


def run_all_checks(depot):
    """Run all validation checks and return results."""
    checks = [
        check_fuel_conservation,
        check_dispatch_ids_unique,
        check_dispatch_ids_sequential,
        check_tank_names_unique,
    ]
    results = []
    for check in checks:
        passed, msg = check(depot)
        results.append((check.__name__, passed, msg))
    return results


if __name__ == "__main__":
    from scripts.seed_data import create_sample_depot

    depot = create_sample_depot()
    for name, passed, msg in run_all_checks(depot):
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {msg}")
