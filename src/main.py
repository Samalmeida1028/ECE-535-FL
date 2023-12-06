import configparser
from fl import FL
import os

def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config

config_directory = 'config'

paths = []
for dir, subdir,files in os.walk(config_directory):
    for sdir in subdir:
        for file in files:
            paths.append(os.path.join(dir,sdir,file))

        # for data in direct:
        #     for file in data:
        #         pass
                # print(os.path.join(dir,direct,data,file))


# for p in paths:
#     print(paths)





for p in paths:
    config = read_config(p)
    fl = FL(config)
    fl.start()