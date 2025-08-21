# 0c8m_prototype_a_rea.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import cv2
import os
import sys
import time
import tkinter as tk
from tkinter import filedialog
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision import transforms
from PIL import Image

# Global Variables
project_folder = os.path.dirname(os.path.abspath(__file__))
module_folder = os.path.join(project_folder, 'modules')
data_folder = os.path.join(project_folder, 'data')
output_folder = os.path.join(project_folder, 'output')

# Function to create directory if not exists
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Create necessary directories
create_dir(module_folder)
create_dir(data_folder)
create_dir(output_folder)

class ModuleGenerator:
    def __init__(self, module_name, module_type):
        self.module_name = module_name
        self.module_type = module_type
        self.module_path = os.path.join(module_folder, module_name)
        create_dir(self.module_path)
    
    def generate_module(self):
        if self.module_type == 'AR':
            # Generate AR module
            pass
        elif self.module_type == 'VR':
            # Generate VR module
            pass

class ModuleDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.modules = []
        self.load_db()
    
    def load_db(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r') as f:
                self.modules = json.load(f)
        else:
            with open(self.db_path, 'w') as f:
                json.dump(self.modules, f)
    
    def save_db(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.modules, f)
    
    def add_module(self, module_name, module_type):
        self.modules.append({'module_name': module_name, 'module_type': module_type})
        self.save_db()

class ARVRGenerator:
    def __init__(self):
        self.db_path = os.path.join(project_folder, 'module_db.json')
        self.module_db = ModuleDatabase(self.db_path)
    
    def generate_module(self, module_name, module_type):
        module_generator = ModuleGenerator(module_name, module_type)
        module_generator.generate_module()
        self.module_db.add_module(module_name, module_type)

if __name__ == "__main__":
    generator = ARVRGenerator()
    while True:
        print("1. Generate AR Module")
        print("2. Generate VR Module")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            module_name = input("Enter module name: ")
            generator.generate_module(module_name, 'AR')
        elif choice == '2':
            module_name = input("Enter module name: ")
            generator.generate_module(module_name, 'VR')
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")