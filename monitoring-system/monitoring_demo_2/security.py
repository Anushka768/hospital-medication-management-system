"""ACCOUNT MODULE. Adapted from the partner's User/auth_user/auth_pass/auth_role.
Secret: credential representation, account lookup and role permission policy.
Console prompts are in ui.py. Database tables are hidden by Storage.
"""
import hashlib
import hmac
import secrets

class User:
    # Same constructor idea as the partner's original User(name, password, role).
    def __init__(self, name, password, role):
        if not name.strip() or not password or role not in ('a', 't', 'p', 'n', 'd'):
            raise ValueError('Supply a username, password and valid role a/t/p/n/d')
        self._name = name.strip()
        self._role = role
        self._salt = secrets.token_hex(16)
        self._password_hash = self._hash(password, self._salt)

    @staticmethod
    def _hash(password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 100_000).hex()

class Accounts:
    def __init__(self, storage):
        self._storage = storage
        self._sessions = {}
        self._failures = {}
        self._permissions = {'a': {'view', 'ack', 'history', 'simulate', 'create'},
                             't': {'view', 'ack', 'simulate'},
                             'p': {'view'}, 'n': {'view'}, 'd': {'view'}}
        for name, role in [('admin','a'), ('technician','t'), ('pharmacist','p'), ('nurse','n'), ('doctor','d')]:
            if not self.auth_user(name):
                self._save(User(name, 'Demo123!', role))

    def _save(self, user):
        self._storage.add_user(user._name, user._salt, user._password_hash, user._role)

    def auth_user(self, u):
        """Original username lookup purpose; returns bool, not the account record."""
        return self._storage.find_user(u) is not None

    def auth_pass(self, u, p):
        """Original password-check purpose, adapted to a salted hash."""
        record = self._storage.find_user(u)
        return record is not None and hmac.compare_digest(User._hash(p, record['salt']), record['password_hash'])

    def auth_role(self, u):
        """Original a/t/p/n/d role lookup."""
        record = self._storage.find_user(u)
        return record['role'] if record else None

    def login(self, username, password):
        # The third attempt may succeed; no counter-only rejection after success.
        if self._failures.get(username, 0) >= 3:
            raise PermissionError('Three failed attempts; account locked for this program run')
        if not self.auth_pass(username, password):
            self._failures[username] = self._failures.get(username, 0) + 1
            self._storage.record_event('Failed login: ' + username)
            raise PermissionError('Username/password do not match')
        self._failures[username] = 0
        token = secrets.token_hex(16)
        self._sessions[token] = (username, self.auth_role(username))
        self._storage.record_event('Login: ' + username)
        return token

    def require(self, token, action):
        session = self._sessions.get(token)
        if session is None or action not in self._permissions[session[1]]:
            raise PermissionError('Not authorized for this operation')
        return session  # username and role only; never a password/account record

    def new_user(self, token, name, password, role):
        actor, _ = self.require(token, 'create')
        user = User(name, password, role)
        self._save(user)
        self._storage.record_event('Account created by ' + actor + ': ' + user._name)

    def logout(self, token):
        self._sessions.pop(token, None)
