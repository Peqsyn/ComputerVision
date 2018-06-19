sudo apt-get -y update
sudo apt-get -y upgrade

# install developer tools as well as prerequisites required for image and video I/O etc.
sudo apt-get -y install build-essential cmake git unzip pkg-config
sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install libhdf5-serial-dev graphviz
sudo apt-get -y install libopenblas-dev libatlas-base-dev gfortran
sudo apt-get -y install python-tk python3-tk python-imaging-tk

# install python 3
sudo apt-get -y install python3-dev