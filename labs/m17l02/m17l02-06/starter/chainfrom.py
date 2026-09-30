settings = {'host': 'localhost'}

def port():
    try:
        return settings['port']
    except KeyError as err:
        raise RuntimeError('the settings file is incomplete') from err

print(port())
