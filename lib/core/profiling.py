#!/usr/bin/env python

"""
Copyright (c) 2006-2023 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import cProfile
import os

from lib.core.data import logger
from lib.core.data import paths

def profile(profileOutputFile=None):
    """
    This will run the program and present profiling data in a nice looking graph
    """

    if profileOutputFile is None:
        profileOutputFile = os.path.join(paths.SQLMAP_OUTPUT_PATH, "sqlmap_profile.raw")

    if os.path.exists(profileOutputFile):
        os.remove(profileOutputFile)

    # Start sqlmap main function and generate a raw profile file
    cProfile.run("start()", profileOutputFile)

    infoMsg = f"execution profiled and stored into file '{profileOutputFile}' (e.g. 'gprof2dot -f pstats {profileOutputFile} | dot -Tpng -o /tmp/sqlmap_profile.png')"
    logger.info(infoMsg)
