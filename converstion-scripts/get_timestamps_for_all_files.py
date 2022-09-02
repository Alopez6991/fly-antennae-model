import sys
import glob
import os
import subprocess
import pandas as pd
from datetime import datetime
import ffmpeg #sudo apt install ffmpeg and pip install ffmpeg-python

def get_timestamps_func(input_folder):
	mkv_files = sorted(glob.glob(input_folder + '/*.mkv'))
	info=[]
	for i,mkv_video in enumerate(mkv_files):
		print('getting start time from ' + str(i+1) + ' of ' + str(len(mkv_files)) + ' files...')
		#proc = subprocess.Popen('ffprobe {mkv_video} -select_streams v -show_entries frame=pkt_pts_time -of default=nk=1:nw=1 -v 0'.format(mkv_video=mkv_video),shell=True,stdout=subprocess.PIPE)
		#proc_output = proc.communicate()[0].decode("utf-8")
		#timestamps = proc_output.split('\n')[0:-1]
    
		proc = subprocess.Popen('ffprobe -v quiet {mkv_video} -of default=nk=1:nw=1 -show_entries format_tags=creation_time'.format(mkv_video=mkv_video),shell=True,stdout=subprocess.PIPE)
		proc_output = proc.communicate()[0].decode("utf-8")
		creation_time = proc_output.split('\n')[0]
		utc_time = datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ')
		name=mkv_video.replace(os.getcwd()+"/","")
		#INFO=utc_time
		info.append([name,creation_time])
		#epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
		#epoch_timestamps = [float(x)+epoch_time for x in timestamps]

		#h5_file = glob.glob(os.path.splitext(mkv_video)[0] + '*.h5')[0]
		#df = pd.read_hdf(h5_file)
		
		#df.insert(0,'timestamp',epoch_timestamps)
		#df.to_hdf(h5_file,key='df',mode='r+')
	print(info)
if __name__ == "__main__":
	input_folder = sys.argv[1]
	get_timestamps_func(input_folder)
