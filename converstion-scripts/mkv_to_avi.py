import sys
import glob
import os
import subprocess
import ffmpeg #sudo apt install ffmpeg and pip install ffmpeg-python

def mkv_to_avi_func(input_folder):
	files = glob.glob(input_folder + '/*.mkv')
	for i,mkv_video in enumerate(files):
		print('Converting ' + str(i+1) + ' of ' + str(len(files)) + ' files...')
		avi_video = os.path.splitext(mkv_video)[0]+'.avi'
		subprocess.run('ffmpeg -i {mkv_video} -c:v copy -c:a copy {avi_video}'.format(mkv_video=mkv_video,avi_video=avi_video), shell=True)
	
if __name__ == "__main__":
	input_folder = sys.argv[1]
	mkv_to_avi_func(input_folder)
