from tank import Tank
from dispatch import Dispatch, DispatchLog


class Depot:
    """Fuel depot managing tanks and fuel dispatches."""

    def __init__(self):
        self._tanks = {}
        self._log = DispatchLog()

    def create_tank(self, name, kind="standard"):
        if name in self._tanks:
            raise ValueError(f"tank {name!r} already exists")
        tank = Tank(name, kind)
        self._tanks[name] = tank
        return tank

    def get_tank(self, name):
        return self._tanks[name]

    def tanks(self):
        return list(self._tanks.values())

    def transfer(self, dest_name, source_name, amount, note=""):
        if amount <= 0:
            raise ValueError("amount must be positive")
        dest_tank = self._tanks[dest_name]
        source_tank = self._tanks[source_name]
        dispatch = Dispatch(dest_tank, source_tank, amount, note)
        self._log.record(dispatch)
        return dispatch

    def log_entries(self):
        return self._log.dispatches()

    def fuel_summary(self):
        total_in = 0
        total_out = 0
        for dispatch in self._log.dispatches():
            total_in += dispatch.amount
            total_out += dispatch.amount
        return total_in, total_out
