
## Get files inside toml folder w/ respect to load order,
## then compile into the main directory's config.toml file

import file_manager as FM
from datetime import datetime

# ----------------------------- #

load_order = ['top', 'people', 'blog', 'companies', 'articles', 'books']

# ----------------------------- #

FM.change_directory('toml')

config_lines = []

for i in range(0,len(load_order)):
    file_lines = FM.get_all(load_order[i]+'.toml')
    for n in range(0,len(file_lines)):
        config_lines.append(file_lines[n])
    config_lines.append('')

FM.change_directory('../../')

if FM.file_exists('config.toml'):
    file_lines = FM.get_all('config.toml')
    if file_lines != config_lines:
        FM.change_directory('config')
        FM.create_directory('backup')
        FM.change_directory('backup')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        FM.create_directory(str(current_time))
        FM.change_directory(str(current_time))
        for i in range(0,len(file_lines)):
            FM.append_substring('config.toml', file_lines[i])
        FM.change_directory('../../../')
    FM.remove_file('config.toml')

for i in range(0,len(config_lines)):
    print(config_lines[i])

for i in range(0,len(config_lines)):
    FM.append_substring('config.toml', config_lines[i])
