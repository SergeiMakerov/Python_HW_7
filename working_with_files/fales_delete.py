# Вариант удаления всего каталога целиком с содержимым.
# import shutil

# shutil.rmtree('dir')

import os
from pathlib import Path
os.remove('names.txt')
#Path('one_more_dir/one_more.txt').unlink()
