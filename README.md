# TasKiller

## A User-Friendly Process Killer for Linux

**TasKiller** is a desktop application built with Python/PySide6 that allows you to easily terminate processes on your Linux system. It provides a user-friendly interface to search for running processes, view details, and selectively kill them.

### Features:

* **Search & Filter:** Enter a process name to quickly find matching processes.
* **Process Information:** View details like Process ID (PID) and Status for each process.
* **Selective Termination:** Select specific processes to terminate or kill all at once.
* **Easy-to-Use Interface:** Intuitive design with clear buttons and informative details.
* **About Dialog:** View information about the application's author, email, creation date, and update history.

### System Requirements

* Linux operating system
* Python 3.6 or later
* PySide6 (install using `pip install PySide6`)
* psutil library (install using `pip install psutil`)
* argparse (install using `pip install argparse`)

**Optional:**

* A process name can be provided as a command-line argument for a more focused search.

### Running TasKiller

1. Install the required libraries (`pip install PySide6 psutil argparse`). If you don't have other requirements, python will squawk and let you know. You can grab those up with another pip install <missing> <deps>.
2. Run the script: `python TasKiller.py` (or `python3 TasKiller.py` on some systems).
   I suggest `python TasKiller.py -h` to get a quick commandline summary.

**Using the Application:**

* Enter a process name in the search bar (optional).
* Click "Refresh" to list any new matching processes.
* Select the processes you want to terminate by clicking on their rows.
* Click "Kill Selected Processes" to terminate the chosen processes.
* A confirmation message will be displayed indicating successful termination or potential errors. Currently it spits out info to your terminal.  Still up in the air whether that's necessary or not. If you don't like it, you can redirect output to a log file or to /dev/null.  Or hack the script as you deem fit.

**About Dialog:**

* Click on the "About" menu option to view information about the application's author, email, creation date, and update history.

### Dummy Processes (For testing)

I don't know why you would personally need to test it, but the script can be started to spawn a specific number of dummy "sleep" processes for testing purposes. As in, you start them, kill them, and boom, test concluded. I used it while I was testing the interface in the legacy version 1.0 of this thing.  It just carried over to this version. This option is disabled by default, but you can set dummies with the "-s 1..5" option. The actual DUMMY variable was removed in version 3.0.1, in favor of the command line switch.

### TODO

There may still be more to do with this thing. If you want to help, get ahold of me after the 2025 new year.

### Thanks!
