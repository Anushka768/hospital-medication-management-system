"""STORAGE MODULE. Secret: SQLite tables, queries and database location.
No other module imports sqlite3 or runs SQL. Reads return independent records.
"""
import sqlite3
from datetime import datetime

class Storage:
    def __init__(self, path):
        self._db = sqlite3.connect(path)
        self._db.row_factory = sqlite3.Row
        self._db.executescript('''
        CREATE TABLE IF NOT EXISTS users
          (name TEXT PRIMARY KEY, salt TEXT, password_hash TEXT, role TEXT);
        CREATE TABLE IF NOT EXISTS cabinets
          (adc TEXT PRIMARY KEY, location TEXT, status TEXT, stale INTEGER);
        CREATE TABLE IF NOT EXISTS alarms
          (id INTEGER PRIMARY KEY, adc TEXT, kind TEXT, severity TEXT,
           raised_at TEXT, state TEXT, acknowledged_by TEXT);
        CREATE TABLE IF NOT EXISTS events
          (id INTEGER PRIMARY KEY, at TEXT, description TEXT);
        ''')
        for adc, location in [('ADC1', 'Floor 1 East'), ('ADC2', 'Floor 2 West')]:
            self._db.execute('INSERT OR IGNORE INTO cabinets VALUES (?,?,?,?)', (adc, location, 'ABSENT', 1))
        self._db.commit()

    def find_user(self, name):
        row = self._db.execute('SELECT * FROM users WHERE name=?', (name,)).fetchone()
        return dict(row) if row else None

    def add_user(self, name, salt, password_hash, role):
        try:
            with self._db:
                self._db.execute('INSERT INTO users VALUES (?,?,?,?)', (name, salt, password_hash, role))
        except sqlite3.IntegrityError as exc:
            raise ValueError('Username already exists') from exc

    def cabinets(self):
        return tuple(dict(row) for row in self._db.execute('SELECT * FROM cabinets ORDER BY adc'))

    def set_status(self, adc, status, stale):
        with self._db:
            changed = self._db.execute('UPDATE cabinets SET status=?,stale=? WHERE adc=?', (status, int(stale), adc)).rowcount
        if not changed:
            raise ValueError('Unknown ADC')

    def add_alarm(self, adc, kind, severity):
        with self._db:
            cursor = self._db.execute('INSERT INTO alarms(adc,kind,severity,raised_at,state) VALUES (?,?,?,?,?)',
                                      (adc, kind, severity, datetime.now().astimezone().isoformat(timespec='seconds'), 'ACTIVE'))
        return cursor.lastrowid

    def alarms(self):
        return tuple(dict(row) for row in self._db.execute('SELECT * FROM alarms ORDER BY id'))

    def update_alarm_state(self, alarm_id, expected_states, state, username=None):
        """Save a transition only if the stored state still matches."""
        placeholders = ', '.join('?' for _ in expected_states)
        with self._db:
            cursor = self._db.execute(
                "UPDATE alarms SET state=?, acknowledged_by=COALESCE(?, acknowledged_by) "
                f"WHERE id=? AND state IN ({placeholders})",
                (state, username, alarm_id, *expected_states),
            )
        return cursor.rowcount == 1

    def record_event(self, description):
        with self._db:
            self._db.execute('INSERT INTO events(at,description) VALUES (?,?)',
                             (datetime.now().astimezone().isoformat(timespec='seconds'), description))

    def history(self):
        return tuple(dict(row) for row in self._db.execute('SELECT * FROM events ORDER BY id'))

    def close(self):
        self._db.close()
