#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 DOKUMENTA AG - License: GNU General Public License v2

# NOTE: Careful when replacing the *-import below with a more specific import. This can cause
# problems because it might remove variables from the check-context which are necessary for
# resolving legacy discovery results such as [("SUMMARY", "diskstat_default_levels")]. Furthermore,
# it might also remove variables needed for accessing discovery rulesets.
from cmk.base.check_legacy_includes.elphase import *  # pylint: disable=wildcard-import,unused-wildcard-import

factory_settings["ups_socomecsts_outphase_default_levels"] = {}


def parse_ups_socomecsts_outphase(info):
    parsed = {}
    parsed["Phase 1"] = {
        "frequency": int(info[0][1]) / 10.0,
        "voltage": int(info[0][3]) / 10.0,
        "current": int(info[0][4]) / 10.0,
        "power": int(info[0][5]),
        "output_load": int(info[0][6]),
    }

    if info[0][2] == "3":
        parsed["Phase 2"] = {
            "frequency": int(info[0][1]) / 10.0,
            "voltage": int(info[0][7]) / 10.0,
            "current": int(info[0][8]) / 10.0,
            "power": int(info[0][9]),
            "output_load": int(info[0][10]),
        }

        parsed["Phase 3"] = {
            "frequency": int(info[0][1]) / 10.0,
            "voltage": int(info[0][11]) / 10.0,
            "current": int(info[0][12]) / 10.0,
            "power": int(info[0][13]),
            "output_load": int(info[0][14]),
        }

    return parsed


check_info["ups_socomecsts_outphase"] = {
    "parse_function": parse_ups_socomecsts_outphase,
    "inventory_function": discover(),
    "check_function": check_elphase,
    "service_description": "Output %s",
    "has_perfdata": True,
    "default_levels_variable": "ups_socomecsts_outphase_default_levels",
    "group": "ups_outphase",
    "snmp_info": (
        ".1.3.6.1.4.1.4555.1.1.10.1.5",
        [
            "1",  # stsOutputLoadStatus
            "3",  # stsOutputFrequency
            "5",  # stsOutputNumLines
            "6.1.2.1",  # stsOutputVoltage1
            "6.1.3.1",  # stsOutputCurrent1
            "6.1.5.1",  # stsOutputPower1
            "4",  # stsOutputLoad1
            "6.1.2.2",  # stsOutputVoltage2
            "6.1.3.2",  # stsOutputCurrent2
            "6.1.5.2",  # stsOutputPower2
            "4",  # stsOutputLoad2
            "6.1.2.3",  # stsOutputVoltage3
            "6.1.3.3",  # stsOutputCurrent3
            "6.1.5.3",  # stsOutputPower3
            "4",  # stsOutputLoad3
        ],
    ),
    "snmp_scan_function": lambda oid: oid(".1.3.6.1.2.1.1.2.0") == ".1.3.6.1.4.1.4555.1.1.10.1.5",
}