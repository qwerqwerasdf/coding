import numpy as np
import matplotlib.pyplot as plt
import time

def create_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    hour_angle = -2 * np.pi * (hour + minute/60) / 12 + np.pi/2
    minute_angle = -2 * np.pi * minute / 60 + np.pi/2
    second_angle = -2*np.pi*second/60+np.pi/2
    