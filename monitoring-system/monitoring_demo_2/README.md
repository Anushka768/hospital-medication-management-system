# Basic Demo 2

A small console prototype based on your partner's User/account functions and letter menus.
It demonstrates an alarm end-to-end, persistent records, and an explicit simulated link failure.
It targets evidence for the demo rubric; it does not implement every D1 requirement or guarantee a grade.

## Run in VS Code on your Mac

1. Extract the ZIP. In VS Code choose File > Open Folder and select monitoring_demo_2_basic.
2. Choose Terminal > New Terminal. Run:

```bash
python3 main.py
```

3. At Username enter `admin`. At Password enter `Demo123!`.
4. Use the letter menu. No third-party Python packages are required.

If the terminal is in the wrong folder, type `cd `, drag the extracted folder into the terminal, press Enter, then run the command above.
Run in the integrated TERMINAL, not the Python Debug Console.

Fictional seeded usernames: admin, technician, pharmacist, nurse, doctor.
All use Demo123! for this classroom demo. Do not use real credentials or patient data.

## Exact demo rehearsal

Each simulator action returns you to the main menu. Enter each item separately.

1. Log in as admin / Demo123!.
2. Enter `h`, then `1`, then `ADC1`: fresh status makes ADC1 AVAILABLE / CURRENT.
3. Enter `h`, then `1`, then `ADC2`: connect the second cabinet.
4. Enter `h`, then `2`, then `ADC1`: receive, save and display a critical security alarm.
5. Enter `b`: view the alarm. Enter its numeric ID to acknowledge it, or press Enter to skip.
   An acknowledged alarm remains visible and its acknowledging user is recorded.
6. Enter `h`, then `3`, then `ADC1`: inject link loss. ADC1 becomes UNAVAILABLE / STALE;
   ADC2 stays AVAILABLE / CURRENT. A communication alarm appears.
7. Enter `h`, then `1`, then `ADC1`: receive fresh simulated status and recover ADC1.
   Its communication alarm is resolved; the independent security alarm remains.
8. Enter `c` to see stored event history.
9. Enter `f` to log out. At Username enter `quit` to close.

To demonstrate persistence, restart and log in again. Alarms and history remain.
Cabinets initially display ABSENT / STALE until fresh simulated status is supplied;
stored status is not treated as proof of a live connection after restart.

## Your partner's contribution retained

- User(name, password, role) remains the account concept and constructor shape.
- auth_user, auth_pass and auth_role remain the account helper names, now methods of Accounts.
- Original a/t/p/n/d role codes and letter-menu layout are retained.
- funcs(role) still chooses an action from the role-specific menu.
- new_user retains the registration prompts and role validation.
- Main-menu ADC, alarms and history selections now perform real prototype operations.

Changes to the original: users are stored in SQLite rather than a shared in-memory list;
passwords are salted hashes rather than public plaintext fields; account creation requires an
administrator; the final-login-attempt bug is fixed. The original script was not overwritten.

## Six application files and their hidden decisions

| File | Responsibility | Secret and anticipated change |
|---|---|---|
| main.py | Construct and connect objects, launch UI | Startup wiring; not claimed as a separate information-hiding policy |
| security.py | User accounts, verification, roles, authorization | Credential representation, account lookup and permission rules |
| communication.py | Decode incoming messages and simulate ADC input | JSON encoding and simulated connection mechanism |
| monitoring.py | Process events and enforce monitoring behaviour | Alarm and cabinet-state policy |
| storage.py | Save and retrieve accounts, cabinets, alarms, events | SQLite schema, queries and storage location |
| ui.py | Input prompts, role menus and presentation | Console layout and wording |

Only storage.py imports SQLite and executes SQL. UI does not read password hashes,
SQL tables or internal account collections. Record reads return independent dictionaries.
Underscore fields are internal by Python convention, not a security boundary against hostile code.

## Brief interfaces for your document

### Accounts in security.py

- User(name, password, role): validate fields and create an internal salted hash; invalid fields raise ValueError.
- auth_user(u) -> bool: whether the username exists; does not expose its record.
- auth_pass(u, p) -> bool: whether the supplied password matches its stored salted hash.
- auth_role(u) -> role code or None: assigned role lookup.
- login(username, password) -> session token: verify credentials and record login; wrong/locked credentials raise PermissionError.
- require(token, action) -> (username, role): authorize an action; otherwise raise PermissionError.
- new_user(token, name, password, role): administrator-only account creation; duplicates/invalid fields raise ValueError.
- logout(token): invalidate the session.

Three consecutive failures block that username for this program run. Sessions and failure counts
are in memory, not persisted. Accounts are persistent. Inactivity timeout and automatic security
alarms for login failures are not implemented in this basic version.

### Communication in communication.py

- decode(raw) -> message: validate JSON, configured cabinet and supported message fields; otherwise ValueError.
- simulate(action, adc) -> encoded message: connect, alarm or disconnect a fictional cabinet.
  Unknown actions/cabinets raise ValueError. An alarm on a disconnected link raises ConnectionError.

### Monitoring in monitoring.py

- receive(raw): decode and apply trusted ADC input; record the event. Invalid messages are logged and rejected.
- simulate(token, action, adc): require simulator permission and pass its encoded message through receive.
- dashboard(token) -> cabinet records: require view permission; return independent records.
- alarms(token) -> unresolved alarm records: require view permission.
- acknowledge(token, alarm_id): require acknowledgement permission; update and audit an active alarm.
  Missing, acknowledged or resolved targets raise ValueError.
- history(token) -> event records: administrator-only query.

### Storage in storage.py

- find_user(name), add_user(name, salt, password_hash, role): persistent account access for Accounts.
- cabinets(), set_status(adc, status, stale): cabinet records and updates.
- add_alarm(adc, kind, severity), alarms(): persistent alarm insertion and retrieval.
- acknowledge(alarm_id, username) -> bool: update an active alarm, returning whether a row changed.
- resolve_communication(adc): resolve outstanding communication alarms after fresh status.
- record_event(description), history(): append and retrieve history.
- close(): close the database connection.

The database is demo.sqlite3 next to main.py. SQL uses parameters, not concatenated user input.
Audit modification/deletion is not offered through normal UI operations. Database tamper resistance,
encryption and transactional recovery across a multi-step workflow are not demonstrated.

### Presentation in ui.py

- funcs(role) -> action: prompt using the partner's role-specific letter menu.
- new_user(new, accounts, token) -> 0/1: prompt and request authorized registration; invalid yes/no returns 0.
- Console.run(): run login and menus; show operation errors without terminating normal interaction.

## External ADC interface and scope

Requires: configured ADC identity and status/alarm information.
Provides: validation, monitoring state, stored alarms/events and display through the operator UI.
The simulator generates a fresh status event, a critical security alarm or an explicit link-lost event.
No real ADC partner protocol, network transport or remote acknowledgement is implemented.

When the simulated ADC is unavailable, last-known information is marked stale and the cabinet
unavailable; another cabinet remains usable. Reconnection supplies fresh status before recovery.
The link-lost event is explicit: this version does NOT detect silent failure by a heartbeat timeout.

## Not implemented

Inventory, report generation, notification delivery, a hospital map, real ADC communication,
message ordering/deduplication by external event ID, inactivity lock, and automatic login-failure
security alarms. Report and inventory menu entries are labelled not implemented. Avoid claiming
these are complete in your report or demo. The same-condition alarm insertion avoids duplicate
unresolved alarms; this is not full protocol replay handling.

## What to say for the rubric

- Modularity: open security.py, communication.py, monitoring.py, storage.py and ui.py;
  name each hidden decision using the table above. Do not call main.py a hidden policy.
- Interfaces: show a UI call to Monitoring and Monitoring's call to Storage; point to permission
  enforcement below the UI. No UI SQL or password-field access.
- Running solution: demonstrate the alarm, then link failure, isolation and recovery.
- Change drill: a different wire encoding changes Communication.decode/simulate; a new
  database schema changes Storage; a new role permission changes Accounts' permission policy.
  Update the associated document/traceability entry and rerun the relevant scenario.
- Individual understanding: both partners should trace one simulator action from UI through
  Communication, Monitoring, Storage and back to the displayed result.

## Tests

```bash
python3 -m unittest -v
```

Five tests cover alarm persistence/acknowledgement, link-loss isolation/recovery, account
persistence/hash/permissions, final allowed login/invalid messages, and the complete console flow.

To rehearse with a separate fresh database without removing prior records:

```bash
python3 main.py --database rehearsal.sqlite3
```
