#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import platform
import re
import sys
import util

# the private key is stored in ~/.local/share/gajim/_SERVERNAME_.key3
# the fingerprints are stored in ~/.local/share/gajim/_SERVERNAME_.fpr
# the accounts are stored in ~/.config/gajim/config

class GajimProperties():

    if platform.system() == 'Windows':
        path = os.path.expanduser('~/Application Data/Gajim')
    else:
        path = os.path.expanduser('~/.local/share/gajim')

    @staticmethod
    def parse(settingsdir=None):
        if settingsdir == None:
            settingsdir = GajimProperties.path
        keydict = dict()
        for f in glob.glob(settingsdir + '*.key3'):
            pass

    @staticmethod
    def write(keys, savedir):
        if not os.path.exists(savedir):
            raise Exception('"' + savedir + '" does not exist!')



#------------------------------------------------------------------------------#
# for testing from the command line:
def main(argv):
    import pprint

    print 'Gajim stores its files in ' + GajimProperties.path

    if len(sys.argv) == 2:
        settingsdir = sys.argv[1]
    else:
        settingsdir = '../tests/gajim'

    keydict = GajimProperties.parse(settingsdir)
    print '----------------------------------------'
    pprint.pprint(keydict)
    print '----------------------------------------'
    GajimProperties.write(keydict, '/tmp')

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
