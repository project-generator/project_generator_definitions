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

# Targets mapping to mcu
# should be : target_name['mcu'] path to mcu file
#             target_name['debugger'] debugger to be set up, not defined - None
#                                     jtag/swd interface
PROGENDEF_TARGETS = {
    'arch-ble': {
        'mcu':'mcu/nordic/nrf51822',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
     },
    'arch-pro': {
        'mcu':'mcu/nxp/lpc1768',
     },
    'arch-max': {
        'mcu':'mcu/st/stm32f407vg',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
     },
    'dfcm-nnn40': {
        'mcu':'mcu/nordic/nrf51822',
     },
    'mbed-lpc1768': {
        'mcu':'mcu/nxp/lpc1768',
     },
    'disco-f334c8': {
        'mcu':'mcu/st/stm32f334x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-f407vg': {
        'mcu':'mcu/st/stm32f407vg',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-f746ng': {
        'mcu':'mcu/st/stm32f746ng',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-f769ni': {
        'mcu':'mcu/st/stm32f769ni',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-l053c8': {
        'mcu':'mcu/st/stm32l053x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-l072cz-lrwan1': {
        'mcu':'mcu/st/stm32l072xz',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-l475vg-iot01a': {
        'mcu':'mcu/st/stm32l475vg',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-l476vg': {
        'mcu':'mcu/st/stm32l476vg',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-f469ni': {
        'mcu':'mcu/st/stm32f469nihx',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'disco-f429zi': {
        'mcu':'mcu/st/stm32f429zi',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'efm32gg-stk': {
        'mcu':'mcu/siliconlabs/efm32gg990f1024',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'efm32hg-stk': {
        'mcu':'mcu/siliconlabs/efm32hg322f64',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'efm32wg-stk': {
        'mcu':'mcu/siliconlabs/efm32wg990f256',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'efm32zg-stk': {
        'mcu':'mcu/siliconlabs/efm32zg222f32',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'efm32lg-stk': {
        'mcu':'mcu/siliconlabs/efm32lg990f256',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'efm32pg-stk': {
        'mcu':'mcu/siliconlabs/efm32pg1b200f256gm48',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'frdm-k20d50m': {
        'mcu':'mcu/freescale/mk20dx128xxx5',
    },
    'teensy-31': {
        'mcu':'mcu/freescale/mk20dx256xxx7',
    },
    'frdm-k22f': {
        'mcu':'mcu/freescale/mk22dn512xxx5',
    },
    'frdm-k64f': {
        'mcu':'mcu/freescale/mk64fn1m0xxx12',
     },
    'k64f': {
        'mcu':'mcu/freescale/mk64fn1m0xxx12',
     },
    'frdm-kl05z': {
        'mcu':'mcu/freescale/mkl05z32xxx4',
    },
    'frdm-kl25z': {
        'mcu':'mcu/freescale/mkl25z128xxx4',
    },
    'frdm-kl43z': {
        'mcu':'mcu/freescale/mkl43z256xxx4',
    },
    'frdm-kl46z': {
        'mcu':'mcu/freescale/mkl46z256xxx4',
    },
    'hexiwear-k64f': {
        'mcu':'mcu/freescale/mk64fn1m0xxx12',
     },
    'hrm1017': {
        'mcu':'mcu/nordic/nrf51822',
    },
    'ty51822r3': {
        'mcu':'mcu/nordic/nrf51822',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'lpcxpresso-lpc54608': {
        'mcu':'mcu/nxp/lpc54608_et180',
    },
    'lpcxpresso-lpc54114': {
        'mcu':'mcu/nxp/lpc54114_bd64',
    },
    'maxwsnenv': {
        'mcu':'mcu/maxim/max32600x85',
    },
    'max32600mbed': {
        'mcu':'mcu/maxim/max32600x85',
    },
    'max32620hsp': {
        'mcu':'mcu/maxim/max32620',
    },
    'max32620mbed': {
        'mcu':'mcu/maxim/max32620',
    },
    'max32625mbed': {
        'mcu':'mcu/maxim/max32625',
    },
    'mbed-lpc11u24': {
        'mcu':'mcu/nxp/lpc11u24_201',
    },
    'bbc-microbit': {
        'mcu':'mcu/nordic/nrf51822',
    },
    'mkit': {
        'mcu':'mcu/nordic/nrf51822',
    },
    'mtm-mtconnect04s': {
        'mcu':'mcu/nordic/nrf51822',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
     },
    'nrf51-dk': {
        'mcu':'mcu/nordic/nrf51822',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'nrf51-dongle': {
        'mcu':'mcu/nordic/nrf51822',
    },
    'nu-nuc472-nutiny': {
        'mcu':'mcu/nuvoton/nuc472hi8ae',
    },
    'numbed-nuc472': {
        'mcu':'mcu/nuvoton/nuc472hi8ae',
        'debugger': {
            'name': 'nu-link',
            'interface': 'swd',
        }
    },
    'numaker-pfm-nuc472': {
        'mcu':'mcu/nuvoton/nuc472hi8ae',
        'debugger': {
            'name': 'nu-link',
            'interface': 'swd',
        }
    },
    'nutiny-m453': {
        'mcu':'mcu/nuvoton/m453vg6ae',
        'debugger': {
            'name': 'nu-link',
            'interface': 'swd',
        }
    },
    'numbed-m453': {
        'mcu':'mcu/nuvoton/m453vg6ae',
        'debugger': {
            'name': 'nu-link',
            'interface': 'swd',
        }
    },
    'numaker-pfm-m453': {
        'mcu':'mcu/nuvoton/m453vg6ae',
        'debugger': {
            'name': 'nu-link',
            'interface': 'swd',
        }
    },
    'nucleo-f030r8': {
        'mcu':'mcu/st/stm32f030x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l011k4': {
        'mcu':'mcu/st/stm32l011x4',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l031k6': {
        'mcu':'mcu/st/stm32l031x6',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l053r8': {
        'mcu':'mcu/st/stm32l053x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l432kc': {
        'mcu':'mcu/st/stm32l432kc',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f031k6': {
        'mcu':'mcu/st/stm32f031x',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f042k6': {
        'mcu':'mcu/st/stm32f042x',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f070rb': {
        'mcu':'mcu/st/stm32f070rb',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f072rb': {
        'mcu':'mcu/st/stm32f072rb',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f103rb': {
        'mcu':'mcu/st/stm32f103xb',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'stm32f103ze': {
        'mcu':'mcu/st/stm32f103ze',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f091rc': {
        'mcu':'mcu/st/stm32f091rc',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f302r8': {
        'mcu':'mcu/st/stm32f302x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f303re': {
        'mcu':'mcu/st/stm32f303xe',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
     'nucleo-f303ze': {
        'mcu':'mcu/st/stm32f303ze',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f303k8': {
        'mcu':'mcu/st/stm32f303x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f334r8': {
        'mcu':'mcu/st/stm32f334x8',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f401re': {
        'mcu':'mcu/st/stm32f401xe',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f410rb': {
        'mcu':'mcu/st/stm32f410rb',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f411re': {
        'mcu':'mcu/st/stm32f411re',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
	 'nucleo-f429zi': {
        'mcu':'mcu/st/stm32f429zi',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f446re': {
        'mcu':'mcu/st/stm32f446re',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f446ze': {
        'mcu':'mcu/st/stm32f446ze',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l476rg': {
        'mcu':'mcu/st/stm32l476rg',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l073rz': {
        'mcu':'mcu/st/stm32l073xz',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-l152re': {
        'mcu':'mcu/st/stm32l152xe',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f746zg': {
        'mcu':'mcu/st/stm32f746zg',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'nucleo-f767zi': {
        'mcu':'mcu/st/stm32f767zi',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'arducleo-f051k8': {
        'mcu':'mcu/st/stm32f051x',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'ublox-c027': {
        'mcu':'mcu/nxp/lpc1768',
    },
    'seed-tinyble': {
        'mcu':'mcu/nordic/nrf51822',
    },
    'stk3700-gcc': {
        'mcu':'mcu/siliconlabs/efm32gg990f1024',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    },
    'odin-w2': {
        'mcu':'mcu/st/stm32f439zitx',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'mts-mdot-f405rg': {
        'mcu':'mcu/st/stm32f405rg',
    },
    'mts-mdot-f411re': {
        'mcu':'mcu/st/stm32f411re',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'mts-dragonfly-f411re': {
        'mcu':'mcu/st/stm32f411re',
        'debugger': {
            'name': 'st-link',
            'interface': 'swd',
        }
    },
    'mts-gambit': {
        'mcu':'mcu/freescale/mk64fn1m0xxx12',
    },
    'mote-l152rc': {
        'mcu':'mcu/st/stm32l152rc',
    },
    'rblab-nrf51822': {
        'mcu':'mcu/nordic/nrf51822',
    },
    'beetle': {
        'mcu':'mcu/arm-ssg/beetle',
        'debugger': {
            'name': 'ulink-pro',
            'interface': 'jtag',
        }
    },
    'gr-peach': {
        'mcu':'mcu/renesas/r7s721001',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'cocorico': {
        'mcu':'mcu/nxp/lpc812m101',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'ncs36510': {
        'mcu':'mcu/onsemi/ncs36510',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'tmpm366fdfg':  {
        'mcu': 'mcu/toshiba/tmpm366fdfg',
        'debugger': {
            'name': 'cmsis-dap',
            'interface': 'swd',
        }
    },
    'mbed-gd32f303ce': {
        'mcu':'mcu/gigadevice/gd32f303xe',
        'debugger': {
            'name': 'j-link',
            'interface': 'swd',
        }
    }
}
