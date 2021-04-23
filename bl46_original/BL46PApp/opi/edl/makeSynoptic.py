#!/bin/env dls-python3

"""
generates a startup script for the GUI for each HTSS rig's set of IOCS

this should be run from the root of BL46P-BUILDER after all of the IOCs
have been compiled.

It creates a launch script for each HTSS in the BL46P-BUILDER/BL4xP-gui
"""

import os
import stat
from pathlib import Path

stGuiTemplate = """
#!/bin/sh
TOP="$(cd $(dirname "$0")/..; pwd)"

echo launcing BL46P-synoptic.edl from ${TOP}

# first load the paths. These have been generated from the configure/RELEASE
# tree. If we have a -d arg then load the opi/edl paths first
shopt -s nullglob
unset EDMDATAFILES

OPTS="-x -eolc -noedit"

EDMDATAFILES="${EDMDATAFILES}${TOP}/data"
EDMDATAFILES="${EDMDATAFILES}:/dls_sw/prod/R3.14.12.7/support/procServControl/1-19/data/"

%s

export EDMDATAFILES

# Set the path to include any scripts in data dirs
export PATH=${EDMDATAFILES}:${PATH}
edm ${OPTS}  -m "dom=BL%dP" BL46P-synoptic.edl
"""


for BL in range(46, 50):
    data_path = Path("data")
    if not data_path.exists():
        data_path.mkdir()

    edmPath = []
    gui_path = Path("data") / f"stBL{BL}P-gui"
    if gui_path.exists():
        os.chmod(gui_path, stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)

    for IOC in ["EA-IOC-01", "EA-IOC-02", "MO-IOC-01"]:
        ioc_path = Path("iocs") / f"BL{BL:d}P-{IOC:s}"
        orig_gui_path = ioc_path / "bin" / "linux-x86_64" / f"stBL{BL:d}P-{IOC:s}-gui"

        with orig_gui_path.open("r") as guiFile:
            lines = guiFile.readlines()

        for line in lines:
            if line.startswith('EDMDATAFILES="${EDMDATAFILES}:'):
                if line not in edmPath:
                    edmPath.append(line)

        # add the iocs's own data folder into the paths
        entry = 'EDMDATAFILES="${EDMDATAFILES}:${TOP}/'
        entry += f'{ioc_path / "data"}"\n'
        edmPath.append(entry)

    blSynoptic = stGuiTemplate % ("".join(edmPath), BL)

    with gui_path.open("w") as stream:
        stream.write(blSynoptic)

    os.chmod(gui_path, stat.S_IEXEC | stat.S_IREAD | stat.S_IXGRP | stat.S_IRGRP | stat.S_IXOTH | stat.S_IROTH)


