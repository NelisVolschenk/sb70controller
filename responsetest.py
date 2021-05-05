
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

DBusGMainLoop(set_as_default=True)
SysBus = dbus.SystemBus()
proxy = VeDbusItemImport(
    bus=SysBus,
    serviceName="com.victronenergy.system",
    path="/Ac/Consumption/L1/Power",
    eventCallback=print_value,
    createsignal=True)

proxy2 = VeDbusItemImport(
    bus=SysBus,
    serviceName="com.victronenergy.system",
    path="/Dc/Battery/Soc",
    eventCallback=print_value,
    createsignal=True)

mainloop = glib.MainLoop()
mainloop.run()
print "mainloop doesn't block"