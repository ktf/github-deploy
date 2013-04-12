#!/usr/bin/env python
import cgi
import os
from os.path import join
import cjson
from sys import exit 


if __name__ == "__main__":
  cfg = cjson.decode(open("config.json").read())
  gitPrefix = cfg.get("git_prefix", None)
  if gitPrefix:
    os.environ["PATH"] = (os.environ["PATH"] and os.environ["PATH"] + ":" or "") + join(gitPrefix, "bin")
  data = cgi.FieldStorage()
  if not "payload" in data:
    print "Status: 404 Not Found"
    print ""
    print "Error"
    exit(0)
  payload = cjson.decode(data.getfirst("payload", None))
  if not payload:
    print "Status: 404 Not Found"
    print ""
    print "Error"
    exit(0)
  file("foo", "w").write(str(payload))
  print "Status: 200 OK"
  print
  exit(0)
