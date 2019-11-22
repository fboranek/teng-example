#!/usr/bin/env python
# -*- coding: utf-8 -*-

import teng


TEMPLATE = """
<html>
<?teng include file="common-head.html" ?>
    <body>
        <!-- value in root -->
        <p>${var1}</p>
        <p>${.var1}</p>

        <!-- value in fragment (dic or list) -->
        <?teng frag global?>
            <p>${var2} - ${var3}</p>
        <?teng endfrag?>
        <!-- value in fragment (dic) -->
        <p>${$$global.var2} - ${$$global.var3}</p>
        <!-- value in fragment (dic) addressed from root -->
        <p>${$$.global.var2} - ${$$.global.var3}</p>

        <?teng frag row?>
            <p>
                <!-- value directly in this fragment -->
                - ${rnum}
                <!-- value from sub-framgment -->
                - ${$$dic.var4}
                <!-- value from root fragment -->
                - ${.var1}
                <!-- value from fragment adresed from root -->
                - ${$$.global.var2}
            <br>
                <!-- only way for list -->
                <?teng frag col?>${cnum} <?teng endfrag?>
            </p>
        <?teng endfrag?>
    </body>
</html>
"""


def createFragment():
    return {
        'var1': 'val1',
        'global': {
            'var2': 'val2',
            'var3': 3
        },
        'row': [
            {'rnum': 'A', 'dic': {'var4': 10}, 'col': [{'cnum': 1}, {'cnum': 2}]},
            {'rnum': 'B', 'dic': {'var4': 20}, 'col': [{'cnum': 1}, {'cnum': 2}]}
        ]
    }


def main():
    tengEngine = teng.Teng(root='templates')
    result = tengEngine.generatePage(templateString=TEMPLATE, data=createFragment())
    print result['output']
    print result['status'], " errorLog: ", result['errorLog']


if __name__ == '__main__':
    main()
