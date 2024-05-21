pip uninstall tensorflow
pip3 uninstall tensorflow
# install the dependencies (if not already onboard)
apt-get install gfortran
apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
apt-get install libatlas-base-dev libopenblas-dev libblas-dev
apt-get install liblapack-dev
# upgrade setuptools 47.1.1 -> 50.3.2
pip3 install --upgrade setuptools
pip3 install pybind11
pip3 install Cython==0.29.21
# install h5py with Cython version 0.29.21 (± 6 min @1950 MHz)
pip3 install h5py==2.10.0
pip3 install https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0-rc2/tensorflow-2.4.0rc2-cp37-none-linux_armv7l.whl