# Project generator definitions

This repository defines definitions for targets and mcus. They are used to set proper data in the tools.

## Create a new mcu yaml definition

This module provides a script to extract the information needed to create a new yaml mcu definiton file.

An example for creating mcu.yaml for lpc1768, from a project file lpc1768_blinky.ewp (IAR)

```
progendef create -m lpc1768 -t iar -f lpc1768_blinky.ewp
```

This creates lpc1768.yaml file in the current directory.

## YAML records

### Targets

To generalize MCU's, there're targets definition available. The target name does not change based on the tool used. We provide a dictionary where we can define a target with mcu, for instance:

```
PROGENDEF_TARGETS = {
    'arch-ble': 'mcu/nordic/nrf51',
}
```

If a project can either use arch-ble as a target or nrf51 (mcu). 

### MCU

MCU record defines the basic information about the mcu and specific settings for each tool. As an example is shown the uvision settings for the lpc1768 mcu. These specific data can be manually extracted from a project file or use progendef commad to create the yaml file for you.

If you are adding a new mcu, please follow the uvision naming for MCUs, for consistency.

```
mcu:
    vendor:
        - nxp
    name:
        - lpc1768
    core:
        - cortex-m3
tool_specific:
    uvision:
        TargetOption:
            Device:
                - LPC1768
            Vendor:
                - NXP
            Cpu:
                - IRAM(0x10000000-0x10007FFF) IRAM2(0x2007C000-0x20083FFF) IROM(0-0x7FFFF) CLOCK(12000000) CPUTYPE("Cortex-M3")
            FlashDriverDll:
                - UL2CM3(-O463 -S0 -C0 -FO7 -FD10000000 -FC800 -FN1 -FF0LPC_IAP_512 -FS00 -FL080000)
            DeviceId:
                - 4868
            SFDFile:
                - SFD\NXP\LPC176x5x\LPC176x5x.SFR
```

The data give in the mcu and target use lower cases, also files within this directory to keep consistency. The tool specific data follow the tools definitions.

## Tools specific definitions

### uVision

There are two supported uvision. uvision (defaults to uvision4 at the moment) and uvision5. uVision 5 uses software packs, and it is compatible with the older version via legacy devices. Define legacy device as uvision/uvision4.

```
tool_specific:
    uvision:
        TargetOption:
            Device:
                - LPC1768
            Vendor:
                - NXP
            Cpu:
                - IRAM(0x10000000-0x10007FFF) IRAM2(0x2007C000-0x20083FFF) IROM(0-0x7FFFF) CLOCK(12000000) CPUTYPE("Cortex-M3")
            FlashDriverDll:
                - UL2CM3(-O463 -S0 -C0 -FO7 -FD10000000 -FC800 -FN1 -FF0LPC_IAP_512 -FS00 -FL080000)
            DeviceId:
                - 4868
            SFDFile:
                - SFD\NXP\LPC176x5x\LPC176x5x.SFR
```

All information in the code above are from uVision project. All attributes needs to be filled in , in order to get proper working target in the project file and the correct flash algorithms for the target.

How to get all this information for a new mcu? Create a new project in uVision, select your target, save the project. Then open the project in any text editor, and look for attributes inside TargetOption, as 'Device', 'Vendor', etc.

Once you specified all needed information, test to build your project and check if the correct target is set in the uVision project.

### IAR

```
    iar:
        OGChipSelectEditMenu:
            state:
                - LPC1768 NXP LPC1768
        OGCoreOrChip:
            state:
                - 1
```

In the code above, LPC1768 is defined. To add a new target, create a new project in IAR, select your desired target, save the project. Use progendef to extract information or manually - open the project in any text editor, and find the attribute OGChipSelectEditMenu. OGCoreOrChip should be set to 1, as Chip will be used. Be carefull with OGChipSelectEditMenu, it should be exact as in origin project.

Once you specified all needed information, test to build your project and check if the correct target is set in the IAR project.

### CoIDE

```
    coide:
    coide:
        Device:
            manufacturerId:
                - 7
            manufacturerName:
                - NXP
            chipId:
                - 165
            chipName:
                - LPC1768
        DebugOption:
            defaultAlgorithm:
                - lpc17xx_512.elf
        MemoryAreas:
            IROM1:
                name:
                    - IROM1
                size:
                    - 0x00080000
                startValue:
                    - 0x00000000
                type:
                    - ReadOnly
            IRAM1:
                name:
                    - IRAM1
                size:
                    - 0x00008000
                startValue:
                    - 0x10000000
                type:
                    - ReadWrite
            IROM2:
                name:
                    - IROM2
                size:
                    - 0x0
                startValue:
                    - 0x0
                type:
                    - ReadOnly
            IRAM2:
                name:
                    - IROM2
                size:
                    - 0x00008000
                startValue:
                    - 0x2007C000
                type:
                    - ReadWrite
```

LPC1768 MCU is defined above for CoIDE. To add a new target, create a new project in CoIDE, select your target, save the project. Use progendef to extract information or manually - open the project file (.coproj) in the text editor, and search for all the information which is above. It's required to set the target properly. There is an information about ROM/RAM sizes, Flash algo used and Id numbers for the target.
