class TooColdError(Exception):
    pass

def swim(water_temp):
    if water_temp < 5:
        raise TooColdError(str(water_temp) + ' degrees is too cold')
    return 'swimming in ' + str(water_temp) + ' degrees'

print(swim(18))
try:
    print(swim(-2))
except TooColdError as err:
    print('caught a TooColdError:', err)
