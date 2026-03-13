"""String formatting helpers."""


def pad_left(text, width, char=" "):
    """Pad a string on the left to reach the desired width."""
    return text.rjust(width, char)


def pad_right(text, width, char=" "):
    """Pad a string on the right to reach the desired width."""
    return text.ljust(width, char)


def truncate(text, max_length, suffix="..."):
    """Truncate text to max_length, adding suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def title_case(text):
    """Convert text to title case, handling hyphens and underscores."""
    return text.replace("_", " ").replace("-", " ").title()


def slugify(text):
    """Convert text to a URL-safe slug."""
    slug = text.lower().strip()
    slug = slug.replace(" ", "-").replace("_", "-")
    return "".join(c for c in slug if c.isalnum() or c == "-")


def format_units(value, unit="units", decimals=2):
    """Format a numeric value with its unit label."""
    return f"{value:.{decimals}f} {unit}"


def pluralize(word, count):
    """Simple English pluralization."""
    if count == 1:
        return word
    if word.endswith("s") or word.endswith("x") or word.endswith("sh"):
        return word + "es"
    return word + "s"


def join_names(names, conjunction="and"):
    """Join a list of names with commas and a conjunction."""
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} {conjunction} {names[1]}"
    return ", ".join(names[:-1]) + f", {conjunction} {names[-1]}"
