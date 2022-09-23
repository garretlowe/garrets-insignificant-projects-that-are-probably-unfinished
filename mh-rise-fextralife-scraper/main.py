import requests
import lxml.html
import pathlib
import sys

# 0 - Silent, 1 - INFO, 2 - WARN, 3 - ERROR
DEBUG_LEVEL = int(sys.argv[1]) if len(sys.argv) == 2 else 1
INFO_LEVEL = 1
WARN_LEVEL = 2
ERROR_LEVEL = 3


def format_monster(mon_page):

    def format_list(row_names=[]):
        for row_name in row_names:
            try:
                row = mon_page.xpath(
                    f'//tr[td[contains(text(), "{row_name}")]]/td[last()]')[0]
            except IndexError:
                continue
            break
        else:
            if DEBUG_LEVEL >= WARN_LEVEL:
                print(f'WARN: Could not find row with "{row_names}".')
            return 'None'

        if row.getchildren():
            row = row.getchildren()
            if len(row) > 0:
                first = True
                out_list = ''
                for element in row:
                    if element.tag == 'a':
                        if first:
                            out_list += f'{element.text_content()}'
                            first = False
                        else:
                            out_list += f', {element.text_content()}'
                return out_list
            return 'None'
        else:
            return row.text_content()

    def format_combat_info(list_parent_name, list_child_contents, replace_text):
        try:
            parent_path = mon_page.xpath(
                f'//li[strong[contains(text(), "{list_parent_name}")]]')[0]
        except IndexError:
            if DEBUG_LEVEL >= WARN_LEVEL:
                print(
                    f'WARN: Could not find list item with parent "{list_parent_name}"')
            return None
        try:
            child_path = parent_path.xpath(
                f'//ul/li[strong[contains(text(), "{list_child_contents}")]]')[0]
        except IndexError:
            try:
                child_path = parent_path.xpath(
                    f'//ul/li[(strong|.)/span[contains(text(), "{list_child_contents}")]]')[0]
            except IndexError:
                if DEBUG_LEVEL >= ERROR_LEVEL:
                    print(
                        f'ERROR: Could not find list item with child "{list_child_contents}".')
                return None
        return child_path.text_content().replace(replace_text, '')

    def format_materials(xp):
        materials = []
        try:
            for mat_row in mon_page.xpath(xp)[0].getchildren():
                material = dict()
                material['name'] = mat_row.getchildren(
                )[0].text_content().replace('--', '-')
                material['target'] = mat_row.getchildren(
                )[1].text_content().replace('--', '-')
                material['capture'] = mat_row.getchildren(
                )[2].text_content().replace('--', '-')
                material['part_break'] = mat_row.getchildren(
                )[3].text_content().replace('--', '-')
                material['carve'] = mat_row.getchildren(
                )[4].text_content().replace('--', '-')
                material['dropped'] = mat_row.getchildren(
                )[5].text_content().replace('--', '-')
                materials.append(material)
        except IndexError:
            for mat_row in mon_page.xpath(xp)[0].getchildren():
                material = dict()
                material['name'] = mat_row.getchildren(
                )[0].text_content().replace('--', '-')
                material['target'] = mat_row.getchildren(
                )[1].text_content().replace('--', '-')
                material['capture'] = '-'
                material['part_break'] = mat_row.getchildren(
                )[2].text_content().replace('--', '-')
                material['carve'] = mat_row.getchildren(
                )[3].text_content().replace('--', '-')
                material['dropped'] = mat_row.getchildren(
                )[4].text_content().replace('--', '-')
                materials.append(material)

        return materials

    threat = format_list(['Threat Level'])
    if len(threat.strip()) > 3:
        threat = f'{len(threat)}⭐'
    mon_class = format_list(['Class', 'Species'])
    locations = format_list(['Location', 'Habitat'])
    element = format_list(['Element'])
    short_ailments = format_list(['Ailment'])
    weaknesses = format_list(['Weakness'])
    resistances = format_list(['Resistance'])

    eff_items = format_combat_info('Item', 'Effective:', 'Effective: ')
    ineff_items = format_combat_info('Item', 'Ineffective:', 'Ineffective: ')
    kinsect = {
        'red': format_combat_info('Kinsect', 'Red', 'Red: '),
        'orange': format_combat_info('Kinsect', 'Orange', 'Orange: '),
        'white': format_combat_info('Kinsect', 'White', 'White: ')
    }

    parts = []
    for index, wep_row in enumerate(mon_page.xpath('//table[@class="wiki_table"]/tbody[tr[count(./*)=4]]')[0].getchildren()):
        ele_row = mon_page.xpath(
            '//table[@class="wiki_table"]/tbody[tr[count(./*)=6]]')[0].getchildren()[index]

        part = dict()
        part['name'] = wep_row[0].text_content()

        part['wep_weaknesses'] = dict()
        part['wep_weaknesses']['severing'] = wep_row[1].text_content()
        part['wep_weaknesses']['blunt'] = wep_row[2].text_content()
        part['wep_weaknesses']['projectile'] = wep_row[3].text_content()

        part['ele_weaknesses'] = dict()
        part['ele_weaknesses']['fire'] = ele_row[1].text_content()
        part['ele_weaknesses']['water'] = ele_row[2].text_content()
        part['ele_weaknesses']['thunder'] = ele_row[3].text_content()
        part['ele_weaknesses']['ice'] = ele_row[4].text_content()
        part['ele_weaknesses']['dragon'] = ele_row[5].text_content()

        parts.append(part)

    try:
        master_rank_mats = format_materials(
            '//div[h3[contains(text(),"Master")]]//div/table/tbody')
    except IndexError:
        master_rank_mats = []

    try:
        low_rank_mats = format_materials(
            '//div[h3[contains(text(),"Low")]]//div/table/tbody')
    except IndexError:
        low_rank_mats = []

    try:
        high_rank_mats = format_materials(
            '//div[h3[contains(text(),"High")]]//div/table/tbody')
    except IndexError:
        high_rank_mats = []

    ailments = []
    for ailment_data in mon_page.xpath('//div[div[@class="tabtitle stun-tab"]]')[0].getchildren():
        ailment = dict()
        ailment['name'] = ailment_data.text_content().replace('⭐', '').strip()
        ailment['rating'] = ailment_data.text_content(
        ).strip()[len(ailment['name']):].replace(' ', '')
        ailments.append(ailment)

    text = f"""
[b]Class: [/b]{mon_class}
[b]Threat Level: [/b]{threat}

[b]Locations:[/b] {locations}

[b]Element:[/b] {element}
[b]Ailments:[/b] {short_ailments}
[b]Weaknesses:[/b] {weaknesses}
[b]Resistances:[/b] {resistances}
"""

    if eff_items:
        text += f"""
[b]Effective Items:[/b] {eff_items}"""

    if ineff_items:
        text += f"""
[b]Ineffective Items:[/b] {ineff_items}
"""

    if kinsect['red'] and kinsect['orange'] and kinsect['white']:
        text += f"""
[b]Kinsect Extracts:[/b]
🟥: {kinsect['red']}
🟧: {kinsect['orange']}
⬜: {kinsect['white']}
"""

    text += f"""
[h1]Weaknesses[/h1]
[b]Weapon Type[/b]
[table]
  [tr]
    [th]Body Part[/th]
    [th][previewimg=26276201;sizeOriginal,floatLeft;severing.png]Severing Damage[/previewimg][/th]
    [th][previewimg=26276197;sizeOriginal,floatLeft;blunt.png]Blunt Damage[/previewimg][/th]
    [th][previewimg=26276199;sizeOriginal,floatLeft;projectile.png]Projectile Damage[/previewimg][/th]
  [/tr]\n"""

    for part in parts:
        text += f"""  [tr]
    [th]{part['name']}[/th]
    [td]{part['wep_weaknesses']['severing']}[/td]
    [td]{part['wep_weaknesses']['blunt']}[/td]
    [td]{part['wep_weaknesses']['projectile']}[/td]
  [/tr]\n"""

    text += """[/table]

[b]Elemental[/b]
[table]
  [tr]
    [th]Body Part[/th]
    [th][previewimg=26276209;sizeOriginal,floatLeft;fire.png]Fire[/previewimg][/th]
    [th][previewimg=26276210;sizeOriginal,floatLeft;water.png]Water[/previewimg][/th]
    [th][previewimg=26276212;sizeOriginal,floatLeft;thunder.png]Thunder[/previewimg][/th]
    [th][previewimg=26276213;sizeOriginal,floatLeft;ice.png]Ice[/previewimg][/th]
    [th][previewimg=26276215;sizeOriginal,floatLeft;dragon.png]Dragon[/previewimg][/th]
  [/tr]\n"""

    for part in parts:
        text += f"""  [tr]
    [th]{part['name']}[/th]
    [td]{part['ele_weaknesses']['fire']}[/td]
    [td]{part['ele_weaknesses']['water']}[/td]
    [td]{part['ele_weaknesses']['thunder']}[/td]
    [td]{part['ele_weaknesses']['ice']}[/td]
    [td]{part['ele_weaknesses']['dragon']}[/td]
  [/tr]\n"""

    text += f"""[/table]

[h1]Ailment Effectiveness[/h1]
[table]
  [tr]
    [th]Ailment[/th]
    [th]Rating[/th]
  [/tr]\n"""

    for ailment in ailments:
        text += f"""  [tr]
    [th]{ailment['name']}[/th]
    [td]{ailment['rating']}[/td]
  [/tr]\n"""

    if len(low_rank_mats) > 0:
        text += """[/table]

[h1]Low Rank Materials[/h1]
[table]
  [tr]
    [th]Material[/th]
    [th]Target[/th]
    [th]Capture[/th]
    [th]Part Break[/th]
    [th]Carve[/th]
    [th]Dropped[/th]
  [/tr]\n"""

        for material in low_rank_mats:
            text += f"""  [tr]
		[th]{material['name']}[/th]
		[td]{material['target']}[/td]
		[td]{material['capture']}[/td]
		[td]{material['part_break']}[/td]
		[td]{material['carve']}[/td]
		[td]{material['dropped']}[/td]
	  [/tr]\n"""

    if len(high_rank_mats) > 0:
        text += """[/table]

[h1]High Rank Materials[/h1]
[table]
  [tr]
    [th]Material[/th]
    [th]Target[/th]
    [th]Capture[/th]
    [th]Part Break[/th]
    [th]Carve[/th]
    [th]Dropped[/th]
  [/tr]\n"""

        for material in high_rank_mats:
            text += f"""  [tr]
    [th]{material['name']}[/th]
    [td]{material['target']}[/td]
    [td]{material['capture']}[/td]
    [td]{material['part_break']}[/td]
    [td]{material['carve']}[/td]
    [td]{material['dropped']}[/td]
  [/tr]\n"""

    if len(master_rank_mats) > 0:
        text += """[/table]

[h1]Master Rank Materials[/h1]
[table]
   [tr]
     [th]Material[/th]
     [th]Target[/th]
     [th]Capture[/th]
     [th]Part Break[/th]
     [th]Carve[/th]
     [th]Dropped[/th]
  [/tr]\n"""

        for material in master_rank_mats:
            text += f"""  [tr]
   [th]{material['name']}[/th]
   [td]{material['target']}[/td]
   [td]{material['capture']}[/td]
   [td]{material['part_break']}[/td]
   [td]{material['carve']}[/td]
   [td]{material['dropped']}[/td]
 [/tr]\n"""

    text += "[/table]"

    return text


# Grab all large monsters pages and save their links with their names
res = requests.get(
    'https://monsterhunterrise.wiki.fextralife.com/Large+Monsters')

tree = lxml.html.fromstring(res.text)
monsters_list = tree.xpath(
    '//*[@id="tagged-pages-container"]')[0].getchildren()

large_monsters = []
apex_monsters = []
for monster in monsters_list:
    mon = {'url': 'http:' +
           monster.attrib['href'], 'name': monster.text_content()}
    if 'Apex' in mon['name']:
        apex_monsters.append(mon)
    else:
        large_monsters.append(mon)

# The lists should already be in order but just in case fextralife fucks them up, we'll sort them by name
large_monsters = sorted(large_monsters, key=lambda monster: monster['name'])
apex_monsters = sorted(apex_monsters, key=lambda monster: monster['name'])

# Iterate through monsters and output bb code for each
if DEBUG_LEVEL >= INFO_LEVEL:
    print('\n==========================\nScraping Large Monster Info\n==========================')
for monster in large_monsters:
    if DEBUG_LEVEL >= INFO_LEVEL:
        print(f'\nINFO: Scraping "{monster["name"]}".')
    mon_page = lxml.html.fromstring(requests.get(monster['url']).text)
    if mon_page.xpath('//*[@id="WikiContent"]/div[1]/h1/strong'):
        if DEBUG_LEVEL >= WARN_LEVEL:
            print('WARN: Page load error. Monster skipped.')
        continue

    pathlib.Path('./Large Monsters/').mkdir(exist_ok=True)
    with open(f"./Large Monsters/{monster['name']}.bb", 'w', encoding='utf-8') as file:
        file.write(format_monster(mon_page))

if DEBUG_LEVEL >= INFO_LEVEL:
    print('\n==========================\nScraping Apex Monster Info\n==========================')
for monster in apex_monsters:
    if DEBUG_LEVEL >= INFO_LEVEL:
        print(f'\nINFO: Scraping "{monster["name"]}".')
    mon_page = lxml.html.fromstring(requests.get(monster['url']).text)
    if mon_page.xpath('//*[@id="WikiContent"]/div[1]/h1/strong'):
        if DEBUG_LEVEL >= WARN_LEVEL:
            print('WARN: Page load error. Monster skipped.')
        continue

    pathlib.Path('./Apex Monsters/').mkdir(exist_ok=True)
    with open(f"./Apex Monsters/{monster['name']}.bb", 'w', encoding='utf-8') as file:
        file.write(format_monster(mon_page))
