from netmiko.linux import LinuxSSH
from datetime import datetime
from conf import Setting

setting = Setting()

def connect_to_nfware_server_via_ssh() -> LinuxSSH:
    try:
        ssh_connection = LinuxSSH(
            ip=setting.nfw_ip,
            port=setting.nfw_port,
            username=setting.nfw_user,
            password=setting.nfw_password
        )
        return ssh_connection
    except Exception as e:
        print(f"Error connecting to NFware server: {e}")
        return None


def get_config_from_nfware_server(ssh_connection: LinuxSSH) -> str:
    try:
        config = ssh_connection.send_command(setting.export_config_command)
        return config
    except Exception as e:
        print(f"Error fetching config from NFware server: {e}")
        return ""   


def save_backup_file_locally(config: str) -> dict:
    try:
        backup_file_name = f'backup_config__{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.txt'
        backup_file_path = f'./backups/{backup_file_name}'
        with open(backup_file_path, "w") as backup_file:
            backup_file.write(config)
        return {"status": "success", "file_path": backup_file_path}
    except Exception as e:
        print(f"Error saving backup file locally: {e}")
        return {"status": "error", "message": str(e)}


def notify_backup_status(backup: dict) -> None:
    pass


def run() -> None:
    # Getting configs
    ssh_connection = connect_to_nfware_server_via_ssh()
    config = get_config_from_nfware_server(ssh_connection)
    ssh_connection.disconnect()

    if config == "":
        print("No config retrieved, aborting backup process.")
        return

    # Backup configs
    backup = save_backup_file_locally(config)

    # Notifying backup status in some channel (Telgram or e-mail) the status backup 
    notify_backup_status(backup)


if __name__ == "__main__":
    print('Starting backup process...')
    run()
