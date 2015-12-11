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

from project_generator_definitions.definitions import ProGenTargets
from project_generator_definitions.target.targets import PROGENDEF_TARGETS

class TestAllTargets(TestCase):

    """test all targets"""

    def setUp(self):
        self.progen_target = ProGenTargets()
        self.targets_list = self.progen_target.get_targets()

    def test_targets_validity(self):
        # Cehck for required info for targets
        for target in self.targets_list:
            mcu_path = PROGENDEF_TARGETS[target]
            assert mcu_path

    def test_targets_mcu_validity(self):
        # Check for required info in mcu
        for target in self.targets_list:
            mcu = self.progen_target.get_mcu_record(target)
            assert mcu['mcu']
            assert mcu['mcu']['name'][0]
            assert mcu['mcu']['core'][0]

    def test_targets_mcu_tool_specific_uvision_validity(self):
        for target in self.targets_list:
            mcu = self.progen_target.get_mcu_record(target)
            if 'tool_specific' in mcu:
                try:
                    for tool in mcu['tool_specific'].keys():
                        if tool == 'uvision':
                            assert mcu['tool_specific']['uvision']['TargetOption']
                            assert mcu['tool_specific']['uvision']['TargetOption']['Device'][0]
                            # DeviceId might be 0
                            assert mcu['tool_specific']['uvision']['TargetOption']['DeviceId'][0] != -1
                except KeyError:
                    pass

    def test_targets_mcu_tool_specific_iar_validity(self):
        for target in self.targets_list:
            mcu = self.progen_target.get_mcu_record(target)
            if 'tool_specific' in mcu:
                for tool in mcu['tool_specific'].keys():
                    if tool == 'iar' :
                        assert mcu['tool_specific']['iar']['OGChipSelectEditMenu']['state'][0]
                        assert mcu['tool_specific']['iar']['OGCoreOrChip']['state'][0]

    def test_targets_mcu_tool_specific_coide_validity(self):
        for target in self.targets_list:
            mcu = self.progen_target.get_mcu_record(target)
            if 'tool_specific' in mcu:
                for tool in mcu['tool_specific'].keys():
                    if tool == 'coide' :
                        assert mcu['tool_specific']['coide']['Device']['manufacturerName'][0]
                        assert mcu['tool_specific']['coide']['Device']['chipId'][0]
                        assert mcu['tool_specific']['coide']['Device']['chipName'][0]
                        assert mcu['tool_specific']['coide']['DebugOption']['defaultAlgorithm'][0]
