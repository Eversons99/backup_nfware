
def connect_to_nfware_server():
    pass

def get_config_from_nfware_server() -> str:
    pass

def save_backup_file(config: str) -> dict:
    pass

def notify_backup_status(backup: dict) -> None:
    pass

def run() -> None:
    # Getting configs
    server_connection = connect_to_nfware_server()
    config = get_config_from_nfware_server()
    server_connection.disconnect()

    # Backup configs
    backup = save_backup_file(config)

    # Notifying backup status in some channel (Telgram or e-mail) the status backup 
    notify_backup_status(backup)


if __name__ == "main":
    run()