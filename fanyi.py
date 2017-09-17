"""命令行翻译

Usage:
    fanyi  <word>


Examples:
   fanyi 你好
   # 英文短语需要加引号
   fanyi 'I love you'
"""

import requests
from docopt import docopt


def translate_word():
    arguments = docopt(__doc__)
    data = {
        'f': 'auto',
        't': 'auto',
        'w': arguments['<word>']

    }
    url = 'http://fy.iciba.com/ajax.php?a=fy'
    r = requests.post(url, data=data)
    content = r.json().get('content')
    out = content.get('out')
    if out:
        out = out.replace('<br/>', '')
        print(out)
    else:
        out = content.get('word_mean')
        print('\n'.join(out))


if __name__ == '__main__':
    translate_word()
