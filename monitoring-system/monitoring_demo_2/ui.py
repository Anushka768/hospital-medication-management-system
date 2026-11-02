"""PRESENTATION MODULE. Secret: console menu wording and layout.
Letter menus and registration flow adapted from the partner's original funcs/new_user.
No SQL, password comparisons or mutable account records are exposed here.
"""
def funcs(role):
    if role in ('d', 'n'):
        text = 'a) View ADC info\nb) Exit'
        actions = {'a': 'ADC', 'b': 'Exit'}
    elif role == 't':
        text = 'a) View ADC info\nb) Alarms\nc) Exit\nd) ADC simulator'
        actions = {'a': 'ADC', 'b': 'Alarms', 'c': 'Exit', 'd': 'Sim'}
    elif role == 'p':
        text = 'a) View ADC info\nb) Hospital Inventory [not implemented]\nc) Exit'
        actions = {'a': 'ADC', 'b': 'Planned', 'c': 'Exit'}
    else:
        text = ('a) View ADC info\nb) Alarms\nc) History\nd) Generate report [not implemented]\n'
                'e) Hospital Inventory [not implemented]\nf) Exit\ng) Create new user\nh) ADC simulator')
        actions = {'a': 'ADC', 'b': 'Alarms', 'c': 'History', 'd': 'Planned',
                   'e': 'Planned', 'f': 'Exit', 'g': 'NewUser', 'h': 'Sim'}
    print('\nChoose a function.\n' + text)
    return actions.get(input('Choice: ').strip().lower(), 'None')


def new_user(new, accounts, token):
    if new.lower() == 'n':
        return 1
    if new.lower() != 'y':
        return 0
    accounts.require(token, 'create')
    username = input('Select a Username: ').strip()
    password = input('Select a password: ')
    role = input('admin(a), technician(t), pharmacist(p), nurse(n), doctor(d): ').strip().lower()
    while role not in ('a', 't', 'p', 'n', 'd'):
        role = input('Enter a, t, p, n or d: ').strip().lower()
    accounts.new_user(token, username, password, role)
    print('Account saved. Password stored as a salted hash.')
    return 1

class Console:
    def __init__(self, accounts, monitoring):
        self._accounts, self._monitoring = accounts, monitoring

    def _dashboard(self, token):
        print('\nCABINETS - SIMULATED INPUT')
        for c in self._monitoring.dashboard(token):
            print(c['adc'], '|', c['location'], '|', c['status'], '|', 'STALE' if c['stale'] else 'CURRENT')

    def _alarms(self, token):
        locations = {c['adc']: c['location'] for c in self._monitoring.dashboard(token)}
        print('\nUNRESOLVED ALARMS (acknowledgement does not remove the condition)')
        alarms = self._monitoring.alarms(token)
        if not alarms:
            print('None')
        for a in alarms:
            print(a['id'], '|', a['adc'], '|', locations[a['adc']], '|', a['kind'], '|', a['severity'], '|',
                  a['raised_at'], '|', a['state'], '| acknowledged by:', a['acknowledged_by'] or '-')

    def _simulate(self, token):
        self._accounts.require(token, 'simulate')
        print('\nSIMULATOR: 1) Connect/recover  2) Raise critical alarm  3) Disconnect  4) Back')
        action = input('Simulation: ').strip()
        if action == '4':
            return
        if action not in ('1', '2', '3'):
            raise ValueError('Choose 1, 2, 3 or 4')
        adc = input('ADC ID [ADC1]: ').strip().upper() or 'ADC1'
        self._monitoring.simulate(token, {'1': 'connect', '2': 'alarm', '3': 'disconnect'}[action], adc)
        self._dashboard(token)
        self._alarms(token)

    def run(self):
        print('BASIC DEMO 2 - partner login/menu design plus alarm and link-failure simulation')
        print('Fictional accounts: admin / technician / pharmacist / nurse / doctor')
        print('Password for each: Demo123!  (use only fictional demonstration data)')
        print('New accounts: log in as admin, then select g. Enter quit at Username to close.')
        try:
            while True:
                username = input('\nUsername: ').strip()
                if username.lower() == 'quit':
                    return
                try:
                    token = self._accounts.login(username, input('Password: '))
                except PermissionError as exc:
                    print('Rejected:', exc)
                    continue
                _, role = self._accounts.require(token, 'view')
                print('Login successful.')
                while True:
                    action = funcs(role)
                    try:
                        if action == 'Exit':
                            self._accounts.logout(token)
                            print('Logged out.')
                            break
                        if action == 'ADC':
                            self._dashboard(token)
                        elif action == 'Alarms':
                            self._alarms(token)
                            value = input('Alarm ID to acknowledge (Enter to skip): ').strip()
                            if value:
                                self._monitoring.acknowledge(token, int(value))
                                self._alarms(token)
                        elif action == 'History':
                            for event in self._monitoring.history(token):
                                print(event['at'], '|', event['description'])
                        elif action == 'NewUser':
                            new_user('y', self._accounts, token)
                        elif action == 'Sim':
                            self._simulate(token)
                        elif action == 'Planned':
                            print('Not implemented in this basic prototype.')
                        else:
                            print('Please input the letter next to the desired function.')
                    except (ValueError, PermissionError, ConnectionError) as exc:
                        print('Rejected:', exc)
        except (EOFError, KeyboardInterrupt):
            print('\nExiting')
