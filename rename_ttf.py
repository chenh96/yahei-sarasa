from fontTools.ttLib import TTFont, TTCollection
# import fontforge
import shutil

TMP_DIR = './temp'
DST_DIR = './result'
VERSION = '2501'
COPYRIGHT = 'Builder: chenh; Date: 2025-02-02; Sources: Source Han Sans 2.004 & Segoe UI 5.67'

FEATURE_FONTS = [
    ('SarasaUiSC-Regular.ttf', 'SarasaUiSC-Regular-NoFeat.ttf'),
    ('SarasaUiSC-Bold.ttf', 'SarasaUiSC-Bold-NoFeat.ttf'),
    ('SarasaUiSC-Light.ttf', 'SarasaUiSC-Light-NoFeat.ttf')
]

KEEP_FEATURES = [
    'abvm', 'abvs', 'akhn', 'blwf', 'blwm', 'blws', 'ccmp', 'cfar', 'cjct', 'curs',
    'dist', 'dtls', 'fin2', 'fin3', 'fina', 'flac', 'half', 'haln', 'init', 'isol',
    'ljmo', 'locl', 'ltra', 'ltrm', 'mark', 'med2', 'medi', 'mkmk', 'nukt', 'pref',
    'pres', 'pstf', 'psts', 'rclt', 'rkrf', 'rlig', 'rphf', 'rtla', 'rtlm', 'rvrn',
    'ssty', 'stch', 'tjmo', 'vjmo', 'DELT'
]

RENAME_FONTS = [
    ('SarasaUiSC-Regular-NoFeat.ttf', 'Regular', False),
    ('SarasaUiSC-Regular-NoFeat.ttf', 'Regular', True),
    ('SarasaUiSC-Bold-NoFeat.ttf', 'Bold', False),
    ('SarasaUiSC-Bold-NoFeat.ttf', 'Bold', True),
    ('SarasaUiSC-Light-NoFeat.ttf', 'Light', False),
    ('SarasaUiSC-Light-NoFeat.ttf', 'Light', True),
]

MERGE_FONTS = [
    ('MicrosoftYaHei.ttf', 'MicrosoftYaHeiUI.ttf', 'msyh.ttc'),
    ('MicrosoftYaHeiBold.ttf', 'MicrosoftYaHeiUIBold.ttf', 'msyhbd.ttc'),
    ('MicrosoftYaHeiLight.ttf', 'MicrosoftYaHeiUILight.ttf', 'msyhl.ttc'),
]

SIMSUN_FONTS = [
    ('SarasaUiSC-Regular.ttf', 'SimSun', '宋体'),
    ('SarasaUiSC-Regular.ttf', 'NSimSun', '新宋体'),
    ('SarasaUiSC-Regular.ttf', 'SimSun-ExtB', '宋体-扩展'),
]

MERGE_SIMSUN_FONTS = [
    ('SimSun.ttf', 'NSimSun.ttf', 'simsun.ttc')
]


def remove_features(src, dst):
    font = TTFont(f'{TMP_DIR}/{src}')
    keep_features = {tag.lower() for tag in KEEP_FEATURES}  # 不区分大小写

    for table in ['GSUB', 'GPOS']:
        if table not in font:
            continue

        features = font[table].table.FeatureList

        records = [
            rec for rec in features.FeatureRecord
            if rec.FeatureTag.lower() in keep_features
        ]

        features.FeatureRecord = records
        features.FeatureCount = len(records)

        if not records:
            del font[table]

    font.save(dst)


def set_names(src, weight, ui):
    font_name = f'MicrosoftYaHei{'UI' if ui else ''}{
        weight if weight != 'Regular' else ''}'
    family_name = f'Microsoft YaHei{' UI' if ui else ''}'
    full_name = f'Microsoft YaHei{' UI' if ui else ''}{
        (' ' + weight) if weight != 'Regular' else ''}'
    family_name_sc = f'微软雅黑{' UI' if ui else ''}'
    full_name_sc = f'微软雅黑{' UI' if ui else ''}{
        (' ' + weight) if weight != 'Regular' else ''}'

    font = TTFont(f'{TMP_DIR}/{src}')
    name_table = font['name']

    name_table.names = []

    name_table.setName(COPYRIGHT, 0, 3, 1, 0x0409)
    name_table.setName(family_name, 1, 3, 1, 0x0409)
    name_table.setName(weight, 2, 3, 1, 0x0409)
    name_table.setName(font_name, 3, 3, 1, 0x0409)
    name_table.setName(full_name, 4, 3, 1, 0x0409)
    name_table.setName(VERSION, 5, 3, 1, 0x0409)
    name_table.setName(font_name, 6, 3, 1, 0x0409)

    name_table.setName(family_name_sc, 1, 3, 1, 0x0804)
    name_table.setName(full_name_sc, 4, 3, 1, 0x0804)

    font.save(f'{TMP_DIR}/{font_name}.ttf')


def set_simsun_names(src, name, name_sc):
    weight = 'Regular'

    font = TTFont(f'{TMP_DIR}/{src}')
    name_table = font['name']

    name_table.names = []

    name_table.setName(COPYRIGHT, 0, 3, 1, 0x0409)
    name_table.setName(name, 1, 3, 1, 0x0409)
    name_table.setName(weight, 2, 3, 1, 0x0409)
    name_table.setName(name, 3, 3, 1, 0x0409)
    name_table.setName(name, 4, 3, 1, 0x0409)
    name_table.setName(VERSION, 5, 3, 1, 0x0409)
    name_table.setName(name, 6, 3, 1, 0x0409)

    name_table.setName(name_sc, 1, 3, 1, 0x0804)
    name_table.setName(name_sc, 4, 3, 1, 0x0804)

    font.save(f'{TMP_DIR}/{name}.ttf')


def merge(src1, src2, dst):
    ttc = TTCollection()

    ttf1 = TTFont(f'{TMP_DIR}/{src1}')
    ttf2 = TTFont(f'{TMP_DIR}/{src2}')

    ttc.fonts.append(ttf1)
    ttc.fonts.append(ttf2)

    ttc.save(f'{DST_DIR}/{dst}')


if __name__ == '__main__':
    for src, dst in FEATURE_FONTS:
        remove_features(src, dst)
    for src, weight, ui in RENAME_FONTS:
        set_names(src, weight, ui)
    for src1, src2, dst in MERGE_FONTS:
        merge(src1, src2, dst)
    for src, weight, ui in SIMSUN_FONTS:
        set_simsun_names(src, weight, ui)
    for src1, src2, dst in MERGE_SIMSUN_FONTS:
        merge(src1, src2, dst)
    shutil.move(f'{TMP_DIR}/SimSun-ExtB.ttf', f'{DST_DIR}/simsunb.ttf')
