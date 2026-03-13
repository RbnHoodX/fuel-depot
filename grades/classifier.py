"""Classify fuel samples by quality and composition."""


OCTANE_GRADES = {
    "regular": (85, 89),
    "midgrade": (90, 93),
    "premium": (94, 98),
    "racing": (99, 110),
}

VISCOSITY_BANDS = {
    "thin": (0.0, 2.0),
    "light": (2.0, 5.0),
    "medium": (5.0, 10.0),
    "heavy": (10.0, 25.0),
    "thick": (25.0, 100.0),
}


def octane_grade(rating):
    """Return the grade name for a given octane rating."""
    if not isinstance(rating, (int, float)):
        return "unknown"
    for grade, (low, high) in OCTANE_GRADES.items():
        if low <= rating <= high:
            return grade
    return "unknown"


def viscosity_band(value):
    """Return the viscosity classification for a given measurement."""
    if not isinstance(value, (int, float)):
        return "unclassed"
    for band, (low, high) in VISCOSITY_BANDS.items():
        if low <= value < high:
            return band
    return "unclassed"


def sulfur_level(ppm):
    """Classify sulfur content by parts-per-million."""
    if not isinstance(ppm, (int, float)) or ppm < 0:
        return "invalid"
    if ppm <= 10:
        return "ultra-low"
    if ppm <= 50:
        return "low"
    if ppm <= 500:
        return "regular"
    return "high"


def cetane_quality(number):
    """Rate diesel fuel quality by cetane number."""
    if not isinstance(number, (int, float)):
        return "unknown"
    if number < 40:
        return "poor"
    if number < 45:
        return "acceptable"
    if number < 55:
        return "good"
    return "excellent"


def flash_point_safety(temp_c):
    """Classify fuel safety by flash point temperature in Celsius."""
    if not isinstance(temp_c, (int, float)):
        return "unknown"
    if temp_c < 23:
        return "extremely_flammable"
    if temp_c < 60:
        return "flammable"
    if temp_c < 93:
        return "combustible"
    return "non_flammable"


def water_content_rating(percent):
    """Rate water contamination level in fuel."""
    if not isinstance(percent, (int, float)) or percent < 0:
        return "invalid"
    if percent <= 0.02:
        return "dry"
    if percent <= 0.05:
        return "acceptable"
    if percent <= 0.1:
        return "marginal"
    return "contaminated"
