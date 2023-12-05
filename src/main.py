import configparser
from fl import FL

def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config

paths = ['/media/sf_ece535_project/ECE-535-SLAM/config/mhealth/split_ae/acce_gyro/A0_B0_AB30_label_A_test_B', # UmFL
         '/media/sf_ece535_project/ECE-535-SLAM/config/mhealth/split_ae/acce_gyro/A0_B0_AB30_label_AB_test_B', # MmFL
         '/media/sf_ece535_project/ECE-535-SLAM/config/mhealth/ablation/acce_gyro/A30_B30_AB0_label_A_test_B', # Baseline
         '/media/sf_ece535_project/ECE-535-SLAM/config/opp/dccae/A0_B0_AB30_label_A_test_B', # UmFL
         '/media/sf_ece535_project/ECE-535-SLAM/config/opp/dccae/A0_B0_AB30_label_AB_test_B', # MmFL
         '/media/sf_ece535_project/ECE-535-SLAM/config/opp/ablation/A30_B30_AB0_label_A_test_B', # Baseline
         '/media/sf_ece535_project/ECE-535-SLAM/config/ur_fall/split_ae/rgb_depth/A0_B0_AB30_label_A_test_B', # UmFL
         '/media/sf_ece535_project/ECE-535-SLAM/config/ur_fall/split_ae/rgb_depth/A0_B0_AB30_label_AB_test_B', # MmFL
         '/media/sf_ece535_project/ECE-535-SLAM/config/ur_fall/ablation/rgb_depth/A30_B30_AB0_label_A_test_B'] # # Baseline

for p in paths:
    config = read_config(p)
    fl = FL(config)
    fl.start()