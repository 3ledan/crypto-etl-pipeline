#!/usr/bin/env python3
from extract import crypto_data
from transform import transform_data
from load import load
import os

os.environ['PATH'] = "/opt/anaconda3/bin/python:" + os.environ['PATH']

# ELT model
def run_pipeline():
    data = crypto_data()
    processed_data = transform_data(data)
    load(processed_data)

if __name__ == "__main__":
    run_pipeline()
