<!--
# Experimnetal setup
collect wind speed data with 2d hotwire. This is published on topic **analog_output** Collect mkv video at 200 fps with 2000 exposure.
you collect the mkv videos by runnig the basler/braid script outlined the how to found [here](https://github.com/vanbreugel-lab/How_To_Guides/tree/main/recording_videos_with_braid). 
-->
# Experimental setup with the 3d Trisonica
## physical system
- Physical setup camera system
  1. place the camera mount in the wind tunnel.
  2. the mount has 3 cables that need to be connected.
  3. Coming out of the camera is a BNC cable that need to be connected to the triger box on the left side of the wind tunnel, disconnect one existing BNC cable and replace with yours.
  4. Coming out of the camera is a USB cable. connect that to the laptop or your computer
  5. then connect a micro USB to USB cable from the triger box to the lap top. youll have to swap out the one that is already pulgged into the trigger box.  
- Physical setup 3D Ultrasonic sensor
  1. mount the 3D sensor to the face of the adjustable rig.
  2. place inside the wind tunnel.
  3. the 3d sensor has one out put cable that need to be connected.
  4. connect a micro USB to USB cable from the 3d sensor hub to your laptop.
  5. turn the switch on on the 3d sensor's HUB.
- Camera lights
  1. there are two sets of camera lights that need to be pligged in. 
  2. the top lights are attaced to a pico buck and should have the female end connected to it. unplug one of the male ends from the wind tunnel and use that. 
  3. the bottom light ring has two jumper wires comeing out of it. these get pluged into a power suply. set the power supply to 12v and 1 A.
  4. the power supply also needs to be plugged in to any outlet or power strip.
- Computer
  1. if using the laptop it need to be pluged in to its piwer supply at all times to maintain charge.     
## Softwear/Code/Terminal/ect
- Terminal set up
  1. use ``` mkdir ``` to make a new directory for collecting data. e.g. ``` mkdir 03_15_23_fly ```
  2. change directories to new folder e.g. ``` cd 03_15_23_fly ```
  3. run the comand ``` roscore ```
- Arduino set up 
  1. flash the arduino with ```fans_no_ros_control.ino ```. This code currently works for Lamninar and Static. you need to comment out lines 29-32 
    ```cpp
      if (Serial.available()){
        Mode = Serial.read();
        new_info =0;
        }
    ```
    and uncomment line 33

    ```cpp
    Mode='T';
    ```

    to swap to Turb. 
- Triasonica set up
  1. run the comand ``` rosrun trisonica trisonica_usb.py ``` note the port your trisonica is pluged into and change that in the script. typically ```dev/ttyUSB0``` or ```dev/ttyUSB1```
 - Camera set up
  1. run ``` braid-pylon run /path/to/config.toml ``` e.g. ``` braid-pylon run Desktop/config.toml ```


<!--
# Post Preccesing
run the data you have colleced on the trisonica node with [MATLAB script](https://github.com/Alopez6991/fly-antennae-model/tree/main/converstion-scripts/MATLAB-bag2h5) to convert from a .bag file to a .hdf5


in the directory that you collected hotwire data as .bag files place **bag2hdf5.py** and **convert_all.py** <br> 
run: ```python convert_all.py```

Next you should follow the instruction for [deeplabcut](https://github.com/vanbreugel-lab/How_To_Guides/tree/main/deeplabcut_instructions) and stop after the step **Create a training dataset and train the network using a GPU (much faster)**

Then you should follow the steps found for [Anipose](https://github.com/vanbreugel-lab/How_To_Guides/tree/main/Running_Anipose_with_Deep_Lab_Cut)

Toss your wind sensor data into the script **New_calibration.ipynb** to get your wind sensor data in terms of x and y velocity values
-->
