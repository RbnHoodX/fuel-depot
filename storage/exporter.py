"""Export depot data to various text formats."""

import csv
import io


def tanks_to_csv(tanks):
    """Export tanks to CSV format string."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["name", "kind", "fuel_level"])
    for tank in tanks:
        writer.writerow([tank.name, tank.kind, tank.fuel_level])
    return output.getvalue()


def dispatches_to_csv(dispatches):
    """Export dispatches to CSV format string."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "source", "dest", "amount", "note"])
    for d in dispatches:
        writer.writerow([d.id, d.source_tank.name, d.dest_tank.name, d.amount, d.note])
    return output.getvalue()


def tanks_to_tsv(tanks):
    """Export tanks to tab-separated format."""
    lines = ["name\tkind\tfuel_level"]
    for tank in tanks:
        lines.append(f"{tank.name}\t{tank.kind}\t{tank.fuel_level}")
    return "\n".join(lines)


def depot_to_text(depot):
    """Export a plain-text summary of the depot."""
    lines = ["Fuel Depot Export", ""]
    lines.append(f"Tanks ({len(depot.tanks())}):")
    for tank in depot.tanks():
        lines.append(f"  {tank.name} ({tank.kind}): {tank.fuel_level} units")
    lines.append("")
    entries = depot.log_entries()
    lines.append(f"Dispatches ({len(entries)}):")
    for d in entries:
        lines.append(f"  #{d.id}: {d.source_tank.name} -> {d.dest_tank.name} ({d.amount} units)")
    return "\n".join(lines)


def fuel_levels_to_text(tanks):
    """Export just fuel levels as a simple text listing."""
    lines = []
    for tank in tanks:
        lines.append(f"{tank.name}: {tank.fuel_level}")
    return "\n".join(lines)
