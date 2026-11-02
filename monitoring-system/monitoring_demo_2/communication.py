"""COMMUNICATION MODULE. Secret: JSON message format and simulated link state.
Only this module knows the wire encoding. No real network transport is included.
"""
import json

class Communication:
    def __init__(self, adc_ids):
        self._connected = {adc: False for adc in adc_ids}

    def decode(self, raw):
        try:
            message = json.loads(raw)
            if not isinstance(message, dict) or message['adc'] not in self._connected:
                raise ValueError('Unknown ADC or invalid message')
            if message['kind'] not in ('status', 'alarm', 'link_lost'):
                raise ValueError('Unknown message type')
            if message['kind'] == 'alarm':
                if message.get('alarm_type') != 'security' or message.get('severity') != 'CRITICAL':
                    raise ValueError('Invalid demo alarm')
            return dict(message)
        except (KeyError, TypeError, json.JSONDecodeError) as exc:
            raise ValueError('Malformed ADC message') from exc

    def simulate(self, action, adc):
        if adc not in self._connected:
            raise ValueError('Unknown ADC')
        if action == 'connect':
            self._connected[adc] = True
            message = dict(adc=adc, kind='status')
        elif action == 'disconnect':
            self._connected[adc] = False
            message = dict(adc=adc, kind='link_lost')
        elif action == 'alarm':
            if not self._connected[adc]:
                raise ConnectionError('ADC link is disconnected; connect it first')
            message = dict(adc=adc, kind='alarm', alarm_type='security', severity='CRITICAL')
        else:
            raise ValueError('Unknown simulation action')
        return json.dumps(message)
