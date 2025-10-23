import os
import sys
import json
from typing import Dict, Any, Optional

class Config:
    def __init__(self, env_file_path: str = ".alg_env"):
        self.env_file_path = env_file_path
        self.db_urls = {}
        self.import_paths = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from .alg_env file"""
        try:
            with open(self.env_file_path, 'r') as file:
                content = file.read().strip()
                
            # Parse the configuration
            for line in content.split('\n'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    if key == 'db_urls':
                        self.db_urls = json.loads(value)
                    elif key == 'import_paths':
                        self.import_paths = json.loads(value)
            
            # Add import paths to Python path
            self._add_paths_to_sys()
                        
        except FileNotFoundError:
            print(f"Warning: {self.env_file_path} file not found")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in {self.env_file_path}: {e}")
        except Exception as e:
            print(f"Error loading configuration: {e}")
    
    def _add_paths_to_sys(self):
        """Add import paths to sys.path for module imports"""
        for path_type, path in self.import_paths.items():
            if path and path not in sys.path:
                sys.path.append(path)
                # print(f"Added to Python path: {path}")
    
    def get_db_url(self, db_type: str) -> Optional[str]:
        """Get database URL for specific type"""
        return self.db_urls.get(db_type, [None])[0] if self.db_urls.get(db_type) else None
    
    def get_import_path(self, path_type: str) -> Optional[str]:
        """Get import path for specific type"""
        return self.import_paths.get(path_type)
    
    def get_postgres_url(self) -> Optional[str]:
        """Get PostgreSQL database URL"""
        return self.get_db_url('postgres_async')
    
    def get_redis_url(self) -> Optional[str]:
        """Get Redis database URL"""
        return self.get_db_url('redis')

# Create a global config instance
config = Config()