# Configuring Ubuntu for deep learning with Python (GPU version of TensorFlow)
<!-- 1. Click [here](http://releases.ubuntu.com/16.04/ubuntu-16.04.4-desktop-amd64.iso) to install the .iso for Ubuntu 16.04
2. Install Ubuntu 16.04 via virtual machine, or onto a local hard drive
3. Turn off X server / X window system two methods, picked one
	1. First method (easier method)
		1. Turn off machine
		2. Unplug your monitor
		3. Reboot
		4. SSH into your machine from a separate system
		5. Perform the install instructions
	2. Second method
		1. Close all running applications
		2. Press ctrl + alt + F2
		3. Login with your username and password
		4. Stop X server by executing sudo service lightdm stop
		5. Perform the install instructions
4. Install Ubuntu system dependencies
	1. Open up terminal
	2. Run the following [setup.sh](setup.sh) with the following command chmod +x /path/to/setup.sh
	3. After running the command you can run the shell script using ./setup.sh
5. Install CUDA Toolkit
	1. First disable Nouveau kernel driver by creating a new file by typing into command line
		1. sudo nano /etc/modprobe.d/blacklist-nouveau.conf
		2. Add the following lines and then save and exit
			1. blacklist nouveau
			2. blacklist lbm-nouveau
			3. options nouveau modeset=0
			4. alias nouveau off
			5. alias lbm-nouveau off -->
1. The GPU instructions install are not as straight forward as the CPU version, use [this](https://www.pyimagesearch.com/2017/09/27/setting-up-ubuntu-16-04-cuda-gpu-for-deep-learning-with-python/) link for the instructions.
