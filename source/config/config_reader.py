from configparser import ConfigParser
from pathlib import Path


class ConfigReader:

    _config = ConfigParser()

    config_path = Path(__file__).parent.parent.parent / "config.ini"

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
    
    
cr = ConfigReader()