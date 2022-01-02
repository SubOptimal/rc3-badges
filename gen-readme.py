#!/usr/bin/env python3

import json

out_lines = list()

out_lines.append('Badges earned during https://events.ccc.de/category/rc3-2021[rc3 2021]\n')
out_lines.append('\n')
out_lines.append('[cols="1a,1a,1a"]\n')
out_lines.append('|===\n')
out_lines.append('|assembly|title|badge\n')
out_lines.append('\n')

with open('badges.json') as json_file:
    badges = json.load(json_file)
    badges.sort(key=lambda x: x["assembly"].lower())

    for badge in badges:
        assembly = badge['assembly']
        title = badge['title'].replace('|', '\\|')
        image = badge['image']
        out_lines.append(f'|{assembly}|{title}|image:{image}[{image},128]\n')

out_lines.append('|===\n')

with open('README.adoc', 'w') as readme_file:
    readme_file.writelines(out_lines)
