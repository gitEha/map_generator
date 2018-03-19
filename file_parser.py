from pathlib import Path
import re

with open('C:/Users/Ranet/Documents/Machine Learning/games/osu map generator/MAPS/maplist.txt') as f:
    maps = f.read().split('\n')


pathlist = Path('G:\Recovery\Games\osu!\Songs').glob('**/*.osu')
pattern = re.compile(r'\(\w+\)\ ')

for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    map_file = path_in_str.split('\\')[-1]
    match = re.findall(pattern, map_file)
    try:
        #print(match[-1])
        map_file = map_file.replace(match[-1], '')
        for m in maps:
            if m in map_file:
                print(map_file, 'YES', len(maps))
                maps.remove(m)
    except:
        pass


    #print(path_in_str)