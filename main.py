#!/usr/bin/env python

# Imports
import dbus
import time
import os
import sys
import datetime
import logging
from logging.handlers import RotatingFileHandler
from settings import settingsdict
from ext.velib_python.vedbus import VeDbusItemImport

# Create a rotating logger
def create_rotating_log(path):

    # Create the logger
    logger = logging.getLogger("Main Log")
    logger.setLevel(logging.INFO)
    # Create a rotating handler
    handler = RotatingFileHandler(path, maxBytes=1048576, backupCount=5)
    # Create a formatter and add to handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger


class SystemController(object):

    def __init__(self):

        self.bus = dbus.SystemBus()
        self.settings = settingsdict
        self.DbusServices = {
            'AcSetpoint': {'Service': "com.victronenergy.settings",
                           'Path': "/Settings/CGwacs/AcPowerSetPoint",
                           'Value': 0},
            'CCGXRelay': {'Service': "com.victronenergy.system",
                           'Path': "/Relay/0/State",
                           'Value': 0},
            'L1Power': {'Service': "com.victronenergy.system",
                        'Path': "/Ac/Consumption/L1/Power",
                        'Value': 0},
            'L2Power': {'Service': "com.victronenergy.system",
                        'Path': "/Ac/Consumption/L2/Power",
                        'Value': 0},
            'L3Power': {'Service': "com.victronenergy.system",
                        'Path': "/Ac/Consumption/L3/Power",
                        'Value': 0},
            'Soc': {'Service': "com.victronenergy.system",
                    'Path': "/Dc/Battery/Soc",
                    'Value': 0}
        }


    def getvalues(self):

        # Get new values for the services
        for service in self.DbusServices:
            try:
                self.DbusServices[service]['Value'] = VeDbusItemImport(
                        bus=self.bus,
                        serviceName=self.DbusServices[service]['Service'],
                        path=self.DbusServices[service]['Path'],
                        eventCallback=None,
                        createsignal=False).get_value()
            except dbus.DBusException:
                mainlogger.warning('Exception in getting dbus service %s' % service)

            try:
                self.DbusServices[service]['Value'] *= 1
                self.DbusServices[service]['Value'] = max(self.DbusServices[service]['Value'], 0)
            except:
                if service == 'L1Power' or service == 'L2Power' or service == 'L3Power':
                    self.DbusServices[service]['Value'] = 1000
                elif service == 'Soc':
                    self.DbusServices[service]['Value'] = self.settings['StableBatterySoc']
                mainlogger.warning('No value on %s' % service)

    def setvalue(self, service, value):

        try:
            VeDbusItemImport(
                bus=self.bus,
                serviceName=self.DbusServices[service]['Service'],
                path=self.DbusServices[service]['Path'],
                eventCallback=None,
                createsignal=False).set_value(value)
        except dbus.DBusException:
            mainlogger.warning('Exception in setting dbus service %s' % service)

    def run(self):
        stablebatterysoc = self.settings['StableBatterySoc']
        weekend = False

        while True:

            # Set the stable battery SOC depending on the weekday
            # The weekend ends in the same week as it starts (eg. sunday)
            if self.settings['WeekendEndDay'] >= self.settings['WeekendStartDay']:
                # Weekend has started
                if datetime.datetime.now().weekday() >= self.settings['WeekendStartDay'] and \
                        datetime.datetime.now().time() >= self.settings['WeekendStartTime']:
                    weekend = True
                # Weekend has ended
                if datetime.datetime.now().weekday() >= self.settings['WeekendEndDay'] and \
                            datetime.datetime.now().time() >= self.settings['WeekendEndTime']:
                    weekend = False
            # The weekend ends during the week after the weekend started
            else:
                # Week has started
                if datetime.datetime.now().weekday() >= self.settings['WeekendEndDay'] and \
                            datetime.datetime.now().time() >= self.settings['WeekendEndTime']:
                    weekend = False
                # Week has ended
                if datetime.datetime.now().weekday() >= self.settings['WeekendStartDay'] and \
                        datetime.datetime.now().time() >= self.settings['WeekendStartTime']:
                    weekend = True
            if weekend:
                stablebatterysoc = self.settings['WeekendStableBatterySoc']
            else:
                stablebatterysoc = self.settings['WeekStableBatterySoc']






if __name__ == "__main__":
    # setup the logger
    log_file = "log.txt"
    mainlogger = create_rotating_log(log_file)
    # start the controller
    controller = SystemController()
    controller.run()