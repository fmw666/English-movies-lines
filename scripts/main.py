'''
# lines.txt

1.Hi,Aunt cass
2.Cass:Are you guys okay? Tell me you’re okay...
3.Hiro:We’re fine.
4.Tadashi:We’re okay
...

备注：有人名则添加md超链接标签

# output.txt

> **Hi,Aunt cass**

> **[Cass](#welcome) : Are you guys okay? Tell me you’re okay...**

> **[Hiro](#welcome) : We’re fine.**

> **[Tadashi](#welcome) : We’re okay**

...

'''

import re

with open('lines.txt', 'r', encoding='utf-8') as fp:
    output = []
    for line in fp.readlines():
        # 正则表达式匹配
        is_matching = re.match(r'\d+.[a-zA-Z]+:', line)
        # 是人名加台词情况
        if is_matching:
            newline = re.sub(r'\d+.', '> **[', line)
            newline = re.sub(r':', '](#welcome) : ', newline)
            newline = re.sub(r'\n', '**\n\n' ,newline)
            print(newline)
        # 不是的话...
        else:
            newline = re.sub(r'\d+.', '> **', line)
            newline = re.sub(r'\n', '**\n\n', newline)
            print(newline)

        output.append(newline)
        
with open('output.txt', 'w', encoding='utf-8') as op:
    op.writelines(output)
