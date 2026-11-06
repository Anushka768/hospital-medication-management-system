"""Coordinate cabinet status, authorization and alarm rules."""
from alarms import AlarmManager


class Monitoring:
    def __init__(self, storage, accounts, communication, alarms=None):
        self._storage = storage
        self._accounts = accounts
        self._communication = communication
        self._alarms = alarms if alarms is not None else AlarmManager(storage)
        # Saved records remain, but no live status is assumed after a restart.
        for cabinet in storage.cabinets():
            storage.set_status(cabinet['adc'], 'ABSENT', True)

    def receive(self, raw):
        """Trusted ADC input boundary; independent of an operator's login."""
        try:
            message = self._communication.decode(raw)
        except ValueError:
            self._storage.record_event('Rejected invalid ADC message')
            raise
        adc, kind = message.adc, message.kind
        if kind == 'status':
            self._storage.set_status(adc, 'AVAILABLE', False)
            self._alarms.resolve_communication(adc)
        elif kind == 'link_lost':
            self._storage.set_status(adc, 'UNAVAILABLE', True)
            self._alarms.raise_alarm(adc, 'communication', 'CRITICAL')
        else:
            self._alarms.raise_alarm(adc, message.alarm_type, message.severity)
        self._storage.record_event(adc + ': ' + kind)

    def simulate(self, token, action, adc):
        self._accounts.require(token, 'simulate')
        self.receive(self._communication.simulate(action, adc))

    def dashboard(self, token):
        self._accounts.require(token, 'view')
        return self._storage.cabinets()

    def alarms(self, token):
        self._accounts.require(token, 'view')
        return self._alarms.unresolved()

    def acknowledge(self, token, alarm_id):
        username, _ = self._accounts.require(token, 'ack')
        self._alarms.acknowledge(alarm_id, username)
        self._storage.record_event('Alarm ' + str(alarm_id) + ' acknowledged by ' + username)

    def history(self, token):
        self._accounts.require(token, 'history')
        return self._storage.history()
