import fontforge as ff
import shutil as fs

FONT_DIR = '/home/chenh/font'
COPYRIGHT = 'Made from sarasa by chenh'

def open_font(path):
    return ff.open(path)

def remove_gasp(font):
    font.gasp = ()

def set_cleartype(font):
    font.head_optimized_for_cleartype = 1

def get_version(font):
    return font.version.split(';')[0]

def set_regular_names(font):
    font.fontname = 'MicrosoftYaHei'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'Fullname', 'Microsoft YaHei'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑')
    )

def set_regular_ui_names(font):
    font.fontname = 'MicrosoftYaHeiUI'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 UI'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 UI')
    )

def set_bold_names(font):
    font.fontname = 'MicrosoftYaHeiBold'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Bold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Bold'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Bold'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 Bold'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Bold')
    )

def set_bold_ui_names(font):
    font.fontname = 'MicrosoftYaHeiUIBold'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Bold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Bold'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Bold'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 UI Bold'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 UI Bold')
    )

def set_light_names(font):
    font.fontname = 'MicrosoftYaHeiLight'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Light'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Light'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Light'),
        ('English (US)', 'SubFamily', 'Light'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 Light'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Light')
    )

def set_light_ui_names(font):
    font.fontname = 'MicrosoftYaHeiUILight'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Light'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Light'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Light'),
        ('English (US)', 'SubFamily', 'Light'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 UI Light'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 UI Light')
    )

def gen_regular():
    fs.copy(FONT_DIR + '/sarasa-ui-sc-regular.ttf', FONT_DIR + '/sarasa-ui-sc-regular-ui.ttf')

    font = open_font(FONT_DIR + '/sarasa-ui-sc-regular.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_regular_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-regular-ui.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_regular_ui_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyh.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_bold():
    fs.copy(FONT_DIR + '/sarasa-ui-sc-bold.ttf', FONT_DIR + '/sarasa-ui-sc-bold-ui.ttf')

    font = open_font(FONT_DIR + '/sarasa-ui-sc-bold.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_bold_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-bold-ui.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_bold_ui_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhbd.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_light():
    fs.copy(FONT_DIR + '/sarasa-ui-sc-light.ttf', FONT_DIR + '/sarasa-ui-sc-light-ui.ttf')

    font = open_font(FONT_DIR + '/sarasa-ui-sc-light.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_light_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-light-ui.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_light_ui_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

if __name__ == '__main__':
    gen_regular()
    gen_bold()
    gen_light()
