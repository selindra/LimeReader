# LimeSDR

Short script which allows to read data from RX1 and RX2 ports of LimeUSB sdr. Output is 1 or 2 files with pairs of numpy.complex64 numbers

python3 lime.py --time [measurement time in seconds] --samprate [sampling rate in samples/sec] --bw [bandwidth in Hz] --channel [channel which is supposed to be used, 1 or 2 or 1 2]  --filename [path to output files, two channels demands two filenames]


example: 

 python3 limereader.py --center 244e6 --time 1 --fs 31.25e5 --bw 6e6 --channel 1 2 --filename test12.bin test22.bin

Here are my installation history entries from oldest to newest

sudo add-apt-repository -y ppa:myriadrf/drivers

sudo apt-get update

sudo apt-get install python3-numpy python3-scipy soapysdr-tools python3-soapysdr

sudo apt-get install python-dev swig

sudo apt-get install soapysdr-module-lms7

sudo apt-get install libsoapysdr-dev

sudo apt-get install limesuite liblimesuite-dev limesuite-udev limesuite-images

SoapySDRUtil --info  for checking if everything correct

SoapySDRUtil --find  to see all SDR devices

prerequisites:

sudo apt-get install python3

sudo pip3 install numpy

last Ubuntu 18.04
