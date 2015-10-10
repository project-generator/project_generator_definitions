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

import yaml
import subprocess
import logging

from os.path import join, normpath, splitext, isfile, dirname
from os import listdir

class ProGenMCU:

    MCU_TEMPLATE = {
        'mcu' : {
            'vendor' : ['Manually add vendor (st, freescale, etc) instead of this text'],
            'name' : [''],
            'core' : ['Manually add core (cortex-mX) instead of this text'],
        },
    }

    TEMPLATE_DIR_MCU = join(dirname(__file__), 'mcu')

    def get_mcu_definition(self):
        return self.MCU_TEMPLATE

    def get_mcu_record(self, target):
        target_path = join(self.TEMPLATE_DIR_TARGET, target + '.yaml')
        target_record = self._load_record(target_path)
        mcu_path = target_record['target']['mcu']
        mcu_path = normpath(mcu_path[0])
        mcu_path = join(dirname(__file__), mcu_path) + '.yaml'
        return self._load_record(mcu_path)

class ProGenTarget:

    TEMPLATE_DIR_TARGET = join(dirname(__file__), 'target')

    def __init__(self):
        self.targets = [splitext(f)[0] for f in listdir(self.TEMPLATE_DIR_TARGET) if isfile(join(self.TEMPLATE_DIR_TARGET,f))]

    def get_targets(self):
        return self.targets

class ProGenDef(ProGenMCU, ProGenTarget):

    def __init__(self):
        ProGenTarget.__init__(self)

    def _load_record(self, file):
        project_file = open(file)
        config = yaml.load(project_file)
        project_file.close()
        return config

    def get_mcu_core(self, target):
        if target not in self.targets:
            return None
        mcu_record = self.get_mcu_record(target)
        try:
            return mcu_record['mcu']['core']
        except KeyError:
            return None

    def get_tool_def(self, target, tool):
        if target not in self.targets:
            return None
        mcu_record = self.get_mcu_record(target)
        try:
            return mcu_record['tool_specific'][tool]
        except KeyError:
            return None

    def is_supported(self, target, tool):
        if target.lower() not in self.targets:
            return False
        mcu_record = self.get_mcu_record(target)
        # Look at tool specific options which define tools supported for target
        # TODO: we might create a list of what tool requires
        try:
            for k,v in mcu_record['tool_specific'].items():
                if k == tool:
                    return True
        except KeyError:
            pass
        return False
