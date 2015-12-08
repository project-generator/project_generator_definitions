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

from unittest import TestCase

from project_generator_definitions.definitions import ProGenMcus

class TestAllMcus(TestCase):

    """test all targets"""

    def setUp(self):
        self.progen_mcus = ProGenMcus()
        self.mcus_list = self.progen_mcus.get_mcus()

    def test_mcu_validity(self):
        # Check for required info in mcu
        for mcu in self.mcus_list:
            mcu_rec = self.progen_mcus.get_mcu_record(mcu)
            assert mcu_rec['mcu']
            assert mcu_rec['mcu']['name'][0]
            assert mcu_rec['mcu']['core'][0]

    def test_mcu_tool_specific_uvision_validity(self):
        for target in self.mcus_list:
            mcu = self.progen_mcus.get_mcu_record(target)
            if mcu['tool_specific']:
                try:
                    for tool in mcu['tool_specific'].keys():
                        if tool == 'uvision':
                            assert mcu['tool_specific']['uvision']['TargetOption']
                            assert mcu['tool_specific']['uvision']['TargetOption']['Device'][0]
                            # DeviceId might be 0
                            assert mcu['tool_specific']['uvision']['TargetOption']['DeviceId'][0] != -1
                except KeyError:
                    pass

    def test_mcu_tool_specific_iar_validity(self):
        for mcu in self.mcus_list:
            mcu = self.progen_mcus.get_mcu_record(mcu)
            if mcu['tool_specific']:
                for tool in mcu['tool_specific'].keys():
                    if tool == 'iar' :
                        assert mcu['tool_specific']['iar']['OGChipSelectEditMenu']['state'][0]
                        assert mcu['tool_specific']['iar']['OGCoreOrChip']['state'][0]

    def test_mcu_tool_specific_coide_validity(self):
        for mcu in self.mcus_list:
            mcu = self.progen_mcus.get_mcu_record(mcu)
            if mcu['tool_specific']:
                for tool in mcu['tool_specific'].keys():
                    if tool == 'coide' :
                        assert mcu['tool_specific']['coide']['Device']['manufacturerName'][0]
                        assert mcu['tool_specific']['coide']['Device']['chipId'][0]
                        assert mcu['tool_specific']['coide']['Device']['chipName'][0]
                        assert mcu['tool_specific']['coide']['DebugOption']['defaultAlgorithm'][0]
