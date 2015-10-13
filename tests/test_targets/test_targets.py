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

class TestAllTargets(TestCase):

    """test all targets"""

    def setUp(self):
        self.progen_target = ProGenTargets()
        self.targets_list = self.progen_target.get_targets()

    def test_targets_validity(self):
        # Cehck for required info for targets
        for target in self.targets_list:
            record = self.progen_target.get_target_record(target)
            assert record['target']['name'][0]
            assert record['target']['mcu'][0]

    def test_targets_mcu_validity(self):
        # Check for required info in mcu
        for target in self.targets_list:
            mcu = self.progen_target.get_mcu_record(target)
            assert mcu['mcu'][0]
            assert mcu['mcu']['name'][0]
            assert mcu['mcu']['core'][0]
