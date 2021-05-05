
import dbus
from ext.velib_python.vedbus import VeDbusItemImport

SysBus = dbus.SystemBus()
proxy = VeDbusItemImport(
    bus=SysBus,
    serviceName="com.victronenergy.system",
    path="/Ac/Consumption/L1/Power",
    eventCallback=None,
    createsignal=True).get_value()