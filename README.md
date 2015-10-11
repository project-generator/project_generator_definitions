# Project generator definitions alpha version

This repository defines definitions for targets and mcus. They are used to set proper data in the tools.

Currently alpha version, please check dev_v1 on this github repository. Master is still currently used by pgen v0.x.0.

### Target

To generalize MCU's, there's a target definition available. The target name does not change based on the tool used. There's file board_definitions, where are all boards supported defined. There's a dictionary which translates the target name to the tool's specific MCU name.

If a project defines frdm-k20d50m as target, the proper mcu settings will be set for a tool.

Each mcu has own tool_specific definitions.

```
target:
    name:
        - frdm-k64f
    mcu:
        - mcu/freescale/mk64fn1m0xxx12
```

### MCU

MCU record defines the basic information about the mcu and specific settings for each tool. As an example is shown the uvision settings for the lpc1768 mcu. The data can be obtain from the project files. Look for keys TargetOption in uvision project file.

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
            DeviceId:
                - 4868
```

The data give in the mcu and target use lower cases, also files within this directory to keep consistency. The tool specific data follow the tools definitions.

All this data must be manually written at the moment. We might add a parser for given project file, to generate valid record file for given tool.

## Tools specific definitions

### uVision

```
    uvision:
        TargetOption:
            Device:
                - LPC1768
            DeviceId:
                - 4868
```

All information in the code above are from uVision project. All attributes needs to be filled in , in order to get proper working target in the project file and the correct flash algorithms for the target.

How to get all this information for a new mcu? Create a new project in uVision, select your target, save the project. Then open the project in any text editor, and look for attributes inside TargetOption, as 'Device', 'Vendor', etc.

Once you specified all needed information, test to build your project and check if the correct target is set in the uVision project.

Note:
You might spot there's RegisterFile for example for nrf51 mcu, which means use new device packs for the mcu.

```
    uvision:
        TargetOption:
            RegisterFile:
                - $$Device:nRF51822_xxAA$Device\Include\nrf.h
```

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

In the code above, LPC1768 is defined. To add a new target, create a new project in IAR, select your desired target, save the project. Then open the project in any text editor, and find the attribute OGChipSelectEditMenu. OGCoreOrChip should be set to 1, as Chip will be used. Be carefull with OGChipSelectEditMenu, it should be exact as in origin project.

Once you specified all needed information, test to build your project and check if the correct target is set in the IAR project.

### CoIDE

```
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
                size:
                    - 0x00080000
                startValue:
                    - 0x00000000
            IRAM1:
                size:
                    - 0x00008000
                startValue:
                    - 0x10000000
            IROM2:
                size:
                    - 0x0
                startValue:
                    - 0x0
            IRAM2:
                size:
                    - 0x00008000
                startValue:
                    - 0x2007C000
```

LPC1768 MCU is defined above for CoIDE. To add a new target, create a new project in CoIDE, selec your target, save the project. Open the project file (.coproj) in the text editor, and search for all the information which is above. It's required to set the target properly. There is an information about ROM/RAM sizes, Flash algo used and Id numbers for the target.
