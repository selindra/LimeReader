# LimeReader

## Description: 

This class can:
1. Read data from LimeSDR
2. Convert data to complex64 numpy array
3. Save data as a bin file

For using LimeSDR with Raspberry Pi use the malinapi project description. There is a basic instalation file and solution to most of the errors that can be catched on the way.

works on this configuration, on 110 seconds get killed:
python3 limereader.py --center 243e6 --time 100 --fs 2e6 --bw 1e6 --channel 1 --filename 28-03-1518.bin
