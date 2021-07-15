import os
import sys
import urllib.request
import logging

from constants import *
from sshfile import parse_ssh, ssh_file, Action

logger = logging.getLogger(__name__)


def get_filehandle(path):
    # print(DARK_GREEN)
    try:
        # ssh://***REMOVED***,***REMOVED***@192.168.1.20/home/***REMOVED***/code/python/hacking/passwordcracker/brutefile.txt
        logger.info(f"SSH| try to parse {path}")
        kwargs = parse_ssh(path)
        logger.info(f"SSH| try to open {path}")
        file = ssh_file(**kwargs, onexception=Action.RAISE)
        logger.info(f"SSH| success, open: {path}")
    except:
        logger.error(f"SSH| could not open {path}")
        try:
            #  https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt
            logger.info(f"URLLIB| try to open {path}")
            file = urllib.request.urlopen(path)
            logger.info(f"URLLIB| success, open {path}")
        except:
            # c:\path\to\file
            # /path/to/file
            logger.error(f"URLLIB| could not open {path}")
            try:
                logger.info(f"FILE| try to open {path}")
                file = open(path, 'r', encoding='utf8')
                logger.info(f"FILE| success, open {path}")
            except:
                # print(RED)
                logger.fatal(f"FATAL| cannot open {path}")
                exit()
    return file


if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)
    if not len(sys.argv[1:]):
        raise SystemExit(f"syntax {os.path.basename(sys.argv[0])} filepath")
    file = get_filehandle(sys.argv[1])
    file.close()