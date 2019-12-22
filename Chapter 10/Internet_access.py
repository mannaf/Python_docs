from urllib.request import urlopen

with urlopen('https://sunplex.net/tvshows') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
