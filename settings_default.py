import datetime
import copy

settingsdict = {
    'MaxSleepTime': 5,
    'LoopCheckTime': 1,
    'BatteryCapacity': 40000,
    'LowBatteryRechargeTime': 6,
    '20%PowerSoc': 85,
    'WeekStableBatterySoc': 80,
    'WeekendStableBatterySoc': 80,
    'WeekendStartDay': 4,
    'WeekendStartTime': datetime.time(hour=15, minute=0),
    'WeekendEndDay': 6,
    'WeekendEndTime': datetime.time(hour=22, minute=0),
    'MinInPower': 250,
    'ThrottleBuffer': 150, # The hysteresis value below MinInPower for throttling to start
    'OverThrottle': 200,  # This needs to be larger than ThrottleBuffer
    'StrongThrottleMinSoc': 97,  # This needs to be more than 20%PowerSOC
    'StrongThrottleMaxSoc': 99,  # This needs to be more than StrongThrottleMinSoc
    'StrongThrottleBuffer': 800,  # This needs to be more than ThrottleBuffer
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
    'ChargePower': 15000,
    'RescanServiceInterval': datetime.timedelta(minutes=10),
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
    'Soc': {'Service': "com.victronenergy.system",
            'Path': "/Dc/Battery/Soc",
            'Proxy': object,
            'Value': 80},
    'L1InPower': {'Service': "com.victronenergy.vebus.ttyO1",
                  'Path': "/Ac/ActiveIn/L1/P",
                  'Proxy': object,
                  'Value': 0},
    'L1OutPower': {'Service': "com.victronenergy.vebus.ttyO1",
                   'Path': "/Ac/Out/L1/P",
                   'Proxy': object,
                   'Value': 0},
        }

pvdict = {
    'L1': {
        'InverterList': [], # This should look something like this: pv_77_1028252, pv_77_1028251
        'Inverters': {},
    },
}

pv_services_structure = {
    'MaxPower': {'Service': "com.victronenergy.pvinverter",
                 'Path': "/Ac/MaxPower",
                 'Proxy': object,
                 'Value': 0},
    'Power': {'Service': "com.victronenergy.pvinverter",
              'Path': "/Ac/Power",
              'Proxy': object,
              'Value': 0},
    'PowerLimit': {'Service': "com.victronenergy.pvinverter",
                   'Path': "/Ac/PowerLimit",
                   'Proxy': object,
                   'Value': 0}
}
# Generate the pvdict
for line in pvdict:
    for inverter in pvdict[line]['InverterList']:
        pvdict[line]['Inverters'][inverter] = copy.deepcopy(pv_services_structure)
        for setting in pvdict[line]['Inverters'][inverter]:
            pvdict[line]['Inverters'][inverter][setting]['Service'] += '.' + inverter


# TODO change this to a dictionary so that the name can be included
donotcalclist = [
    "/Settings/CGwacs/AcPowerSetPoint",
    "/Ac/PowerLimit"
]

servicelist = []