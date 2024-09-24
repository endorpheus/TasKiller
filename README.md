# TasKiller

## TasKiller: A User-Friendly Process Killer for Linux

**TasKiller** is a desktop application built with PySide6 that allows you to easily terminate processes on your Linux system. It provides a user-friendly interface to search for running processes, view details, and selectively kill them.

### Features:

* **Search & Filter:** Enter a process name to quickly find matching processes.
* **Detailed Process Information:** View details like Process ID (PID) and Status for each process.
* **Selective Termination:** Select specific processes to terminate or kill all at once.
* **Easy-to-Use Interface:** Intuitive design with clear buttons and informative details.
* **Customizable Window Size:** Resize the window to fit your needs.
* **About Dialog:** View information about the application's author, email, creation date, and update history.

### System Requirements

* Linux operating system
* Python 3.6 or later
* PySide6 (install using `pip install PySide6`)
* psutil library (install using `pip install psutil`)

**Optional:**

* A process name can be provided as a command-line argument for a more focused search.

### Running TasKiller

1. Install the required libraries (`pip install PySide6 psutil`).
2. Run the script: `python TasKiller.py` (or `python3 TasKiller.py` on some systems).

**Using the Application:**

* Enter a process name in the search bar (optional).
* Click "Refresh" to list all running processes (or update the list).
* Select the processes you want to terminate by clicking on their rows.
* Click "Kill Selected Processes" to terminate the chosen processes.
* A confirmation message will be displayed indicating successful termination or potential errors.

**About Dialog:**

* Click on the "About" menu option to view information about the application's author, email, creation date, and update history.

### Dummy Processes (Optional)

The script can be configured to spawn a specific number of dummy "sleep" processes for testing purposes. This option is disabled by default (set `DUMMY = 0` in the code). If you want to create dummy processes, edit the `DUMMY` variable at the beginning of the script and set it to the desired number. Then, run the script again.

### TODO

There is MUCH to do with this work in progress. The list is long, especially with the Jelly class upon which it get's it's character. If you want to help, get ahold of me after the 2025 new year.

### Thanks!
