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
# should be target name: path to mcu yaml file
PROGENDEF_TARGETS = {
    'arch-ble': 'mcu/nordic/nrf51822',
    'arch-pro': 'mcu/nordic/nrf51822',
    'dfcm-nnn40': 'mcu/nordic/nrf51822',
    'mbed-lpc1768': 'mcu/nxp/lpc1768',
    'disco-f334c8':'mcu/st/stm32f334x8',
    'disco-f407vg':'mcu/st/stm32f401xe',
    'disco-f746ng':'mcu/st/stm32f746ng',
    'disco-l053c8':'mcu/st/stm32l053x8',
    'disco-l476vg':'mcu/st/stm32l476vg',
    'efm32gg-stk':'mcu/siliconlabs/efm32gg990f1024',
    'efm32hg-stk':'mcu/siliconlabs/efm32hg322f64',
    'efm32wg-stk':'mcu/siliconlabs/efm32wg990f256',
    'efm32zg-stk':'mcu/siliconlabs/efm32zg222f32',
    'efm32lg-stk':'mcu/siliconlabs/efm32lg990f256',
    'frdm-k20d50m':'mcu/freescale/mk20dx128xxx5',
    'frdm-k22f':'mcu/freescale/mk22dn512xxx5',
    'frdm-k64f': 'mcu/freescale/mk64fn1m0xxx12',
    'k64f': 'mcu/freescale/mk64fn1m0xxx12',
    'frdm-kl05z':'mcu/freescale/mkl05z32xxx4',
    'frdm-kl25z':'mcu/freescale/mkl25z128xxx4',
    'frdm-kl43z':'mcu/freescale/mkl43z256xxx4',
    'frdm-kl46z':'mcu/freescale/mkl46z256xxx4',
    'hrm1017':'mcu/nordic/nrf51822',
    'max32600':'mcu/maxim/max32600x85',
    'max32600':'mcu/maxim/max32600x85',
    'mbed-lpc11u24':'mcu/nxp/lpc11u24_201',
    'mbed-lpc1768':'mcu/nxp/lpc1768',
    'mkit':'mcu/nordic/nrf51822',
    'nrf51-dk':'mcu/nordic/nrf51822',
    'nrf51-dongle':'mcu/nordic/nrf51822',
    'nu-nuc472-nutiny':'mcu/nuvoton/nuc472hi8ae',
    'nucleo-f030r8':'mcu/st/stm32f030x8',
    'nucleo-f070rb':'mcu/st/stm32f070rb',
    'nucleo-f072rb':'mcu/st/stm32f072rb',
    'nucleo-f103rb':'mcu/st/stm32f103xb',
    'nucleo-f091rc':'mcu/st/stm32f091rc',
    'nucleo-f302r8':'mcu/st/stm32f302x8',
    'nucleo-f303re':'mcu/st/stm32f303xe',
    'nucleo-f334r8':'mcu/st/stm32f334x8',
    'nucleo-f401re':'mcu/st/stm32f401xe',
    'nucleo-f411re':'mcu/st/stm32f411re',
    'nucleo-f446re':'mcu/st/stm32f446re',
    'nucleo-l073rz':'mcu/st/stm32l073xz',
    'nucleo-l152re':'mcu/st/stm32l152xe',
    'ublox-c027':'mcu/nxp/lpc1768',
    'seed-tinyble':'mcu/nordic/nrf51822',
    'stk3700-gcc':'mcu/siliconlabs/efm32gg990f1024',
    'odin-w2':'mcu/st/stm32f439zitx',
}
