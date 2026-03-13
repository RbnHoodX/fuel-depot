class Dispatch:
    """A fuel movement entry linking two tanks."""

    def __init__(self, dest_tank, source_tank, amount, note=""):
        self._id = 0
        self._dest_tank = dest_tank
        self._source_tank = source_tank
        self._amount = amount
        self._note = note

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def dest_tank(self):
        return self._dest_tank

    @property
    def source_tank(self):
        return self._source_tank

    @property
    def amount(self):
        return self._amount

    @property
    def note(self):
        return self._note

    def __repr__(self):
        return (f"Dispatch(id={self._id}, dest={self._dest_tank.name!r}, "
                f"source={self._source_tank.name!r}, amount={self._amount})")


class DispatchLog:
    """Append-only log of fuel dispatch records."""

    def __init__(self):
        self._dispatches = []
        self._counter = 0

    def record(self, dispatch):
        self._counter += 1
        dispatch.id = self._counter
        self._dispatches.append(dispatch)
        dispatch.dest_tank._add_dispatch(dispatch)
        dispatch.source_tank._add_dispatch(dispatch)
        return dispatch

    def dispatches(self):
        return list(self._dispatches)
