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

from .tools import UvisionDefinition, IARDefinitions, CoIDEdefinitions

TEMPLATE_DIR_TARGET = join(dirname(__file__), 'target')

def _load_record(file):
    project_file = open(file)
    config = yaml.load(project_file)
    project_file.close()
    return config

class ProGenTargets:

    def __init__(self):
        self.targets = [splitext(f)[0] for f in listdir(TEMPLATE_DIR_TARGET) if isfile(join(TEMPLATE_DIR_TARGET,f))]

    def get_targets(self):
        return self.targets

    def get_target_record(self, target):
        target_path = join(TEMPLATE_DIR_TARGET, target + '.yaml')
        return _load_record(target_path)

    def get_mcu_record(self, target):
        target_path = join(TEMPLATE_DIR_TARGET, target + '.yaml')
        target_record = _load_record(target_path)
        mcu_path = target_record['target']['mcu']
        mcu_path = normpath(mcu_path[0])
        mcu_path = join(dirname(__file__), mcu_path) + '.yaml'
        return _load_record(mcu_path)


class ProGenDef(ProGenTargets):

    # TODO: add a generic function to get just core
    TOOL_SPECIFIC = {
        'uvision': UvisionDefinition,
        'iar':     IARDefinitions,
        'coide':   CoIDEdefinitions
    }

    def __init__(self, tool=None):
        """ Tool can be either tool_specific or None=generic"""
        ProGenTargets.__init__(self)
        self.definitions = None
        self.tool = None
        if tool != None:
            try:
                self.definitions = self.TOOL_SPECIFIC[tool]()
                self.tool = tool
            except KeyError:
                logging.debug("Tool %s is not supported")

    def get_mcu_core(self, target):
        if target not in self.targets:
            return None
        mcu_record = self.get_mcu_record(target)
        try:
            return mcu_record['mcu']['core']
        except KeyError:
            return None

    def get_tool_definition(self, target):
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
        if self.tool:
            # tool_specific requested look for it
            try:
                for k,v in mcu_record['tool_specific'].items():
                    if k == self.tool:
                        return True
            except KeyError:
                pass
            return False
        else:
            # supports generic part (mcu part)
            return True

    def mcu_create(self, mcu_name, template_file):
        if self.definitions == None:
            return False
        data = self.definitions.get_mcu_definition(template_file)
        data['mcu']['name'] = [mcu_name]
        # we got target, now damp it to root using target.yaml file
        # we can make it better, and ask for definitions repo clone, and add it
        # there, at least to MCU folder
        with open(join(getcwd(), mcu_name + '.yaml'), 'wt') as f:
            f.write(yaml.safe_dump(data, default_flow_style=False, width=200))
        return True
