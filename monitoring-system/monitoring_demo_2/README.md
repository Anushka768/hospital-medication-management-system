# Hospital Monitoring System | Deliverable 2

Extract the ZIP, open this folder in VS Code, and run `python3 main.py`
in its terminal. Log in as `admin` with the fictional password `Demo123!`.
Python 3.8+ and its standard library are sufficient.

Enter each menu choice separately:

| Choices | Result |
|---|---|
| h → 1 → ADC1 | Connect ADC1 |
| h → 1 → ADC2 | Connect ADC2 |
| h → 2 → ADC1 | Raise and display a simulated security alarm |
| b → displayed alarm ID | Acknowledge the alarm |
| h → 3 → ADC1 | Mark ADC1 unavailable and stale. ADC2 remains available. |
| h → 1 → ADC1 | Restore ADC1 and resolve its communication alarm |
| c | Read event history |
| f → quit | Log out and close the app |

The application creates a local SQLite database on first run. You can select
another file with `python3 main.py --database rehearsal.sqlite3`.

## OOP review

- **Composition:** `main.py` creates the storage, account, communication,
  alarm manager, and monitoring objects and passes them to their callers.
- **Encapsulation:** `Accounts` owns session and permission checks.
  `Storage` owns SQL and returns independent record dictionaries.
- **Abstraction:** `Communication.decode()` converts JSON to an immutable
  `ADCEvent`. Monitoring uses the event fields.
- **Responsibility:** `Monitoring` reacts to cabinet events. `AlarmManager`
  owns alarm rules and asks Storage to save the resulting transitions.

Trace one disconnection from the console through `Monitoring.receive()`.
Identify which object marks the cabinet stale, which decides whether an
alarm already exists, and which saves the record.

This baseline uses explicit simulated link loss. Automatic heartbeat timeouts,
security alarm resolution, and live ADC integration are later features.

## Updating an existing demo

Copy all seven Python files together. The existing demo.sqlite3 schema is compatible. For the module guide, list AlarmManager as the owner of alarm rules and Storage.update_alarm_state() as the persistence operation. Communication.decode() returns an ADCEvent rather than a dictionary.
