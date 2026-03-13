"""Statistical calculations for depot reporting."""

import math


def mean(values):
    """Calculate the arithmetic mean."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def median(values):
    """Calculate the median of a list of numbers."""
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def variance(values):
    """Calculate population variance."""
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return sum((x - avg) ** 2 for x in values) / len(values)


def std_dev(values):
    """Calculate population standard deviation."""
    return math.sqrt(variance(values))


def percentile(values, pct):
    """Calculate the given percentile (0-100) using linear interpolation."""
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    k = (pct / 100) * (len(sorted_vals) - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[int(k)]
    return sorted_vals[f] * (c - k) + sorted_vals[c] * (k - f)


def dispatch_amount_stats(dispatches):
    """Return basic stats for dispatch amounts."""
    amounts = [d.amount for d in dispatches]
    if not amounts:
        return {"count": 0, "mean": 0, "median": 0, "std_dev": 0, "min": 0, "max": 0}
    return {
        "count": len(amounts),
        "mean": round(mean(amounts), 2),
        "median": round(median(amounts), 2),
        "std_dev": round(std_dev(amounts), 2),
        "min": min(amounts),
        "max": max(amounts),
    }


def fuel_level_distribution(tanks):
    """Return a dict summarizing fuel levels across tanks."""
    levels = [t.fuel_level for t in tanks]
    if not levels:
        return {"count": 0, "total": 0, "mean": 0, "min": 0, "max": 0}
    return {
        "count": len(levels),
        "total": sum(levels),
        "mean": round(mean(levels), 2),
        "min": min(levels),
        "max": max(levels),
    }
