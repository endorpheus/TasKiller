import sys
from typing import List, Optional

import psutil

from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QAbstractItemView, QPushButton, QHeaderView,
    QMessageBox, QInputDialog, QWidget, QMenu
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction

from Jelly import Jelly  # Import the updated Jelly class

# About
AUTHOR = "Ryon Shane Hall"
EMAIL = "endorpheus@gmail.com"
CREATED = "202409230220"
UPDATED = "202409231537"
VERSION = "3.0"

# Dummy processes to run (0 for no spawn)
DUMMY = 0

class TasKiller(Jelly):
    def __init__(self):
        super().__init__()
        self.process_name = self.get_process_name()
        if not self.process_name:
            print("No process name provided. Exiting.")
            sys.exit(0)

        self.init_ui()
        self.update_process_list()
        self.adjustSize()

    def init_ui(self):
        self.setWindowTitle(f"TasKiller - {self.process_name}")
        self.resize(400, 300)  # Set initial size

        # Create a container widget for our content
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        self.table_widget = self.create_table_widget()
        layout.addWidget(self.table_widget)

        self.kill_button = self.create_button("Kill Selected Processes", self.kill_processes)
        layout.addWidget(self.kill_button)

        self.refresh_button = self.create_button("Refresh", self.update_process_list)
        layout.addWidget(self.refresh_button)

        # Add the content widget to Jelly
        self.add_content_widget(content_widget)

        self.create_menu()

    def create_table_widget(self) -> QTableWidget:
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["PID", "Name", "Status"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.MultiSelection)
        return table

    def create_button(self, text: str, callback) -> QPushButton:
        button = QPushButton(text)
        button.clicked.connect(callback)
        return button

    def create_menu(self):
        menu = QMenu("Help", self)
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        menu.addAction(about_action)
        self.add_menu(menu)

    def get_process_name(self) -> Optional[str]:
        if len(sys.argv) > 1:
            return sys.argv[1]
        name, ok = QInputDialog.getText(self, "Search for Process", "Enter process name:")
        return name if ok else None

    def update_process_list(self):
        self.table_widget.setRowCount(0)
        matching_processes = self.get_matching_processes()

        if not matching_processes:
            print("No matching processes found.")
            QMessageBox.information(self, "No Results", f"No processes matching '{self.process_name}' found.")
            return

        for process in matching_processes:
            self.add_process_to_table(process)

        print(f"Found {len(matching_processes)} matching processes.")

    def get_matching_processes(self) -> List[dict]:
        return [
            process.info for process in psutil.process_iter(['pid', 'name'])
            if self.process_name.lower() in process.info['name'].lower()
        ]

    def add_process_to_table(self, process: dict):
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)
        self.table_widget.setItem(row, 0, QTableWidgetItem(str(process['pid'])))
        self.table_widget.setItem(row, 1, QTableWidgetItem(process['name']))
        self.table_widget.setItem(row, 2, QTableWidgetItem("Running"))

    def kill_processes(self):
        selected_rows = sorted(set(item.row() for item in self.table_widget.selectedItems()), reverse=True)
        if not selected_rows:
            print("No processes selected for termination.")
            return

        killed_pids = []
        for row in selected_rows:
            pid = int(self.table_widget.item(row, 0).text())
            status = self.terminate_process(pid)
            if status == "Terminated":
                killed_pids.append(pid)
                self.table_widget.removeRow(row)        
            else:
                self.table_widget.item(row, 2).setText(status)

        self.print_termination_results(killed_pids)
        self.adjustSize()

    def terminate_process(self, pid: int) -> str:
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait(timeout=3)  # Wait for the process to actually terminate
            return "Terminated"
        except psutil.NoSuchProcess:
            return "Not Found"
        except psutil.AccessDenied:
            return "Access Denied"
        except psutil.TimeoutExpired:
            return "Termination Timeout"
        except Exception as e:
            return f"Error: {str(e)}"

    def print_termination_results(self, killed_pids: List[int]):
        if killed_pids:
            print(f"Terminated processes with PIDs: {', '.join(map(str, killed_pids))}")
        else:
            print("No processes were terminated.")

    def show_about_dialog(self):
        about_dialog = QMessageBox(self)
        about_dialog.setText(f"TasKiller v{VERSION}\n{AUTHOR}\n{EMAIL}\nCreated: {CREATED}\nUpdated: {UPDATED}\nJust kill it.")
        about_dialog.show()

def create_dummy_processes(count: int = DUMMY):
    import subprocess
    for _ in range(count):
        subprocess.Popen(["sleep", "300"])
    print(f"Created {count} dummy 'sleep' processes.")

if __name__ == "__main__":
    if DUMMY > 0:
        create_dummy_processes()

    app = QApplication(sys.argv)
    window = TasKiller()
    window.show()
    sys.exit(app.exec())