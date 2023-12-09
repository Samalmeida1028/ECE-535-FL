import configparser
from fl import FL
import os

def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config

config_directory = 'config'
paths = []

for dir, subdir, files in os.walk(config_directory):
    if len(subdir) == 0:
        for file in files:
            paths.append(os.path.join(dir, file))

# for p in paths:
#     print(p)

# print(len(paths)) # 98 configs * 100 runs per config = 9800 runs total ~ 24 hours tops

for p in paths:
    config = read_config(p)
    fl = FL(config)
    fl.start()