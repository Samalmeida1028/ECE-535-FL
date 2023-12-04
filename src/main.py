import configparser
from fl import FL

def read_config(path):
    config = configparser.ConfigParser()
    #config.read('/media/sf_ece535SLAM/config/ur_fall/ablation/rgb_depth/A30_B30_AB0_label_A_test_B')
    #config.read('/media/sf_ece535SLAM/config/mhealth/ablation/gyro_mage/A30_B30_AB0_label_A_test_B')
    #config.read('/media/sf_ece535SLAM/config/opp/dccae/A10_B0_AB30_label_A_test_B')
    #config.read('/media/sf_ece535SLAM/config/mhealth/split_ae/acce_gyro/A10_B10_AB30_label_A_test_B')
    #config.read('/media/sf_ece535SLAM/config/ur_fall/split_ae/rgb_depth/A10_B10_AB30_label_A_test_B')
    config.read(path)

    return config

paths = ['/media/sf_ece535SLAM/config/mhealth/split_ae/acce_gyro/A0_B0_AB30_label_A_test_B', # UmFL
         '/media/sf_ece535SLAM/config/mhealth/split_ae/acce_gyro/A0_B0_AB30_label_AB_test_B', # MmFL
         '/media/sf_ece535SLAM/config/opp/dccae/A0_B0_AB30_label_A_test_B', # UmFL
         '/media/sf_ece535SLAM/config/opp/dccae/A0_B0_AB30_label_AB_test_B', # MmFL
         '/media/sf_ece535SLAM/config/ur_fall/split_ae/rgb_depth/A0_B0_AB30_label_A_test_B', # UmFL
         '/media/sf_ece535SLAM/config/ur_fall/split_ae/rgb_depth/A0_B0_AB30_label_AB_test_B'] # MmFL

for p in paths:
    config = read_config(p)
    fl = FL(config)
    fl.start()