import os


# EACH DIRECTORY IS A NEW PROJECT

def create_new_dir(directory):
    if not os.path.exists(directory):
        print('creating project ' + directory)
        os.makedirs(directory)


create_new_dir("Quotes_to_scrape")


# CREATE QUEUE AND CRAWLED FILES

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')


# CREATING A FILE

def write_file(path, data):
    f = open(path, 'w')
    f.write(data + '\n')
    f.close()


create_data_files("Quotes_to_scrape", "http://quotes.toscrape.com/")


# APPEND TO FILE

def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


# DELETE FILE CONTENTS

def delete_file_contents(path):
    with open(path, 'w'):
        pass


# READ A FILE AND CONVERT IT INTO A SET OF ITEMS

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))

    return results


# ITERATE THROUGH A SET

def set_to_file(links, file):
    delete_file_contents(file)

    for link in links:
        append_to_file(file,link)
