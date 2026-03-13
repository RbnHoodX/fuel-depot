"""Command-line interface for managing the fuel depot."""

import sys
from depot import Depot


def create_depot_from_args(args):
    """Build a depot from command-line arguments."""
    depot = Depot()
    i = 0
    while i < len(args):
        cmd = args[i]
        if cmd == "--tank":
            name = args[i + 1]
            kind = args[i + 2] if i + 2 < len(args) and not args[i + 2].startswith("--") else "standard"
            depot.create_tank(name, kind)
            i += 3 if kind != "standard" else 2
        elif cmd == "--transfer":
            dest = args[i + 1]
            source = args[i + 2]
            amount = int(args[i + 3])
            depot.transfer(dest, source, amount)
            i += 4
        else:
            i += 1
    return depot


def print_depot_status(depot):
    """Print the current status of all tanks."""
    print("=== Fuel Depot Status ===")
    print(f"Tanks: {len(depot.tanks())}")
    print(f"Dispatches: {len(depot.log_entries())}")
    print()
    for tank in depot.tanks():
        print(f"  {tank.name}: {tank.fuel_level} units ({tank.kind})")
    print()
    total_in, total_out = depot.fuel_summary()
    print(f"Total fuel moved: {total_in} units")


def print_dispatch_log(depot):
    """Print the full dispatch log."""
    print("=== Dispatch Log ===")
    for dispatch in depot.log_entries():
        print(f"  #{dispatch.id}: {dispatch.source_tank.name} -> "
              f"{dispatch.dest_tank.name} ({dispatch.amount} units)")
        if dispatch.note:
            print(f"         note: {dispatch.note}")


def run_interactive(depot):
    """Run a simple interactive session."""
    print("Fuel Depot Interactive Mode")
    print("Commands: status, log, transfer <dest> <source> <amount>, quit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not line:
            continue
        parts = line.split()
        cmd = parts[0].lower()
        if cmd == "quit":
            break
        elif cmd == "status":
            print_depot_status(depot)
        elif cmd == "log":
            print_dispatch_log(depot)
        elif cmd == "transfer" and len(parts) == 4:
            try:
                depot.transfer(parts[1], parts[2], int(parts[3]))
                print("Transfer recorded.")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
        else:
            print("Unknown command.")


def main():
    """Entry point for the CLI."""
    depot = Depot()
    if len(sys.argv) > 1:
        depot = create_depot_from_args(sys.argv[1:])
        print_depot_status(depot)
    else:
        depot.create_tank("main", "standard")
        depot.create_tank("reserve", "reserve")
        depot.create_tank("overflow", "reserve")
        run_interactive(depot)


if __name__ == "__main__":
    main()
