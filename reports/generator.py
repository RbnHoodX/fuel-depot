"""Generate structured reports from depot data."""


def tank_status_report(tanks):
    """Generate a list of tank status dicts.

    Each dict has keys: name, kind, fuel_level, dispatch_count.
    """
    report = []
    for tank in tanks:
        report.append({
            "name": tank.name,
            "kind": tank.kind,
            "fuel_level": tank.fuel_level,
            "dispatch_count": len(tank.dispatches()),
        })
    return report


def dispatch_summary_report(dispatches):
    """Summarize dispatches by source and destination.

    Returns a dict mapping (source_name, dest_name) to total amount.
    """
    summary = {}
    for d in dispatches:
        key = (d.source_tank.name, d.dest_tank.name)
        summary[key] = summary.get(key, 0) + d.amount
    return summary


def top_receivers(dispatches, limit=5):
    """Find tanks that received the most fuel.

    Returns a list of (tank_name, total_received) sorted descending.
    """
    totals = {}
    for d in dispatches:
        name = d.dest_tank.name
        totals[name] = totals.get(name, 0) + d.amount
    ranked = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return ranked[:limit]


def top_senders(dispatches, limit=5):
    """Find tanks that sent the most fuel.

    Returns a list of (tank_name, total_sent) sorted descending.
    """
    totals = {}
    for d in dispatches:
        name = d.source_tank.name
        totals[name] = totals.get(name, 0) + d.amount
    ranked = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return ranked[:limit]


def daily_volume_breakdown(dispatches, date_extractor=None):
    """Group dispatch amounts by date.

    If no date_extractor is provided, groups all into a single bucket.
    """
    if date_extractor is None:
        total = sum(d.amount for d in dispatches)
        return {"all": total}
    buckets = {}
    for d in dispatches:
        key = date_extractor(d)
        buckets[key] = buckets.get(key, 0) + d.amount
    return buckets


def idle_tanks(tanks):
    """Return tanks with no dispatches."""
    return [t for t in tanks if len(t.dispatches()) == 0]
