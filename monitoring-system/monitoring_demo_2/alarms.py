"""Alarm rules shared by the dashboard and incoming ADC events."""


class AlarmManager:
    def __init__(self, storage):
        self._storage = storage

    def unresolved(self):
        return tuple(alarm for alarm in self._storage.alarms()
                     if alarm['state'] != 'RESOLVED')

    def raise_alarm(self, adc, kind, severity):
        for alarm in self.unresolved():
            if alarm['adc'] == adc and alarm['kind'] == kind:
                return alarm['id']
        return self._storage.add_alarm(adc, kind, severity)

    def acknowledge(self, alarm_id, username):
        changed = self._storage.update_alarm_state(
            alarm_id, ('ACTIVE',), 'ACKNOWLEDGED', username
        )
        if not changed:
            raise ValueError('Alarm missing, already acknowledged, or resolved')

    def resolve_communication(self, adc):
        for alarm in self.unresolved():
            if alarm['adc'] == adc and alarm['kind'] == 'communication':
                self._storage.update_alarm_state(
                    alarm['id'], ('ACTIVE', 'ACKNOWLEDGED'), 'RESOLVED'
                )
