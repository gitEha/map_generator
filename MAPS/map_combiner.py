from pathlib import Path
import os

PATH = 'C:/Users/Ranet/Documents/Machine Learning/games/osu map generator/MAPS/PROTOTYPE MAPS/TEST/'

maps_collabed = []
with open('C:/Users/Ranet/Documents/Machine Learning/games/osu map generator/MAPS/combined_maps.txt', 'w', encoding='utf8') as f:
    for file in os.listdir(PATH):
        filename = os.fsdecode(file)
        if filename.endswith(".osu"):
            with open(os.path.join(PATH, file), encoding='utf8') as mf:
                content = [x.strip() for x in mf.readlines()]

            hitobjects_index = [x for x in content].index('[HitObjects]')
            X_one_example = '\n'.join(content[hitobjects_index + 1:])
            maps_collabed.append(X_one_example)
            f.write(X_one_example)
        f.write('\nEOS\n')
