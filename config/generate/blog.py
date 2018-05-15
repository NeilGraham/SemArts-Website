# For calculating read time and such

import sys
sys.path.insert(0, '../')
import file_manager as FM
sys.path.insert(0, 'generate/')

def main():
    # Get to Blog folder
    FM.change_directory('../../content/blog/')

    # Find each post
    files = FM.list_files()
    posts = []

    for i in range(0,len(files)):
        if files[i] == 'index.md':
            del files[i]
            break

    for i in range(0,len(files)):
        if files[i][-3:] == '.md':
            posts.append({'url' : files[i][:-3]})

    # ----------- Search each file for unordered metadata ----------- #
    find_meta = ['title', 'author_id', 'date', 'description']
    for i in range(0,len(posts)):
        meta = []
        for j in range(0,len(find_meta)):
            meta.append(find_meta[j])

        lines = FM.get_all(posts[i]['url'] + '.md')

        # Search front matter for required metadata
        encountered_before = False
        for j in range(0,len(lines)):
            ln = lines[j].strip()
            if ln == '+++':
                if encountered_before:
                    lines = lines[j+1:]
                    break
                else:
                    encountered_before = True
            # if inside frontmatter
            if encountered_before:
                # see if current line contains required metadata
                for k in range(0,len(meta)):
                    if ln[:len(meta[k])] == meta[k]:
                        # Find the key value separator in line
                        separator = -1
                        value = ''
                        for n in range(len(meta[k]), len(ln)):
                            if ln[n] == '=':
                                value = ln[n+1:].strip()
                        posts[i][meta[k]] = value
                        del meta[k]
                        break
                # If found all metadata
                if len(meta) == 0:
                    # Find end of Front Matter before breaking
                    for k in range(j,len(lines)):
                        if lines[k].strip() == '+++':
                            lines = lines[k+1:]
                            break
                    break

        # ERROR: if could not find all required metadata in frontmatter
        if len(meta) > 0:
            print('\nERROR:')
            print('Could not find ', end='')
            # print each item not able to be found in frontmatter
            for j in range(0,len(meta)):
                print(meta[j], end='')
                # if not last item in meta, print comma separator
                if j < (len(meta) - 1):
                    print(', ', end='')
            print(' in file ' + posts[i] + '.md')
            raise SystemExit

        # Convert date to string in new key
        posts[i]['datestr'] = date_to_string(posts[i]['date'])

        # Get read time from markdown content
        posts[i]['readtime'] = str(get_readtime(lines))
    # --------------------------------------------------------------- #

    # Once finished gathering metadata for each post

    # Arrange blog posts by date
    posts = arrange_by_date(posts)

    # Go back to config folder, then go into toml folder
    FM.change_directory('../../config/toml/')

    # Blog data file name
    file_name = 'blog.toml'

    # Make sure each required item has quotations surrounding them
    rqd_quotes = ['title', 'author_id', 'url', 'description', 'readtime', 'datestr']
    for i in range(0,len(posts)):
        for j in range(0,len(rqd_quotes)):
            key_val = posts[i][rqd_quotes[j]]
            if (key_val[0] == '\'' or key_val[0] == '\"') and key_val[0] == key_val[-1]:
                continue
            else:
                new_string = '\"'
                for k in range(0,len(key_val)):
                    if key_val[k] == '\"':
                        new_string += '\\"'
                    else:
                        new_string += key_val[k]
                new_string += '\"'
                posts[i][rqd_quotes[j]] = new_string


    # TOML table name for each blog post
    table_name = '[[extra.blog]]'

    # Lines to be written to new TOML file
    toml_lines = []
    for i in range(0,len(posts)):
        toml_lines.append(table_name)
        for key, value in posts[i].items():
            toml_lines.append('\t' + str(key) + ' = ' + str(value))
        toml_lines.append('')

    toml_files = FM.list_files()

    for i in range(0,len(toml_files)):
        if file_name == toml_files[i]:
            FM.remove_file(toml_files[i])

    for i in range(0,len(toml_lines)):
        FM.append_substring(file_name, toml_lines[i])

# ---- End Main ------------------------------------------------------------- #


# Get readtime for markdown article
# HEADSUP: Must omit Front-Matter before passing to md_lines
def get_readtime(md_lines):
    # Words Per Minute
    wpm = 275
    # Minutes Per Image (Around 13 seconds)
    mpi = 0.22

    images = 0
    words = 0
    for j in range(0,len(md_lines)):
        ln = md_lines[j].strip()
        if len(ln) == 0:
            continue
        # If ln represents an image
        elif match_ordered_pattern(['![', '](', ')'], ln):
            images += 1
            continue
        # If ln represents a link
        elif match_ordered_pattern(['[', '](', ')'], ln):
            first_bracket = -1
            for k in range(0,len(ln)):
                if ln[k] == '[':
                    first_bracket = k
                elif ln[k] == ']':
                    if first_bracket >= 0:
                        words += len(ln[first_bracket+1:k].split())
                        words += len(ln[:first_bracket].split())
                        continue
                    else:
                        # ERROR: right bracket before left bracket
                        print('\nERROR:')
                        print('Right bracket found before left bracket in link')
                        raise SystemExit
            continue
        omitted_chars = ['#', '&', '*', '>']
        was_found = False
        for k in range(0,len(omitted_chars)):
            # If first char in line is one that should be omitted
            if ln[0] == omitted_chars[k]:
                # Only add words following the first character's string
                words += len(ln.split()[1:])
                was_found = True
                break
        if was_found:
            continue
        words += len(ln.split())

    # Round to nearest half integer
    readtime = round((words/wpm + images*mpi) * 2) / 2
    if readtime % 1 == 0:
        readtime = str(int(readtime))
    elif readtime == 0:
        readtime = "0.5"
    else:
        readtime = str(readtime)

    return readtime


# 'logs' represent a list of dictionaries carrying a
# key, value pair of 'date' and 'yyyy-mm-dd'
def arrange_by_date(logs):
    # Separate year, month, and date in new list, 'dates'
    dates = []
    for i in range(0,len(logs)):
        dates.append({'date':logs[i]['date'].split('-')})
        # associate index to each dictionary pair
        dates[i]['index'] = i
        for n in range(0,len(dates[i]['date'])):
            dates[i]['date'][n] = int(dates[i]['date'][n])

    # Basic sorting method comparing year, then month, then day,
    for i in range(0,len(dates)):
        for j in range(i+1,len(dates)):
            current = dates[i]['date']
            following = dates[j]['date']
            # Compare year, then month, then day;
            # Break if certain one is newer or older
            for k in range(0,len(current)):
                # if current unit of time is greater than following
                if current[k] > following[k]:
                    # Current is newer than following,
                    # continue to next index comparison
                    break
                elif current[k] < following[k]:
                    # Following is newer than current,
                    # Switch the two and continue to next index
                    placeholder = dates[i]
                    dates[i] = dates[j]
                    dates[j] = placeholder
                    break
                # Cannot prove one is older or newer
                # go on to next comparison

    # Rearrange logs in new_logs
    new_logs = []
    for i in range(0,len(dates)):
        index = dates[i]['index']
        new_logs.append(logs[index])

    return new_logs



# Given date format of yyyy-mm-dd, converting to compact string
#   EX: Mar. 27th, 2018
def date_to_string(date):
    months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June',
    'July', 'Aug.', 'Sept.', 'Nov.', 'Oct.', 'Nov.', 'Dec.']
    date = date.split('-')
    for i in range(0,len(date)):
        date[i] = int(date[i])
    num_suffix = ''
    if date[2] % 10 == 1 and date[2] != 11:
        num_suffix = 'st'
    elif date[2] % 10 == 2 and date[2] != 12:
        num_suffix = 'nd'
    elif date[2] % 10 == 3 and date[2] != 13:
        num_suffix = 'rd'
    else:
        num_suffix = 'th'

    return months[date[1]-1]+' '+str(date[2])+num_suffix+', '+str(date[0])






# Find ordered pattern in string
#   Ex: pattern = ['![',     '](',      ')']
#   - This would be for finding an image in a markdown line
def match_ordered_pattern(pattern,string):
    for k in range(0,len(string)):
        if string[k:(k+len(pattern[0]))] == pattern[0]:
            del pattern[0]
            # if entire ordered pattern was found in string
            if len(pattern) == 0:
                return True
    return False


main()
