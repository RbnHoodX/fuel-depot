"""Seed a depot with sample data for testing and demos."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from depot import Depot


def create_sample_depot():
    """Create a depot with sample tanks and transfers."""
    depot = Depot()
    depot.create_tank("main-storage", "standard")
    depot.create_tank("reserve-a", "reserve")
    depot.create_tank("reserve-b", "reserve")
    depot.create_tank("overflow", "standard")
    depot.create_tank("processing", "standard")

    depot.transfer("main-storage", "reserve-a", 500, "initial fill")
    depot.transfer("main-storage", "reserve-b", 300, "initial fill")
    depot.transfer("processing", "main-storage", 200, "refining batch")
    depot.transfer("overflow", "main-storage", 100, "excess")
    depot.transfer("reserve-a", "processing", 150, "return")

    return depot


def print_seed_summary(depot):
    """Print summary of seeded data."""
    print(f"Created {len(depot.tanks())} tanks")
    print(f"Recorded {len(depot.log_entries())} dispatches")
    for tank in depot.tanks():
        print(f"  {tank.name}: {tank.fuel_level} units")


if __name__ == "__main__":
    d = create_sample_depot()
    print_seed_summary(d)
