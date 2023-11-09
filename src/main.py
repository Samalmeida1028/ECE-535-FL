import configparser
import argparse
import logging
import os
import warnings
import torch
from fl import FL

def read_config():
    config = configparser.ConfigParser()
    config.read('/media/sf_ece535SLAM/config/ur_fall/ablation/rgb_depth/A30_B30_AB0_label_B_test_A')
    #config.read('/media/sf_ece535SLAM/config/mhealth/ablation/gyro_mage/A30_B30_AB0_label_A_test_B')
    #config.read('/media/sf_ece535SLAM/config/opp/dccae/A0_B0_AB30_label_AB_test_B')

    return config

config = read_config()

fl = FL(config)

fl.start()
