from os.path import exists

import yaml

with open("assos_links.yaml", "r", encoding="utf8") as links_file:
    data = yaml.load(links_file, Loader=yaml.CLoader)

for banner in data:
    for link in banner["links"]:
        if not exists("src/assets/icons/" + link["icon"]):
            raise ValueError(
                f"File {link['icon']} is missing from the assets directory"
            )