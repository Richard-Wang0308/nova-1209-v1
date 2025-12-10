# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

class RuntimeConfig:
    _current_dir = os.path.dirname(os.path.abspath(__file__))  # nova_ph2_mine/PSICHIC
    _parent_dir = os.path.dirname(_current_dir)  # nova_ph2_mine
    _base_dir = os.path.dirname(_parent_dir)  # nova-blueprint-test
    PSICHIC_PATH = os.path.join(_base_dir, 'nova_ph2', 'PSICHIC')
    device = os.environ.get("DEVICE_OVERRIDE")
    DEVICE = ["cpu" if device=="cpu" else "cuda:0"][0]
    MODEL_PATH = os.path.join(PSICHIC_PATH, 'trained_weights', 'PDBv2020_PSICHIC')
    BATCH_SIZE = 600
    
