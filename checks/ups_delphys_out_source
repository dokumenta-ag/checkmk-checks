#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 DOKUMENTA AG - License: GNU General Public License v2

def inventory_ups_delphys_out_source(info):
    if info:
        return [(None, None)]


def check_ups_delphys_out_source(_no_item, _no_params, info):

    # This is from the old (v5.01) MIB
    ups_delphys_source_states = {
        1: (3, "Other"),
        2: (2, "Offline"),
        3: (0, "Normal"),
        4: (1, "Internal Maintenance Bypass"),
        5: (2, "On battery"),
        6: (0, "Booster"),
        7: (0, "Reducer"),
        8: (0, "Standby"),
        9: (0, "Eco mode"),
    }

    return ups_delphys_source_states[int(info[0][0])]


check_info["ups_delphys_out_source"] = {
    "inventory_function": inventory_ups_delphys_out_source,
    "check_function": check_ups_delphys_out_source,
    "service_description": "Output Source",
    "snmp_info": (".1.3.6.1.4.1.4555.1.1.5.1.4", ["1"]),
    "snmp_scan_function": lambda oid: oid(".1.3.6.1.2.1.1.2.0") == ".1.3.6.1.4.1.4555.1.1.5",
}