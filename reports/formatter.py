"""Format depot data into human-readable strings."""


def format_tank_row(name, fuel_level, kind):
    """Format a single tank status line."""
    return f"  {name:<20} {fuel_level:>10.2f} units  ({kind})"


def format_dispatch_row(dispatch_id, source, dest, amount, note=""):
    """Format a single dispatch log line."""
    line = f"  #{dispatch_id:<5} {source} -> {dest}  ({amount} units)"
    if note:
        line += f"  [{note}]"
    return line


def format_header(title, width=60):
    """Format a section header with dividers."""
    return f"{'=' * width}\n  {title}\n{'=' * width}"


def format_summary(total_in, total_out, tank_count):
    """Format the depot summary block."""
    lines = [
        f"Tanks:      {tank_count}",
        f"Total in:   {total_in:.2f} units",
        f"Total out:  {total_out:.2f} units",
        f"Net:        {total_in - total_out:.2f} units",
    ]
    return "\n".join(lines)


def format_percentage(value, decimals=1):
    """Format a number as a percentage string."""
    return f"{value:.{decimals}f}%"


def format_fuel_level_bar(level, max_level, width=40):
    """Create an ASCII bar chart for fuel level."""
    if max_level <= 0:
        return "[" + " " * width + "]"
    filled = int((level / max_level) * width)
    filled = min(filled, width)
    return "[" + "#" * filled + " " * (width - filled) + "]"


def indent_block(text, spaces=4):
    """Indent every line of a text block."""
    prefix = " " * spaces
    return "\n".join(prefix + line for line in text.split("\n"))
