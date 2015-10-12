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
        # check validity of template otherwise we fail with keyerror, same for IAR
        project_file = join(getcwd(), project_file)
        uvproj_dic = xmltodict.parse(file(project_file), dict_constructor=dict)
        # Generic Target, should get from Target class !
        mcu = MCU_TEMPLATE

        mcu['tool_specific'] = {
            # legacy device
            'uvision' : {
                'TargetOption' : {
                    'Device' : [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['Device']],
                    'DeviceId' : [int(uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['DeviceId'])],

                }
            }
        }

        if 'RegisterFile' in uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']:
            mcu['tool_specific']['uvision']['TargetOption']['RegisterFile'] = [uvproj_dic['Project']['Targets']['Target']['TargetOption']['TargetCommonOption']['RegisterFile']]

        return mcu

class IARDefinitions:

    def get_mcu_definition(self, project_file):
        """ Parse project file to get mcu definition """
        # TODO: check the extension here if it's valid IAR project or we
        # should at least check if syntax is correct check something IAR defines and return error if not
        project_file = join(getcwd(), project_file)
        ewp_dic = xmltodict.parse(file(project_file), dict_constructor=dict)

        mcu = MCU_TEMPLATE

        # we take 0 configuration or just configuration, as multiple configuration possibl
        # debug, release, for mcu - does not matter, try and adjust
        try:
            index_general = self._get_option(ewp_dic['project']['configuration'][0]['settings'], 'General')
            configuration = ewp_dic['project']['configuration'][0]
        except KeyError:
            index_general = self._get_option(ewp_dic['project']['configuration']['settings'], 'General')
            configuration = ewp_dic['project']['configuration']
        index_option = self._get_option(configuration['settings'][index_general]['data']['option'], 'OGChipSelectEditMenu')
        OGChipSelectEditMenu = configuration['settings'][index_general]['data']['option'][index_option]

        mcu['tool_specific'] = {
            'iar' : {
                'OGChipSelectEditMenu' : {
                    'state' : [OGChipSelectEditMenu['state'].replace('\t', ' ', 1)],
                },
                'OGCoreOrChip' : {
                    'state' : [1],
                },
            }
        }
        return mcu
