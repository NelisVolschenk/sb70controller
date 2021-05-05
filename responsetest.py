
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import glib
from ext.velib_python.vedbus import VeDbusItemImport

def print_value(name, path, changes):
    print "Value changed"

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