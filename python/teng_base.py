#!/usr/bin/env python
# -*- coding: utf-8 -*-

import teng


TEMPLATE = """
<html>
<?teng include file="common-head.html" ?>
    <body>
        <?teng frag row?><p>${rnum}
            <?teng frag col?>${cnum} <?teng endfrag?>
        </p><?teng endfrag?>
    </body>
</html>
"""


def createFragment():
    return {
        'row': [
            {'rnum': 'A', 'col': [{'cnum': 1}, {'cnum': 2}]},
            {'rnum': 'B', 'col': [{'cnum': 1}, {'cnum': 2}]}
        ]
    }


def main():
    tengEngine = teng.Teng(root='templates')
    result = tengEngine.generatePage(templateString=TEMPLATE, data=createFragment())
    print result['output']
    print result['status'], " errorLog: ", result['errorLog']


if __name__ == '__main__':
    main()
