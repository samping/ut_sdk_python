# Copyright 2021 The UmbraTek Inc. All Rights Reserved.
#
# Software License Agreement (BSD License)
#
# Author: Jimy Zhang <jimy.zhang@umbratek.com> <jimy92@163.com>
# =============================================================================
import sys
import argparse
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from utapi.utra.utra_api_tcp import UtraApiTcp
from utapi.utra.utra_flxie_api import UtraFlxiE2Api

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'ubot demo'
    parser.add_argument("--ip", help=" ", default="127.0.0.1", type=str)
    args = parser.parse_args()

    ubot = UtraApiTcp(args.ip)
    fixi = UtraFlxiE2Api(ubot, 101)

    ret1, uuid = fixi.get_uuid()
    print("et_uuid: %d, uuid = %s" % (ret1, uuid))
    ret1, version = fixi.get_sw_version()
    print("et_sw_version: %d, version = %s" % (ret1, version))
    ret1, version = fixi.get_hw_version()
    print("et_hw_version: %d, version = %s" % (ret1, version))
    print(" ")

    ret1, value = fixi.get_temp_limit()
    print("et_temp_limit: %d, value = %d %d" % (ret1, value[0], value[1]))
    ret1, value = fixi.get_volt_limit()
    print("et_volt_limit: %d, value = %d %d" % (ret1, value[0], value[1]))
    ret1, value = fixi.get_curr_limit()
    print("et_curr_limit: %d, value = %f" % (ret1, value))
    print(" ")

    ret, value = fixi.get_motion_mode()
    print("et_motion_mode  : %d, value = %d" % (ret, value))
    ret, value = fixi.get_motion_enable()
    print("et_motion_enable: %d, value = %d" % (ret, value))
    ret, value = fixi.get_temp_driver()
    print("et_temp_driver  : %d, value = %.1f" % (ret, value))
    ret, value = fixi.get_temp_motor()
    print("et_temp_motor   : %d, value = %.1f" % (ret, value))
    ret, value = fixi.get_bus_volt()
    print("et_bus_volt     : %d, value = %.1f" % (ret, value))
    ret, value = fixi.get_bus_curr()
    print("et_bus_curr     : %d, value = %.1f" % (ret, value))
    ret, value = fixi.get_error_code()
    print("et_error_code   : %d, value = %d" % (ret, value))
    print(" ")

    ret, value = fixi.get_vel_limit_min()
    print("et_vel_limit_min : %d, value = %f" % (ret, value))
    ret, value = fixi.get_vel_limit_max()
    print("et_vel_limit_max : %d, value = %f" % (ret, value))
    ret, value = fixi.get_tau_limit_min()
    print("et_tau_limit_min : %d, value = %f" % (ret, value))
    ret, value = fixi.get_tau_limit_max()
    print("et_tau_limit_max : %d, value = %f" % (ret, value))
    print(" ")

    ret, value = fixi.get_pos_target()
    print("et_pos_target : %d, value = %f" % (ret, value))
    ret, value = fixi.get_pos_current()
    print("et_pos_current: %d, value = %f" % (ret, value))
    ret, value = fixi.get_vel_current()
    print("et_vel_current: %d, value = %f" % (ret, value))
    ret, value = fixi.get_tau_target()
    print("et_tau_target : %d, value = %f" % (ret, value))
    ret, value = fixi.get_tau_current()
    print("et_tau_current: %d, value = %f" % (ret, value))

    ret, pid_p = fixi.get_pos_pidp()
    print("et_pos_pid    : %d, pid_p = %d" % (ret, pid_p))
    ret, pid_p = fixi.get_vel_pidp()
    ret, pid_i = fixi.get_vel_pidi()
    print("et_vel_pid    : %d, pid_p = %d, pid_p = %d" % (ret, pid_p, pid_i))
    ret, pid_p = fixi.get_tau_pidp()
    ret, pid_i = fixi.get_tau_pidi()
    print("et_tau_pid    : %d, pid_p = %d, pid_p = %d\n" % (ret, pid_p, pid_i))

    ret, value = fixi.get_pos_smooth_cyc()
    print("et_pos_smooth_cyc: %d, value = %d" % (ret, value))
    ret, value = fixi.get_vel_smooth_cyc()
    print("et_vel_smooth_cyc: %d, value = %d" % (ret, value))
    ret, value = fixi.get_tau_smooth_cyc()
    print("et_tau_smooth_cyc: %d, value = %d" % (ret, value))
