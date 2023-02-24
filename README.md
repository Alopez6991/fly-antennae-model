# Experimnetal setup
collect wind speed data with 2d hotwire. This is published on topic **analog_output** Collect mkv video at 200 fps with 2000 exposure.
you collect the mkv videos by runnig the basler/braid script outlined the how to found [here](https://github.com/vanbreugel-lab/How_To_Guides/tree/main/recording_videos_with_braid). 
# Post Preccesing
in the directory that you collected hotwire data as .bag files place **bag2hdf5.py** and **convert_all.py** <br> 
run: ```python convert_all.py```

Next you should follow the instruction for [deeplabcut](https://github.com/vanbreugel-lab/How_To_Guides/tree/main/deeplabcut_instructions) and stop after the step **Create a training dataset and train the network using a GPU (much faster)**

Then you should follow the steps found for [Anipose](https://github.com/vanbreugel-lab/How_To_Guides/tree/main/Running_Anipose_with_Deep_Lab_Cut)

Toss your wind sensor data into the script **New_calibration.ipynb** to get your wind sensor data in terms of x and y velocity values
