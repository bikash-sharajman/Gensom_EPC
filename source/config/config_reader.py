from configparser import ConfigParser
from pathlib import Path
from dotenv import load_dotenv
import os


class ConfigReader:

    _config = ConfigParser()
    root_dir = Path(__file__).parent.parent.parent

    config_path = root_dir / "config.ini"
    env_path = root_dir / ".env"
    load_dotenv(env_path)

    _config.read(config_path)

    @classmethod
    def get_browser(cls):
        return cls._config.get("DEFAULT", "default_browser")

    @classmethod
    def get_headless(cls):
        return cls._config.getboolean("DEFAULT", "default_headless")

    @classmethod
    def get_slow_mo(cls):
        return cls._config.getint("DEFAULT", "slow_mo")

    @classmethod
    def get_url(cls):
        return cls._config.get("ENVIRONMENTS", "qa")
    

    email: str = (os.getenv("email") or "").strip()
    password: str = (os.getenv("password") or "").strip()
    url:str = (os.getenv("url") or "").strip()



   
cr = ConfigReader()

