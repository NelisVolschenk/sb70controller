
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import glib
from datetime import datetime
from ext.velib_python.vedbus import VeDbusItemImport
from ext.velib_python.ve_utils import unwrap_dbus_value

oldtime = datetime.now()

def print_value(name, path, changes):
    value = changes['Value']
    newtime = datetime.now()
    global oldtime
    delta = newtime - oldtime
    oldtime = newtime
    print delta, " - Value changed to ", changes

def print_proxy():
    print proxy.get_value()

def buschecker(name, path, changes):
    print datetime.now(), "bus"

def syschecker(name, path, changes):
    print datetime.now(), "sys"


DBusGMainLoop(set_as_default=True)
SysBus = dbus.SystemBus()

proxy1 = VeDbusItemImport(
    bus=SysBus,
    serviceName="com.victronenergy.vebus.ttyO1",
    path="/Ac/Out/L1/P",
    eventCallback=buschecker,
    createsignal=True)

proxy2 = VeDbusItemImport(
    bus=SysBus,
    serviceName="com.victronenergy.system",
    path="/Ac/Consumption/L1/Power",
    eventCallback=syschecker,
    createsignal=True)

#glib.timeout_add_seconds(2, print_proxy)
mainloop = glib.MainLoop()
mainloop.run()