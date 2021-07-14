import paramiko
from enum import Enum
import logging

logger = logging.getLogger(__name__)


def parse_ssh(login: str):
    message = "syntax: ssh://login,password@host:port/path/to/file"

    if not login.startswith("ssh://"):
        raise ValueError(message)
    else:
        _, login = login.split("ssh://")            # '', login,password@host:port/path/to/file

    if "," not in login:
        raise ValueError(message)
    else:
        username, login = login.split(",")          # login, password@host:port/path/to/file

    if "@" not in login:
        raise ValueError(message)
    else:
        password, login = login.split("@")          # password, host:port/path/to/file

    if ":" not in login:
        port = 22
        if "/" not in login:
            raise ValueError(message)
        host, path = login.split("/", maxsplit=1)   # host, path/to/file

    else:
        host, login = login.split(":")              # host, port/path/to/file

        if "/" not in login:
            raise ValueError(message)
        port, path = login.split("/", maxsplit=1)   # port, path/to/file

    path = "/" + path

    return dict(
        username=username,
        password=password,
        host=host,
        port=port,
        path=path
    )


Action = Enum('Action', "EXIT RAISE IGNORE")


def ssh_file(host, port, username, password, path, mode='r', onexception=Action.EXIT):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        logger.info("opening connection")
        ssh.connect(hostname=host, port=port, username=username, password=password)

        logger.info("creating sftp")
        sftp = ssh.open_sftp()
        logger.info(f"opening file {path}")
        file = sftp.open(path, mode=mode)
        logger.info("ok")
        return file
    except Exception as e:
        print(repr(e))
        if onexception == Action.EXIT:
            logger.fatal("exiting")
            exit()
        elif onexception == Action.RAISE:
            logger.error("raising exception")
            raise e
        elif onexception == Action.IGNORE:
            logger.info("ignoring")
            pass
        else:
            raise SystemExit(f"FATAL: unknow action on exception: {onexception}")


if __name__ == '__main__':

    kwargs = parse_ssh("ssh://login,password@host:port/path/to/file")
    print(kwargs)

    kwargs = parse_ssh("ssh://root, ***REMOVED***@192.168.1.10:2200/path/to/file")
    print(kwargs)

    kwargs = parse_ssh("ssh://root,1234@192.168.1.10/path/to/file")
    print(kwargs)

    kwargs = parse_ssh("ssh://***REMOVED***,***REMOVED***@192.168.1.20/home/***REMOVED***/code/python/hacking/passwordcracker/brutefile.txt")
    print(kwargs)

    # exit()

    # file = ssh_file(
    #     host='192.168.1.20',
    #     username='***REMOVED***',
    #     password='***REMOVED***',
    #     path='/home/***REMOVED***/code/python/hacking/passwordcracker/brutefile.txt'
    # )

    file = ssh_file(**kwargs)
    try:
        for line in file:
            print(line.strip())
    finally:
        file.close()
