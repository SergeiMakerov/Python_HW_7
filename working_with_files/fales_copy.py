import shutil
shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')


# Если стоит задача скопировать каталог со всем его содержимым в новое место,
# модуль предоставляет функции copytree.
# import shutil
# shutil.copytree('dir', 'one_more_dir')
