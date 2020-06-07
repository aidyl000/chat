def read_file(filename):
    lines = []
    with open('line.txt', 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    lydia_word_count = 0
    yan_word_count = 0
    lydia_sticker_count = 0
    yan_sticker_count = 0
    lydia_image_count = 0
    yan_image_count = 0
    for line in lines:
        s = line.split(' ') # 切割後會變清單
        time = s[0]
        name = s[1]
        if name == 'Lydia':
            if s[3] == 'Stickers':
                lydia_sticker_count += 1
            elif s[3] == 'Picture':
                lydia_image_count += 1
            else:
                for m in s[3:]:
                    lydia_word_count += len(m)
        elif name == 'Yan':
            if s[3] == 'Stickers':
                yan_sticker_count += 1
            elif s[3] == 'Picture':
                yan_image_count += 1
            else:
                for m in s[3:]:
                    yan_word_count += len(m)
    print('Lydia說了', lydia_word_count, '字')
    print('Lydia傳了', lydia_sticker_count, '個貼圖' )
    print('Lydia傳了', lydia_image_count, '張圖片' )
    print('Yan說了', yan_word_count, '字')
    print('Yan傳了', yan_sticker_count, '個貼圖')
    print('Yan傳了', yan_image_count, '張圖片')
             

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('line.txt')
    lines = convert(lines)
    # write_file('line_output.txt', lines)


main()