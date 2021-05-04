import datetime




settingsdict = {
    'BatteryCapacity': 155000,
    'LowBatteryRechargeTime': 7,
    'WeekStableBatterySoc': 79,
    'WeekendStableBatterySoc': 79,
    'WeekendStartDay': 4,
    'WeekendStartTime': datetime.time(hour=15, minute=0),
    'WeekendEndDay': 6,
    'WeekendEndTime': datetime.time(hour=22, minute=0),
    '20%PowerSoc': 85,
    'MinInPower': 600,
    'MaxInPower': 50000,
    'SafetyDuration': datetime.timedelta(minutes=5),
    'SafetyEndTime': datetime.datetime.now()
}
