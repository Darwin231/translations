import os 
from typing import Optional, Union
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv, find_dotenv

class Environment:

    def __init__(self, dotenv_path: Optional[Union[str, Path]] = None):
        """
        dotenv_path: ruta al archivo .env. Si es None, buscará automáticamente con find_dotenv().
        """
        self.dotenv_path = Path(dotenv_path) if dotenv_path else None
        self._loaded = False
  

    def load(self, override: bool = False):
        """
        Load the environment
        """
        if self._loaded:
            return "Loaded"
        
        path = str(self.dotenv_path) if self.dotenv_path else find_dotenv(usecwd=True)
        
        # Si no hay .env (path == "" o None), marcamos como "cargado" y salimos silenciosamente.
        # Esto permite que el programa funcione sin .env (útil en producción/CI).
        if not path:
            self._loaded = True
            return

        load_dotenv(dotenv_path=path)
        

    def get(self, name: str, default: Optional[str] = None, required: bool = False):
        """
        With the loaded environment, get the nedded variable.
        """

        self.load()

        value = os.getenv(name, default)

        if required and (value is None or value == ""):
            raise KeyError(f"Required environment variable `{name}")
        
        return value


