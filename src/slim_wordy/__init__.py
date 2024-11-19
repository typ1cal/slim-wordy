import os
from box.exceptions import BoxValueError
import yaml
from slim_wordy.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns 

    Args:
        path_to_yaml (str):  path like input

    Raises:
        ValueError: If the YAML file is not valid
        e: empty file
    
        Returns:
            ConfigBox: A ConfigBox containing the YAML data
    """


    try:
        with open(path_to_yaml, 'r') as file:
            data = yaml.safe_load(file)
            if data is None:
                raise ValueError('The YAML file is empty.')
            return ConfigBox(data)
    except FileNotFoundError:
        logger.error(f'The YAML file {path_to_yaml} does not exist.')
        raise
    except yaml.YAMLError as e:
        logger.error(f'The YAML file {path_to_yaml} is not valid: {e}')
        raise
    except BoxValueError as e:
        logger.error(f'The YAML file {path_to_yaml} is not valid: {e}')
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """
        creates directories if they don't exist

    Args:
        path_to_directory (list):  list of paths like inputpaths
        ignore_log (bool, optional): If True, ignores logging errors. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory: {path}')

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path):  path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"