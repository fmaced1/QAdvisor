import logging
import uuid
import os
import json
import pandas as pd
from timeit import default_timer as timer
from datetime import timedelta
import yaml

logging.basicConfig(
    filename="logs/log.log",
    format='%(asctime)s %(message)s', 
    filemode='a',
    level=logging.DEBUG
)

log = logging.getLogger(__name__)

class Cronometer:
    def start_cronometer(self) -> float:
        return timer()

    def stop_cronometer(self, start_time: float) -> timedelta:
        return timedelta(seconds=timer() - start_time)

def percentage_change(old_value: float, new_value: float) -> float:
    """Calculates the percentage change between two prices."""
    if old_value == 0:
        raise ValueError("old_value cannot be zero")
    return 100 * (new_value - old_value) / old_value

def file_exists(filename: str) -> str:
    """Checks if a file exists and returns its absolute path."""
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, filename)

    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")

    return full_path

def read_yaml(yaml_file: str) -> dict:
    """Reads a YAML file and returns its contents as a dictionary."""
    with open(yaml_file, 'r') as content:
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError as err:
            log.error(f"Error reading YAML file: {err}")
            raise

def read_file(file_to_read: str) -> str:
    """Reads a file and returns its content as a single string."""
    full_path = os.path.join(os.path.dirname(__file__), file_to_read)
    
    with open(full_path, 'r') as file:
        try:
            return file.read().replace('\n', '')
        except ValueError as err:
            log.error(f"Error reading file: {err}")
            raise

def read_csv_df(csv_filename: str) -> pd.DataFrame:
    """Reads a CSV file into a DataFrame."""
    full_path = os.path.join(os.path.dirname(__file__), csv_filename)
    return pd.read_csv(full_path)

def write_json(content: dict, json_filename: str) -> str:
    """Writes a dictionary to a JSON file."""
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, sort_keys=True, indent=4)

    log.info(f"Function: write_json | Filename: {json_filename}")
    return json_filename

def write_output(content: str, dir_to_file: str) -> str:
    """Writes content to a file, creating directories if necessary."""
    try:
        if not dir_to_file:
            dir_to_file = os.path.join('output', f'{uuid.uuid4()}.txt')

        os.makedirs(os.path.dirname(dir_to_file), exist_ok=True)

        with open(dir_to_file, 'a') as f:
            f.write(content)

        log.info(f"Function: write_output | File: {dir_to_file}")
        return dir_to_file
    
    except OSError as e:
        log.error(f"Unable to write to file: {dir_to_file}. Error: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected error: {e}")
        raise

def remove_files_in_folder(folders_to_cleanup: list) -> bool:
    """Removes all files in the specified folders."""
    for folder in folders_to_cleanup:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        for file in files:
            os.remove(os.path.join(folder, file))
    return True

def remove_file(filename: str) -> None:
    """Removes a file if it exists."""
    try:
        os.remove(filename)
    except FileNotFoundError:
        log.warning(f"File not found: {filename}")
    except Exception as e:
        log.error(f"Error removing file: {e}")
        raise

def df_analysis_to_json(df: pd.DataFrame, ticker: str) -> str:
    """Converts a DataFrame to a JSON string, including specific columns."""
    df = df.rename(columns={'stock splits': 'stock_splits'})
    df_json = df.to_dict(orient='index')
    output_json = {ticker: [{"date": str(index), **row} for index, row in df_json.items()]}
    return json.dumps(output_json, indent=4, ignore_nan=True)
