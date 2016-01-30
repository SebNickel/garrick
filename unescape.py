def unescape(string):

    byte_string = string.encode('utf8')
    unescaped_string = byte_string.decode('unicode_escape')

    return unescaped_string
