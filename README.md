# the ULTRASprig

an updated version of the [Sprig](https://github.com/hackclub/sprig/), made to be ultra-modular and expansible!

# Why?
the current model of the sprig is a bit... outdated. It still runs on the RP2040, has only 4 (broken out) gpios and just 2Mb of flash. The ULTRASprig has 7 usable GPIOs, and a completely new expansion system that allows for up to 16MB of additional flash, + PSRAM. it also uses I2C "modules" to give even more  interfaces

# Setup
## RP2354B
- get the larger packages (the BQ, RP2354, and the TP) pre-assembled
- use a stencil to solder the smaller passives
- solder male headers into the broken out pins
## Mainboard
- Solder all components except the pinsockets
- while soldering the pinsockets, make sure to have 1mm of clearance between the tips and the SPI display
- for the battery headers, one battery header will be connected to the + and - of the battery, and the other should be connected to the battery pins of the coreboard

# Usage
- build the firmware and flash it on the sprig

# Sub(Links)
- Mainboard
    - [Mainboard BoM](BOM.csv)
    - [Gerbers - Mainboard](gerbers.zip)
    - [Mainboard Design -- root folder](.)
- Core Board
    - [Core BoM](core_board/RP2354B/BOM.csv)
    - [Coreboard Design Files](core_board/RP2354B/)
- Expansions
    - IO Expander   
        - [Design](Expansions/IOExpander/)
        - [Gerbers](Expansions/IOExpander/Gerbers.zip)
        - [BoM](Expansions/IOExpander/BOM.csv)
    - Flash Breakout   
        - [Design](Expansions/FlashBreakout/)
        - [Gerbers](Expansions/FlashBreakout/gerbers.zip)
        - [BoM](Expansions/FlashBreakout/BOM.csv)
    - IMU Breakout   
    - [Design](Expansions/IMUBreakout/)
    - [Gerbers](Expansions/IMUBreakout/Gerbers.zip)
    - [BoM](Expansions/IMUBreakout/BOM.csv)

- [Gerbers - coreboard](core_board/RP2354B/Gerbers.zip)
# Renders
![front view](images/image.png)
> front view

![back view w/ board and battery headers](images/buh.png)
> back view w/ board and battery headers

![main board with modules](images/modules.png)
> front view, main board with modules


# Routing

![routed mainboard](images/image-1.png)
> routed mainboard

![routed coreboard](images/image%20copy.png)
> routed coreboard

# Schematics
![mainboard schematic](images/mainboard_schem.png)
> mainboard schematic

![core schematic](images/core.png)
> coreboard schematic