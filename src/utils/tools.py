import logging, uuid, os
import simplejson as json

logging.basicConfig(filename="src/log/log.log",
                format='%(asctime)s %(message)s', 
                filemode='a')

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

from timeit import default_timer as timer
class Cronometer(object):
    def start_cronometer(self):
        return timer()

    def stop_cronometer(self, start_time):
        from datetime import timedelta
        end_time = timer()

        return timedelta(seconds=end_time - start_time)

def init_logging():
    logging.basicConfig(filename="src/log/log.log",
                    format='%(asctime)s %(message)s', 
                    filemode='a')

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    return log

def percentage_change(old_value, new_value):
    """ Calculating change in percentage between two prices
    print [100 * (b - a) / a for a, b in zip(prices[::1]), prices[1::1])]
    """

    result = float(100 * (new_value - old_value) / old_value)

    return result

def file_exists(filename=str):

    from errno import ENOENT
    import os

    script_dir = os.path.dirname(__file__)
    filename = os.path.join(script_dir, filename)

    if not os.path.isfile(filename):
        script_dir = os.path.dirname(__file__)
        filename = os.path.join(script_dir, filename)

    if not os.path.isfile(filename):
        raise IOError(ENOENT, 'File not found: ', filename)

    return filename

def read_yaml(self, yaml_file=str):
    import yaml

    with open(yaml_file, 'r') as content:
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError as err:
            print(err)

def read_file(file_to_read):
    import os
    file_to_read = os.path.join(os.path.dirname(__file__), file_to_read)

    with open(file_to_read, 'r') as file:
        try:
            content = file.read().replace('\n', '')
            return content
        except ValueError as err:
            raise Exception(err)

def read_csv_df(csv_filename):
    import pandas, os

    csv_filename = os.path.join(os.path.dirname(__file__), csv_filename)

    df = pandas.read_csv(csv_filename)

    return df

def write_json(content, json_filename):
    import json

    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, sort_keys=True, indent=4)

    log.info('function: {} filename: {}'.format('write_output', json_filename))

    return json_filename

def write_output(content, dir_to_file):

    """TODO melhorar o tratamento dessa funcao"""

    if not dir_to_file:
        dir_to_file = '{0}output-{1}'.format(dir_to_file, uuid.uuid4())

    f = open(dir_to_file, 'a')
    f.write(content)
    f.close()

    log.info('function: {} dir_to_file: {}'.format('write_output', dir_to_file))

    return dir_to_file

def remove_files_in_folder(folders_to_cleanup):
    for folder in folders_to_cleanup:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
        for file in files:
            os.remove("{}{}".format(folder, file))

    return True

def remove_file(filename):
    try:
        return os.remove(filename)
    except:
        pass

def df_analisys_to_json(df, ticker):
    _open = df['open']
    _high = df['high']
    _low = df['low']
    _close = df['close']
    _volume = df['volume']
    _dividends = df['dividends']
    _stock_splits = df['stock splits']
    _macd = df['macd']
    _macds = df['macds']
    _macdh = df['macdh']
    _macdh_a = df['macdh_a']

    _json = {}
    _json[ticker] = []

    for i in range(0, len(df.index)):
        _json[ticker].append({
            "date": str(df.index[i]),
            "open": float(_open[i]),
            "high": float(_high[i]),
            "low": float(_low[i]),
            "close": float(_close[i]),
            "volume": float(_volume[i]),
            "dividends": float(_dividends[i]),
            "stock splits": float(_stock_splits[i]),
            "macd": float(_macd[i]),
            "macds": float(_macds[i]),
            "macdh": float(_macdh[i]),
            "macdh_a": str(_macdh_a[i])
        })

    _json = json.dumps(_json, indent=4, ignore_nan=True)

    return _json