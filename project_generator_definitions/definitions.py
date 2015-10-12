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
from os import listdir, getcwd

from .tools import UvisionDefinition, IARDefinitions

TEMPLATE_DIR_TARGET = join(dirname(__file__), 'target')

class ProGenMCU:

    def _load_record(self, file):
        project_file = open(file)
        config = yaml.load(project_file)
        project_file.close()
        return config

    def get_mcu_record(self, target):
        target_path = join(self.TEMPLATE_DIR_TARGET, target + '.yaml')
        target_record = self._load_record(target_path)
        mcu_path = target_record['target']['mcu']
        mcu_path = normpath(mcu_path[0])
        mcu_path = join(dirname(__file__), mcu_path) + '.yaml'
        return self._load_record(mcu_path)

class ProGenTarget:

    def __init__(self):
        self.targets = [splitext(f)[0] for f in listdir(TEMPLATE_DIR_TARGET) if isfile(join(TEMPLATE_DIR_TARGET,f))]

    def get_targets(self):
        return self.targets

class ProGenDef(ProGenMCU, ProGenTarget):

    TOOLS = {
        'uvision': UvisionDefinition,
        'iar':     IARDefinitions,
    }

    def __init__(self, tool):
        ProGenTarget.__init__(self)
        try:
            self.definitions = self.TOOLS[tool]()
        except KeyError:
            logging.debug("Tool %s not supported." % tool)
        self.tool = tool

    def get_mcu_core(self, target):
        if target not in self.targets:
            return None
        mcu_record = self.get_mcu_record(target)
        try:
            return mcu_record['mcu']['core']
        except KeyError:
            return None

    def get_tool_def(self, target):
        if target not in self.targets:
            return None
        mcu_record = self.get_mcu_record(target)
        try:
            return mcu_record['tool_specific'][self.tool]
        except KeyError:
            return None

    def is_supported(self, target):
        if target.lower() not in self.targets:
            return False
        mcu_record = self.get_mcu_record(target)
        # Look at tool specific options which define tools supported for target
        # TODO: we might create a list of what tool requires
        try:
            for k,v in mcu_record['tool_specific'].items():
                if k == self.tool:
                    return True
        except KeyError:
            pass
        return False

    def mcu_create(self, mcu_name, template_file):
        data = self.definitions.get_mcu_definition(template_file)
        data['mcu']['name'] = [mcu_name]
        # we got target, now damp it to root using target.yaml file
        # we can make it better, and ask for definitions repo clone, and add it
        # there, at least to MCU folder
        with open(join(getcwd(), mcu_name + '.yaml'), 'wt') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False, width=200))
        return 0