import get, gen

if __name__ == '__main__':
    url = get.get_latest()
    print('Latest url: ' + url)
    get.clear_dir(get.DOWNLOAD_DIR)
    print('Clear directory: ' + get.DOWNLOAD_DIR)
    path = get.download(url)
    print('Download path: ' + path)
    get.unzip(path)
    print('Downlaod finished')
    gen.gen_regular()
    print('Regular generated')
    gen.gen_bold()
    print('Bold generated')
    gen.gen_light()
    print('Light generated')
    print('Finished')
