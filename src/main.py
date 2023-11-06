import configparser
import argparse
import logging
import os
import warnings
import torch
from fl import FL

def read_config():
    config = configparser.ConfigParser()
    config.read('/media/sf_ece535SLAM/opp/dccae/A0_B0_AB30_label_AB_test_B')

    return config

config = read_config()

fl = FL(config)

fl.start()
