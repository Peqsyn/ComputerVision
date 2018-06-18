# Configuring Ubuntu for deep learning with Python
1. Click [here](http://releases.ubuntu.com/16.04/ubuntu-16.04.4-desktop-amd64.iso) to install the .iso for Ubuntu 16.04
2. Install Ubuntu 16.04 via virtual machine, or onto a local hard drive
3. Install Ubuntu system dependencies
	1. Open up terminal
	2. Run the following [setup.sh](setup.sh) with the following command chmod +x /path/to/setup.sh
	3. After running the command you can run the shell script using ./setup.sh
4. Create your Python virtual environment
	1. Run the following [venv.sh](venv.sh) with the following command chmod +x /path/to/venv.sh
	2. After running the command you can run the shell script using ./venv.sh
5. Compile and install OpenCV
	1. Run the following [opencv.sh](opencv.sh) with the following command chmod +x /path/to/opencv.sh
	2. After running the command you can run the shell script using ./opencv.sh
6. Install Keras
	1. Run the following [keras.sh](keras.sh) with the following command chmod +x /path/to/keras.sh
	2. After running the command you can run the shell script using ./keras.sh