# plugins/history_management.py
from plugin_interface import Plugin
import pandas as pd
import os
import csv

current_dir = os.path.dirname(os.path.realpath(__file__))
HISTORY_FILE = os.path.join(current_dir, '..', 'history.csv')

class HistoryManagementPlugin(Plugin):
    def get_name(self):
        return "History Management Plugin"

    def get_commands(self):
        return {
            'load': self.load_history,
            'save history': self.save_history,
            'clear history': self.clear_history,
            'delete record': self.delete_record
        }

    def load_history(self, arg):
        try:
            history_df = pd.read_csv(HISTORY_FILE)
            if history_df.empty:
                print('No calculation history found.')
            else:
                print('Calculation history:')
                print(history_df)
        except FileNotFoundError:
            print('No calculation history found.')

    def save_history(self, history_data):
        with open(HISTORY_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            for operation, result in history_data:
                writer.writerow([operation, result])

    def clear_history(self, arg):
        with open(HISTORY_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Operation', 'Result'])

    def delete_record(self, index):
        try:
            history_df = pd.read_csv(HISTORY_FILE)
            history_df.drop(index, inplace=True)
            history_df.to_csv(HISTORY_FILE, index=False)
            print('Record deleted successfully.')
        except FileNotFoundError:
            print('No calculation history found.')
        except KeyError:
            print('Invalid record index. Record not found.')