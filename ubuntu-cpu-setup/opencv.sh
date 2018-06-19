cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.1.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.1.zip

unzip opencv.zip
unzip opencv_contrib.zip

cd ~/opencv-3.4.1/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D WITH_CUDA=OFF \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules \
      -D BUILD_EXAMPLES=ON ..

make -j4

sudo make install
sudo ldconfig
cd ~
rm -rf opencv-3.4.1 opencv.zip
rm -rf opencv_contrib-3.4.1 opencv_contrib.zip