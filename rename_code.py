from fontTools.ttLib import TTFont


TMP_DIR = './temp'
DST_DIR = './result'
VERSION = '2503'
COPYRIGHT = 'Builder: chenh; Date: 2025-03-11; Sources: Source Han Sans & Iosevka'


RENAME_FONTS = [
    ('SarasaMonoSC-Regular.ttf', 'Regular', 'HansCode-Regular.ttf'),
    ('SarasaMonoSC-Bold.ttf', 'Bold', 'HansCode-Bold.ttf'),
    ('SarasaMonoSC-Oblique.ttf', 'Italic', 'HansCode-Italic.ttf'),
    ('SarasaMonoSC-BoldOblique.ttf', 'Bold Italic', 'HansCode-BoldItalic.ttf')
]


def set_names(src, weight, out):
    family_name = 'HansCode'
    font_name = f'HansCode{weight}'

    font = TTFont(f'{TMP_DIR}/{src}')
    name_table = font['name']

    name_table.names = []

    name_table.setName(COPYRIGHT, 0, 3, 1, 0x0409)
    name_table.setName(family_name, 1, 3, 1, 0x0409)
    name_table.setName(weight, 2, 3, 1, 0x0409)
    name_table.setName(font_name, 3, 3, 1, 0x0409)
    name_table.setName(font_name, 4, 3, 1, 0x0409)
    name_table.setName(VERSION, 5, 3, 1, 0x0409)
    name_table.setName(font_name, 6, 3, 1, 0x0409)

    font.save(f'{DST_DIR}/{out}')


if __name__ == '__main__':
    for src, weight, out in RENAME_FONTS:
        set_names(src, weight, out)
