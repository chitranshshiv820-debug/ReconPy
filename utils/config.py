import os
import json
import yaml

class ConfigLoader:
    """
    Loads configuration settings from YAML or JSON files.
    Example usage:
        config = ConfigLoader("config.yaml")
        api_key = config.get("shodan_api_key")
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.config: dict = {}
        self._load_config()

    def _load_config(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Config file not found: {self.filepath}")

        _, ext = os.path.splitext(self.filepath)

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                if ext.lower() in [".yaml", ".yml"]:
                    self.config = yaml.safe_load(f)
                elif ext.lower() == ".json":
                    self.config = json.load(f)
                else:
                    raise ValueError("Unsupported config format. Use .yaml/.yml or .json")

            if self.config is None:
                self.config = {}
        except Exception as e:
            raise RuntimeError(f"Error loading config: {e}")

    def get(self, key: str, default: object = None) -> object:
        """Retrieve a config value by key, with optional default."""
        return self.config.get(key, default)

    def all(self) -> dict:
        """Return the entire config dictionary."""
        return self.config

    def reload(self):
        """Reload the config file."""
        self._load_config()
