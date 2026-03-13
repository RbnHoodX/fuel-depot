class Tank:
    """A fuel tank that tracks its fuel level from dispatch log entries.

    The fuel level is always computed from dispatches -- never stored directly.
    This guarantees the level is always consistent with the dispatch log.
    """

    def __init__(self, name, kind="standard"):
        self._name = name
        self._kind = kind
        self._dispatches = []

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def fuel_level(self):
        total = 0
        for dispatch in self._dispatches:
            if dispatch.dest_tank is self:
                total += dispatch.amount
            elif dispatch.source_tank is self:
                total -= dispatch.amount
        return total

    def _add_dispatch(self, dispatch):
        self._dispatches.append(dispatch)

    def dispatches(self):
        return list(self._dispatches)

    def __repr__(self):
        return f"Tank(name={self._name!r}, kind={self._kind!r})"
