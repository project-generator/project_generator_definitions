# Project generator definitions

This repository defines definitions for targets and mcus. They are used to set proper data in the tools.

## YAML records description

### Target

Target record defines the name and mcu it contains.

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

All this data must be manually written at the moment. We might add a parser for given project file, to generate valid record file for given tool.

