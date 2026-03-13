"""Industry standards and compliance checks for fuel quality."""


ASTM_LIMITS = {
    "diesel_sulfur_ppm": 15,
    "gasoline_sulfur_ppm": 10,
    "diesel_cetane_min": 40,
    "gasoline_octane_min": 87,
    "max_water_percent": 0.05,
    "max_sediment_percent": 0.01,
}

EPA_TIERS = {
    "tier1": {"sulfur_max": 30, "benzene_max": 1.0},
    "tier2": {"sulfur_max": 30, "benzene_max": 0.62},
    "tier3": {"sulfur_max": 10, "benzene_max": 0.62},
}


def meets_sulfur_standard(ppm, fuel_type="diesel"):
    """Check if sulfur content meets ASTM limits."""
    key = f"{fuel_type}_sulfur_ppm"
    limit = ASTM_LIMITS.get(key)
    if limit is None:
        return None
    return ppm <= limit


def meets_cetane_standard(cetane_number):
    """Check if cetane number meets the ASTM minimum."""
    return cetane_number >= ASTM_LIMITS["diesel_cetane_min"]


def meets_octane_standard(octane_rating):
    """Check if octane rating meets the ASTM minimum."""
    return octane_rating >= ASTM_LIMITS["gasoline_octane_min"]


def water_within_limits(percent):
    """Check if water content is within acceptable limits."""
    return percent <= ASTM_LIMITS["max_water_percent"]


def sediment_within_limits(percent):
    """Check if sediment content is within acceptable limits."""
    return percent <= ASTM_LIMITS["max_sediment_percent"]


def epa_tier_compliance(sulfur_ppm, benzene_percent):
    """Return the highest EPA tier met by the given measurements."""
    for tier in ["tier3", "tier2", "tier1"]:
        limits = EPA_TIERS[tier]
        if sulfur_ppm <= limits["sulfur_max"] and benzene_percent <= limits["benzene_max"]:
            return tier
    return "non_compliant"


def full_compliance_check(sulfur_ppm, cetane, water_pct, sediment_pct):
    """Run all diesel compliance checks and return a results dict."""
    return {
        "sulfur": meets_sulfur_standard(sulfur_ppm, "diesel"),
        "cetane": meets_cetane_standard(cetane),
        "water": water_within_limits(water_pct),
        "sediment": sediment_within_limits(sediment_pct),
    }
