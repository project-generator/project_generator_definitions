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
import glob

from os.path import join, normpath, splitext, isfile, dirname, basename
from os import listdir, getcwd

from .tools import UvisionDefinition, UvisionDefinition5, IARDefinitions, CoIDEdefinitions
from .target.targets import PROGENDEF_TARGETS

def _load_record(file):
    project_file = open(file)
    config = yaml.load(project_file)
    project_file.close()
    return config

class ProGenMcus:

    def __init__(self):
        mcu_files = glob.glob(join(dirname(__file__), 'mcu', '*', '*.yaml'))
        self.mcus = {}
        for m in mcu_files:
            self.mcus[splitext(basename(m))[0]] = m

    def get_mcus(self):
        return list(self.mcus.keys())

    def get_mcu_record(self, mcu):
        if mcu in self.get_mcus():
            mcu_path = self.mcus[mcu]
            return _load_record(mcu_path)
        else:
            return None

class ProGenTargets:

    def __init__(self):
        self.targets = PROGENDEF_TARGETS

    def get_targets(self):
        return list(self.targets.keys())

    def get_mcu_record(self, target):
        if target in self.get_targets():
            mcu_path = self.targets[target]['mcu']
            mcu_path = normpath(mcu_path)
            mcu_path = join(dirname(__file__), mcu_path) + '.yaml'
            return _load_record(mcu_path)
        else:
            return None

    def get_debugger(self, target):
        try:
            debugger = self.targets[target]['debugger']
        except KeyError:
            debugger = None
        return debugger

class ProGenDef:

    TOOL_SPECIFIC = {
        'uvision': UvisionDefinition,
        'uvision5': UvisionDefinition5,
        'iar':     IARDefinitions,
        'coide':   CoIDEdefinitions
    }

    def __init__(self, tool=None):
        """ Tool can be either tool_specific or None=only generic available """
        self.targets = ProGenTargets()
        self.mcus = ProGenMcus()
        # list of all mcu and targets. User can request any of these, we figure it out
        self.targets_mcu_list = self.targets.get_targets() + self.mcus.get_mcus()
        self.definitions = None
        self.tool = None
        if tool != None:
            try:
                self.definitions = self.TOOL_SPECIFIC[tool]()
                self.tool = tool
            except KeyError:
                pass

    def get_targets(self):
        return self.targets.get_targets()

    def get_mcus(self):
        return self.mcus.get_mcus()

    def get_mcu_core(self, target):
        if target not in self.targets_mcu_list:
            return None
        mcu_record = self.targets.get_mcu_record(target) if self.mcus.get_mcu_record(target) is None else self.mcus.get_mcu_record(target)
        try:
            return mcu_record['mcu']['core']
        except KeyError:
            return None

    def get_tool_definition(self, target):
        """ Returns tool specific dic or None if it does not exist for defined tool """
        if target not in self.targets_mcu_list:
            logging.debug("Target not found in definitions")
            return None
        mcu_record = self.targets.get_mcu_record(target) if self.mcus.get_mcu_record(target) is None else self.mcus.get_mcu_record(target)
        try:
            return mcu_record['tool_specific'][self.tool]
        except KeyError:
            return None

    def is_supported(self, target):
        """ Returns True if target is supported by definitions """
        if target.lower() not in self.targets_mcu_list:
            logging.debug("Target not found in definitions")
            return False
        mcu_record = self.targets.get_mcu_record(target) if self.mcus.get_mcu_record(target) is None else self.mcus.get_mcu_record(target)
        # Look at tool specific options which define tools supported for target
        # TODO: we might create a list of what tool requires
        if self.tool:
            # tool_specific requested look for it
            try:
                for k,v in mcu_record['tool_specific'].items():
                    if k == self.tool:
                        return True
            except (TypeError, KeyError) as err:
                pass
            return False
        else:
            # supports generic part (mcu part)
            return True

    def get_debugger(self, target):
        return self.targets.get_debugger(target)

    def mcu_create(self, mcu_name, template_file):
        if self.definitions == None:
            logging.debug("No tool definitoned, can't parse the template file")
            return False
        data = self.definitions.get_mcu_definition(template_file)
        data['mcu']['name'] = [mcu_name]
        # we got target, now damp it to root using target.yaml file
        # we can make it better, and ask for definitions repo clone, and add it
        # there, at least to MCU folder
        with open(join(getcwd(), mcu_name + '.yaml'), 'wt') as f:
            f.write(yaml.safe_dump(data, indent=4, default_flow_style=False, width=200))
        return True
