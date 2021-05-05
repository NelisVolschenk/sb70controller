
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import glib
from datetime import datetime
from ext.velib_python.vedbus import VeDbusItemImport
from ext.velib_python.ve_utils import unwrap_dbus_value

def print_value(name, path, changes):
    value = changes['Value']
    print datetime.now(), " - Value changed to ", value

DBusGMainLoop(set_as_default=True)
SysBus = dbus.SystemBus()
proxy = VeDbusItemImport(
    bus=SysBus,
    serviceName="com.victronenergy.system",
    path="/Ac/Consumption/L1/Power",
    eventCallback=print_value,
    createsignal=True)

mainloop = glib.MainLoop()
mainloop.run()
print "mainloop doesn't block"