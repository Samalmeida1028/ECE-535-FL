# import configparser
# from fl import FL
import os

# def read_config(path):
#     config = configparser.ConfigParser()
#     config.read(path)
#     return config

config_directory = 'config'

paths = []
for dir in os.listdir(config_directory):
    t_path=os.path.join(config_directory,dir)
    print(t_path)
    for direct in os.listdir(t_path):
        t_path = os.path.join(t_path,direct)
        print(t_path)
        # for data in direct:
        #     for file in data:
        #         pass
                # print(os.path.join(dir,direct,data,file))


# for p in paths:
#     print(paths)





# for p in paths:
#     config = read_config(p)
#     fl = FL(config)
#     fl.start()