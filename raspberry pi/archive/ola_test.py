

# Raspberry Pi 3
# pip install ola
# sudo apt-get install python-dev
# sudo apt-get install libncurses5-dev
# sudo easy_install readline
#
# sudo pip install protobuf


import array
from ola.ClientWrapper import ClientWrapper

def DmxSent(state):
  wrapper.Stop()

universe = 1
data = array.array('B', [8, 120, 0,8,120,0])
wrapper = ClientWrapper()
client = wrapper.Client()
client.SendDmx(universe, data, DmxSent)
wrapper.Run()
