# udpate ubuntu
sudo apt-get -y update
sudo apt-get -y upgrade

# install necessary development tools, images/video I/O, GUI operations
sudo apt-get -y install build-essential cmake git unzip pkg-config
sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install libhdf5-serial-dev graphviz
sudo apt-get -y install libopenblas-dev libatlas-base-dev gfortran
sudo apt-get -y install python-tk python3-tk python-imaging-tk

# download python 3
sudo apt-get -y python3-dev

# prepare system for default drivers with NVIDA CUDA drivers
sudo apt-get -y install linux-image-generic linux-image-extra-virtual
sudo apt-get -y install linux-source linux-headers-generic