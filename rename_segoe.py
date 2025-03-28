from fontTools.ttLib import TTFont
import fontforge


SRC_DIR = './segoe'
REF_DIR = './inter'
DST_DIR = './temp'

FONTS = [
    ('segoeui.ttf', 'Inter-Regular.ttf'),
    ('segoeuib.ttf', 'Inter-Bold.ttf'),
    ('segoeuil.ttf', 'Inter-Light.ttf')
]


def subset_font(font_a_path, font_b_path, output_path):
    font_a = fontforge.open(font_a_path)
    font_b = fontforge.open(font_b_path)

    glyphs_in_b = set(glyph.glyphname for glyph in font_b.glyphs())

    for glyph in font_a.glyphs():
        if glyph.glyphname not in glyphs_in_b:
            font_a.removeGlyph(glyph.glyphname)

    font_a.generate(output_path)
    font_a.close()
    font_b.close()

    
def copy_font_info(src, ref, dst):
    src_font = TTFont(src)
    ref_font = TTFont(ref)

    src_font['name'] = ref_font['name']
    src_font['head'] = ref_font['head']
    src_font['OS/2'] = ref_font['OS/2']

    src_font.save(dst)


if __name__ == '__main__':
    for src, dst in FONTS:
        subset_font(f'{SRC_DIR}/{src}', f'{REF_DIR}/{dst}', f'{DST_DIR}/{src}')
        copy_font_info(f'{DST_DIR}/{src}', f'{REF_DIR}/{dst}', f'{DST_DIR}/{dst}')