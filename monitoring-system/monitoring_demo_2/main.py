"""STARTUP ONLY: create modules and connect them. Run: python3 main.py"""
import argparse
from pathlib import Path
from storage import Storage
from security import Accounts
from communication import Communication
from monitoring import Monitoring
from ui import Console

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', default=str(Path(__file__).with_name('demo.sqlite3')))
    args = parser.parse_args()
    storage = Storage(args.database)
    try:
        accounts = Accounts(storage)
        communication = Communication(c['adc'] for c in storage.cabinets())
        monitoring = Monitoring(storage, accounts, communication)
        Console(accounts, monitoring).run()
    finally:
        storage.close()

if __name__ == '__main__':
    main()
