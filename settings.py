import datetime




settingsdict = {
    'MaxSleepTime': 5,
    'LoopCheckTime': 1,
    'BatteryCapacity': 155000,
    'LowBatteryRechargeTime': 7,
    'WeekStableBatterySoc': 79,
    'WeekendStableBatterySoc': 79,
    'WeekendStartDay': 4,
    'WeekendStartTime': datetime.time(hour=15, minute=0),
    'WeekendEndDay': 6,
    'WeekendEndTime': datetime.time(hour=22, minute=0),
    '20%PowerSoc': 85,
    'ConstInPower': 200,
    'MinInPower': 200,
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
    'ChargePower': 30000
}

servicesdict = {
            'AcSetpoint': {'Service': "com.victronenergy.settings",
                           'Path': "/Settings/CGwacs/AcPowerSetPoint",
                           'Value': 0},
            'CCGXRelay': {'Service': "com.victronenergy.system",
                           'Path': "/Relay/0/State",
                           'Value': 0},
            'L1OutPower': {'Service': "com.victronenergy.system",
                        'Path': "/Ac/Consumption/L1/Power",
                        'Value': 0},
            'L1SolarPower': {'Service': "com.victronenergy.system",
                         'Path': "/Ac/PvOnOutput/L1/Power",
                         'Value': 0},
            'Soc': {'Service': "com.victronenergy.system",
                    'Path': "/Dc/Battery/Soc",
                    'Value': 0}
        }
