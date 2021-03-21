#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import pathlib


"""
Access:
  PROTOCOL        URL             USER            EFFECT
  http            http://.../                     klaus-ui,read-only
  http            http://.../     ro              klaus-ui,read-only
  http            http://.../     rw              klaus-ui,read-only(FIXME)
  git-over-http   http://.../                     read-only
  git-over-http   http://.../     ro              read-only
  git-over-http   http://.../     rw              read-write

Notes:
  1. We don't support git-protocol since it does not support one-server-multiple-domain.
"""


def start(params):
    selfDir = os.path.dirname(os.path.realpath(__file__))
    serverId = params["server-id"]
    domainName = params["domain-name"]
    dataDir = params["data-directory"]
    tmpDir = params["temp-directory"]
    webRootDir = params["webroot-directory"]

    # wsgi script
    wsgiFn = os.path.join(tmpDir, "wsgi-%s.py" % (serverId))
    with open(wsgiFn, "w") as f:
        buf = pathlib.Path(os.path.join(selfDir, "entry.py.in")).read_text()
        buf = buf.replace("%%DATA_DIR%%", dataDir)
        buf = buf.replace("%%SERVER_ID%%", serverId)
        f.write(buf)

    # generate apache config segment
    buf = ''
    buf += 'ServerName %s\n' % (domainName)
    buf += 'DocumentRoot "%s"\n' % (webRootDir)
    buf += 'WSGIScriptAlias / %s\n' % (wsgiFn)
    buf += 'WSGIChunkedRequest On\n'
    buf += 'WSGIPassAuthorization On\n'
    buf += '\n'

    cfg = {
        "module-dependencies": [
            "mod_wsgi.so",
        ],
        "config-segment": buf,
    }
    privateData = None
    return (cfg, privateData)


def stop(private_data):
    pass
