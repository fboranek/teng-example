#!/usr/bin/env python
# -*- coding: utf-8 -*-

import teng
import os


TEMPLATE = """
<html>
<?teng include file="in-memmory-common-head.html" ?>
    <body>
        <?teng frag row?><p>${rnum}
            <?teng frag col?>${cnum} <?teng endfrag?>
        </p><?teng endfrag?>
    </body>
</html>
"""


class FileSystem:
    def read(self, name):
        if name == 'in-memmory-common-head.html':
            return """
        <head>
            <title>Example page: ${title}</title>
        </head>
        """

        # raise Exception("gggggg") # converts exception to RuntimeError: Failed to call python fileSystem callback.
        # return None # rise RuntimeError: No such file '.../teng-example/build/templates/some-file.html in python fileSystem callback.
        return None

    def hash(self, name):
        return 0


def createFragment():
    return {
        'row': [
            {'rnum': 'A', 'col': [{'cnum': 1}, {'cnum': 2}]},
            {'rnum': 'B', 'col': [{'cnum': 1}, {'cnum': 2}]}
        ]
    }


def main():
    tengEngine = teng.Teng(root='templates', fileSystem=FileSystem())
    result = tengEngine.generatePage(templateString=TEMPLATE, data=createFragment())
    print result['output']
    print result['status'], " errorLog: ", result['errorLog']


if __name__ == '__main__':
    main()
