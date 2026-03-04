# Backup Nfware Configuration

A Python utility for backing up NFware server configurations.

## Features

- Connect to NFware server
- Retrieve configuration data
- Save backup files to local storage or remote storage (FTP Server)
- Notify backup status via Telegram or email

## Installation

Clone the repository and install required packages:

```bash
pip install -r requirements.txt
```

## Usage (Windows 11)
Create a virtual environment to isolate project dependencies and third-party library versions. 

```python
python -m venv .venv
```

Activing the virtual environment
```python
    .venv/Scripts/activate
```

Running the aplication.
```python
python backup.py
```

## Functions

- `connect_to_nfware_server()` - Establishes connection to NFware server
- `get_config_from_nfware_server()` - Retrieves server configuration
- `save_backup_file(config)` - Saves configuration to backup file
- `notify_backup_status(backup)` - Sends backup status notification

## Requirements

- Python >= 3.11
