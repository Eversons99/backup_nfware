from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    nfw_ip: str
    nfw_user: str
    nfw_password: str
    nfw_port: int
    export_config_command: str
    
    # Reading environment variables from .env file
    class Config:
        env_file = ".env"
