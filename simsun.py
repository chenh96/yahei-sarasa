import fontforge as ff
import shutil as fs

FONT_DIR = '/home/chenh/font'
OUT_DIR = '/home/chenh/font/result'
COPYRIGHT = 'Made from sarasa by chenh'

def open_font(path):
    return ff.open(path)

def remove_gasp(font):
    font.gasp = ()

def set_cleartype(font):
    font.head_optimized_for_cleartype = 1

def get_version(font):
    return font.version.split(';')[0]

def set_simsun_names(font):
    font.fontname = 'SimSun'
    font.familyname = 'SimSun'
    font.fullname = 'SimSun'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT), 
        ('English (US)', 'Family', 'SimSun'), 
        ('English (US)', 'SubFamily', 'Regular'), 
        ('English (US)', 'UniqueID', 'SimSun'), 
        ('English (US)', 'Fullname', 'SimSun'), 
        ('English (US)', 'Version', get_version(font)), 
        ('English (US)', 'PostScriptName', 'SimSun'), 
        ('Chinese (PRC)', 'Family', '宋体'), 
        ('Chinese (PRC)', 'Fullname', '宋体')
    )

def set_new_simsun_names(font):
    font.fontname = 'NSimSun'
    font.familyname = 'NSimSun'
    font.fullname = 'NSimSun'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT), 
        ('English (US)', 'Family', 'NSimSun'), 
        ('English (US)', 'SubFamily', 'Regular'), 
        ('English (US)', 'UniqueID', 'NSimSun'), 
        ('English (US)', 'Fullname', 'NSimSun'), 
        ('English (US)', 'Version', get_version(font)), 
        ('English (US)', 'PostScriptName', 'NSimSun'), 
        ('Chinese (PRC)', 'Family', '新宋体'), 
        ('Chinese (PRC)', 'Fullname', '新宋体')
    )

def set_simsun_ext_names(font):
    font.fontname = 'SimSun-ExtB'
    font.familyname = 'SimSun-ExtB'
    font.fullname = 'SimSun-ExtB'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT), 
        ('English (US)', 'Family', 'SimSun-ExtB'), 
        ('English (US)', 'SubFamily', 'Regular'), 
        ('English (US)', 'UniqueID', 'SimSun-ExtB'), 
        ('English (US)', 'Fullname', 'SimSun-ExtB'), 
        ('English (US)', 'Version', get_version(font)), 
        ('English (US)', 'PostScriptName', 'SimSun-ExtB')
    )

def gen_simsun_ttc():
    fs.copy(FONT_DIR + '/sarasa-ui-sc-regular.ttf', FONT_DIR + '/sarasa-ui-sc-regular-new.ttf')

    font = open_font(FONT_DIR + '/sarasa-ui-sc-regular.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_simsun_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-regular-new.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_new_simsun_names(font_ui)

    font.generateTtc(OUT_DIR + '/simsun.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_simsun_ext():
    font = open_font(FONT_DIR + '/sarasa-ui-sc-regular.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_simsun_ext_names(font)
    font.generate(OUT_DIR + '/simsunb.ttf')

if __name__ == '__main__':
    gen_simsun_ttc()
    gen_simsun_ext()
    