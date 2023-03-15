
%% Run bag2hdf5.m for multiple files
clear ; close all ; clc

topics = {'trisonica'};
root = '/home/austinlopez/Documents/MATLAB/bag2hdf5/bag';

[files, path] = uigetfile({'*.bag','files'}, 'Select files', root, 'MultiSelect', 'on');
files = string(files);

n_file = length(files);
for n = 1:n_file
    filepath = fullfile(path, files(n));
    bag2hdf5(filepath, topics, true);
end