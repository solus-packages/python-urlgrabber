
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, pythonmodules, pisitools


def install():
    pythonmodules.install ()
    pisitools.domove ("/usr/share/doc/urlgrabber-3.10.1", "/usr/share/doc/python-urlgrabber")
