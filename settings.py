import datetime

settingsdict = {
    'MaxSleepTime': 5,
    'LoopCheckTime': 1,
    'BatteryCapacity': 40000,
    'LowBatteryRechargeTime': 7,
    '20%PowerSoc': 85,
    'WeekStableBatterySoc': 79,
    'WeekendStableBatterySoc': 79,
    'WeekendStartDay': 4,
    'WeekendStartTime': datetime.time(hour=15, minute=0),
    'WeekendEndDay': 6,
    'WeekendEndTime': datetime.time(hour=22, minute=0),
    'MinInPower': 250,
    'ThrottleBuffer': 150,
    'OverThrottle': 100,
    'ThrottleValue': 0,
    'Safety': {
        'Active': False,
        'Duration': datetime.timedelta(minutes=5),
        'EndTime': datetime.datetime.now(),
        'MaxInverterPower': 3000,
        'CriticalThreshold': 7000,
        'BuildupThreshold': 4000,
        'BuildupIterations': 30,
        'BuildupPercentage': 50,
    },
    'DoCharge': True,
    'ChargeDay': 6,
    'ChargeStartTime': datetime.time(hour=17, minute=0),
    'ChargeDuration': datetime.timedelta(hours=8),
    'ChargeDate': datetime.date.today(),
    'ChargeEndTime': datetime.datetime.now(),
    'ChargeInterval': datetime.timedelta(weeks=1),
    'ChargeActive': False,
    'ChargePower': 30000,
    'PvInverterDbusNames': ['pv_77_1064614']
}

servicesdict = {
            'AcSetpoint': {'Service': "com.victronenergy.settings",
                           'Path': "/Settings/CGwacs/AcPowerSetPoint",
                           'Proxy': object,
                           'Value': 0},
            'CCGXRelay': {'Service': "com.victronenergy.system",
                          'Path': "/Relay/0/State",
                          'Proxy': object,
                          'Value': 0},
            'L1InPower': {'Service': "com.victronenergy.vebus.ttyO1",
                           'Path': "/Ac/ActiveIn/L1/P",
                           'Proxy': object,
                           'Value': 0},
            'L1OutPower': {'Service': "com.victronenergy.vebus.ttyO1",
                           'Path': "/Ac/Out/L1/P",
                           'Proxy': object,
                           'Value': 0},
            'L1SolarMaxPower': {'Service': "com.victronenergy.pvinverter",
                                  'Path': "/Ac/MaxPower",
                                  'Proxy': object,
                                  'Value': 0},
            'L1SolarPower': {'Service': "com.victronenergy.pvinverter",
                             'Path': "/Ac/Power",
                             'Proxy': object,
                             'Value': 0},
            'L1SolarPowerLimit':{'Service': "com.victronenergy.pvinverter",
                             'Path': "/Ac/PowerLimit",
                             'Proxy': object,
                             'Value': 0},
            'Soc': {'Service': "com.victronenergy.system",
                    'Path': "/Dc/Battery/Soc",
                    'Proxy': object,
                    'Value': 0}
        }

donotcalclist = ["/Settings/CGwacs/AcPowerSetPoint"]

for invname in settingsdict['PvInverterDbusNames']:
    for name in servicesdict:
        if name.startswith('L1Solar'):
            servicesdict[name]['Service'] += '.' + invname