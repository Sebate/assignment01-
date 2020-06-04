#!C:\Users\Botshelo.Sebate\PycharmProjects\assignment01-\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'res==0.1.7','console_scripts','res'
__requires__ = 'res==0.1.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('res==0.1.7', 'console_scripts', 'res')()
    )
