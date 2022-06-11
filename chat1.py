def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines 

def convert(lines):
    person = None
    Ray_word_count = 0
    Ray_sticker_count = 0
    Ray_picture_count = 0
    Ziv_word_count = 0
    Ziv_sticker_count = 0
    Ziv_picture_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Ray':
            if s[3] == 'sticker':
                Ray_sticker_count += 1
            elif s[3] == 'picture':
                Ray_picture_count += 1
            else:
                for msg in s[3:]:
                    Ray_word_count += len(msg)
        elif name == 'Ziv':
            if s[3] == 'sticker':
                Ziv_sticker_count += 1
            elif s[3] == 'picture':
                Ziv_picture_count += 1
            else:
                for msg in s[3:]:
                    Ziv_word_count += len(msg)
    print('Ray says', Ray_word_count, 'words,', 'sent', Ray_sticker_count, 'stickers', 'and sent', Ray_picture_count, 'pictures')
    print('Ziv says', Ziv_word_count, 'words,', 'sent', Ziv_sticker_count, 'stickers', 'and sent', Ziv_picture_count, 'pictures')


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('[LINE]Ray.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main()
