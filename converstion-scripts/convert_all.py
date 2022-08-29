# import required module
import os
import bag2hdf5
# assign directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = dir_path
# iterate over files in
# that directory
LIST=[]
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		list_1=f
		if f[-4:]==".bag":
			LIST.append(f)
print (LIST)

for i in range(0,len(LIST)):
	os.system("python bag2hdf5.py "+LIST[i])
