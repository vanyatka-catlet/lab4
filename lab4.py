#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Sensor:
    def __init__(self, fps, power, min_range, max_range, fov):
        self.fps = fps
        self.power = power
        self.min_range = min_range
        self.max_range = max_range
        self.azimuth = fov[0]
        self.elevation = fov[1]
        
    def is_true(self):
        if (self.power == 1):
            return True
        else:
            return False
        
    def get_params(self):
        return f" fps = {self.fps} \n\
power = {self.power} \n\
min_range = {self.min_range} \n\
max_range = {self.max_range} \n\
azimuth = {self.azimuth} \n\
elevation = {self.elevation}"
    
class Radar(Sensor):
    def set_freq(self):
        self.__freq = 77e9
    def get_params(self):
        return f"Radar params:\n\
fps = {self.fps} \n\
power = {self.power} \n\
min_range = {self.min_range} \n\
max_range = {self.max_range} \n\
azimuth = {self.azimuth} \n\
elevation = {self.elevation}"
   
class Camera(Sensor):
    def set_type(self):
        self.__type = "visible"
    
    def set_memory(self):
        self.__memory = 1024 #in Mb
    def get_params(self):
        return f"Camera params:\n\
fps = {self.fps} \n\
power = {self.power} \n\
min_range = {self.min_range} \n\
max_range = {self.max_range} \n\
azimuth = {self.azimuth} \n\
elevation = {self.elevation}"

class Lidar(Sensor):
    def set_lights(self):
        self.__num_of_lights = 8
    def get_params(self):
        return f"Lidar params:\n\
fps = {self.fps} \n\
power = {self.power} \n\
min_range = {self.min_range} \n\
max_range = {self.max_range} \n\
azimuth = {self.azimuth} \n\
elevation = {self.elevation}"

radar_fps = 10
radar_power = True
radar_min_range = 1
radar_max_range = 250
radar_fov = [70,10]

my_radar = Radar(radar_fps,
                 radar_power,
                 radar_min_range,
                 radar_max_range,
                 radar_fov)

camera_fps = 50
camera_power = False
camera_min_range = 0
camera_max_range = 50
camera_fov = [60,30]

my_camera = Camera(camera_fps,
                 camera_power,
                 camera_min_range,
                 camera_max_range,
                 camera_fov)

lidar_fps = 20
lidar_power = True
lidar_min_range = 0.5
lidar_max_range = 150
lidar_fov = [360,20]

my_lidar = Lidar(lidar_fps,
                 lidar_power,
                 lidar_min_range,
                 lidar_max_range,
                 lidar_fov)

my_tech_vis_system=[my_radar, my_camera, my_lidar]

for a in range (0,3):
    int(input('Введите число от 0 до 2, где 0 - параметры радара, 1 - параметры камеры, 2 - параметры лидара: 0'))
    print(my_tech_vis_system[a].get_params())
"""
Created on Fri Dec 20 15:34:03 2024

@author: _vanyatka
"""

