# Copyright 2021 The UmbraTek Inc. All Rights Reserved.
#
# Software License Agreement (BSD License)
#
# Author: Jimy Zhang <jimy.zhang@umbratek.com> <jimy92@163.com>
# =============================================================================
import sys
import time

sys.path.append("./api")
sys.path.append("./modules_lib/")
from adra.adra_api_serial import AdraApiSerial


def main():
    adra = AdraApiSerial("/dev/ttyUSB0", 921600)  # instantiate the adra executor api class
    adra.connect_to_id(1)  # The ID of the connected target actuator, where the ID is 1
    adra.set_motion_mode(3)  # Set actuator motion mode 3: current mode
    adra.set_motion_enable(1)  # Enable actuator
    adra.set_tau_target(0.8)  # Set actuator motion current 0.8A
    while 1:
        time.sleep(0.01)


if __name__ == '__main__':
    main()
