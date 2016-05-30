# Copyright 2015 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xmltodict
import logging

from os import getcwd
from os.path import join

MCU_TEMPLATE = {
    'mcu' : {
        'vendor' : ['Manually add vendor (st, freescale, etc) instead of this text'],
        'name' : [''],
        'core' : ['Manually add core (cortex-mX) instead of this text'],
    },
}

class UvisionDefinition:

    def get_mcu_definition(self, project_file):
        """ Parse project file to get mcu definition """
        project_file = join(getcwd(), project_file)
        uvproj_dic = xmltodict.parse(file(project_file), dict_constructor=dict)
        # Generic Target, should get from Target class !
        mcu = MCU_TEMPLATE

        try:
            mcu['tool_specific'] = {
                # legacy device
                'uvision' : {
                    'TargetOption' : {
                        'Device' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Device']],
                        'DeviceId' : [None if not uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['DeviceId'] else 
                            int(uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['DeviceId'])],
                        'Vendor' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Vendor']],
                        'Cpu' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Cpu']],
                        'FlashDriverDll' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['FlashDriverDll']],
                        'SFDFile' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['SFDFile']],
                        'RegisterFile': [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['RegisterFile']],
                    }
                }
            }
        except KeyError:
            # validity check for uvision project
            logging.debug("The project_file %s seems to be not valid .uvproj file.")
            return mcu

        return mcu

class UvisionDefinition5:

    # TODO: create comomn uvision class (4 and 5 have many common keys)
    def get_mcu_definition(self, project_file):
        """ Parse project file to get mcu definition """
        project_file = join(getcwd(), project_file)
        uvproj_dic = xmltodict.parse(file(project_file), dict_constructor=dict)
        # Generic Target, should get from Target class !
        mcu = MCU_TEMPLATE

        try:
            mcu['tool_specific'] = {
                'uvision5' : {
                    'TargetOption' : {
                        'Device' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Device']],
                        'DeviceId' : [None if not uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['DeviceId'] else 
                            int(uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['DeviceId'])],
                        'Vendor' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Vendor']],
                        'Cpu' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Cpu']],
                        'FlashDriverDll' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['FlashDriverDll']],
                        'SFDFile' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['SFDFile']],
                        'PackID' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['PackID']],
                        'RegisterFile': [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['RegisterFile']],
                    }
                }
            }
        except KeyError:
            # validity check for uvision project
            logging.debug("The project_file %s seems to be not valid .uvproj file.")
            return mcu

        return mcu


class IARDefinitions:

    def _get_option(self, settings, find_key):
        for option in settings:
            if option['name'] == find_key:
                return settings.index(option)

    def get_mcu_definition(self, project_file):
        """ Parse project file to get mcu definition """
        # TODO: check the extension here if it's valid IAR project or we
        # should at least check if syntax is correct check something IAR defines and return error if not
        project_file = join(getcwd(), project_file)
        ewp_dic = xmltodict.parse(file(project_file), dict_constructor=dict)

        mcu = MCU_TEMPLATE

        try:
            ewp_dic['project']['configuration']
        except KeyError:
            # validity check for iar project
            logging.debug("The project_file %s seems to be not valid .ewp file.")
            return mcu

        # Fill in only must-have values, fpu will be added if defined for mcu
        mcu['tool_specific'] = {
            'iar' : {
                # MCU selection
                'OGChipSelectEditMenu' : {
                    'state' : [],
                },
                # we use mcu
                'OGCoreOrChip' : {
                    'state' : [1],
                },
            }
        }


        # we take 0 configuration or just configuration, as multiple configuration possible
        # debug, release, for mcu - does not matter, try and adjust
        try:
            index_general = self._get_option(ewp_dic['project']['configuration'][0]['settings'], 'General')
            configuration = ewp_dic['project']['configuration'][0]
        except KeyError:
            index_general = self._get_option(ewp_dic['project']['configuration']['settings'], 'General')
            configuration = ewp_dic['project']['configuration']
        index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'OGChipSelectEditMenu')
        OGChipSelectEditMenu = configuration['settings'][index_general]['data']['option'][index_option]
        mcu['tool_specific']['iar']['OGChipSelectEditMenu']['state'].append(OGChipSelectEditMenu['state'].replace('\t', ' ', 1))
        # we keep this as the internal version. FPU - version 1, FPU2 version 2. 
        # TODO:We shall look at IAR versioning to get this right
        fileVersion = 1
        try:
            if self._get_option(configuration['settings'][index_general]['data']['option'], 'FPU2'):
                fileVersion = 2
        except TypeError:
            pass

        index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'GBECoreSlave')
        GBECoreSlave = configuration['settings'][index_general]['data']['option'][index_option]
        mcu['tool_specific']['iar']['GBECoreSlave'] = { 'state': [int(GBECoreSlave['state'])] }

        if fileVersion == 2:
            index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'GFPUCoreSlave2')
            GFPUCoreSlave2 = configuration['settings'][index_general]['data']['option'][index_option]
            mcu['tool_specific']['iar']['GFPUCoreSlave2'] = { 'state': [int(GFPUCoreSlave2['state'])] }
            index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'CoreVariant')
            CoreVariant = configuration['settings'][index_general]['data']['option'][index_option]
            mcu['tool_specific']['iar']['CoreVariant'] = { 'state': [int(CoreVariant['state'])] }
        else:
            index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'GFPUCoreSlave')
            GFPUCoreSlave = configuration['settings'][index_general]['data']['option'][index_option]
            mcu['tool_specific']['iar']['GFPUCoreSlave'] = { 'state': [int(GFPUCoreSlave['state'])] }
            index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'Variant')
            Variant = configuration['settings'][index_general]['data']['option'][index_option]
            mcu['tool_specific']['iar']['Variant'] = { 'state': [int(Variant['state'])] }
        return mcu

class CoIDEdefinitions:

    def _coproj_find_option(self, option_dic, key_to_find, value_to_match):
        i = 0
        for option in option_dic:
            for k,v in option.items():
                if k == key_to_find and value_to_match == v:
                    return i
            i += 1
        return None

    def get_mcu_definition(self, project_file):
        """ Parse project file to get mcu definition """
        project_file = join(getcwd(), project_file)
        coproj_dic = xmltodict.parse(file(project_file), dict_constructor=dict)

        mcu = MCU_TEMPLATE

        IROM1_index = self._coproj_find_option(coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'], '@name', 'IROM1')
        IROM2_index = self._coproj_find_option(coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'], '@name', 'IROM2')
        IRAM1_index = self._coproj_find_option(coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'], '@name', 'IRAM1')
        IRAM2_index = self._coproj_find_option(coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'], '@name', 'IRAM2')
        defaultAlgorithm_index = self._coproj_find_option(coproj_dic['Project']['Target']['DebugOption']['Option'], '@name', 'org.coocox.codebugger.gdbjtag.core.defaultAlgorithm')

        mcu['tool_specific'] = {
            'coide' : {
                'Device' : {
                    'manufacturerId' : [coproj_dic['Project']['Target']['Device']['@manufacturerId']],
                    'manufacturerName': [coproj_dic['Project']['Target']['Device']['@manufacturerName']],
                    'chipId': [coproj_dic['Project']['Target']['Device']['@chipId']],
                    'chipName': [coproj_dic['Project']['Target']['Device']['@chipName']],
                },
                'DebugOption': {
                    'defaultAlgorithm': [coproj_dic['Project']['Target']['DebugOption']['Option'][defaultAlgorithm_index]['@value']],
                },
                'MemoryAreas': {
                    'IROM1': {
                        'name': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM1_index]['@name']],
                        'size': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM1_index]['@size']],
                        'startValue': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM1_index]['@startValue']],
                        'type': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM1_index]['@type']],
                    },
                    'IRAM1': {
                        'name': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM1_index]['@name']],
                        'size': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM1_index]['@size']],
                        'startValue': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM1_index]['@startValue']],
                        'type': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM1_index]['@type']],
                    },
                    'IROM2': {
                        'name': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM2_index]['@name']],
                        'size': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM2_index]['@size']],
                        'startValue': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM2_index]['@startValue']],
                        'type': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IROM2_index]['@type']],
                    },
                    'IRAM2': {
                        'name': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM2_index]['@name']],
                        'size': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM2_index]['@size']],
                        'startValue': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM2_index]['@startValue']],
                        'type': [coproj_dic['Project']['Target']['BuildOption']['Link']['MemoryAreas']['Memory'][IRAM2_index]['@type']],
                    }
                }
            }
        }
        return mcu
