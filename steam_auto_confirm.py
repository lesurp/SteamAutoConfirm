import requests
import sys
import re
import time
import random

try:
    EMAILS_FILENAME = sys.argv[1]
except:
    print('Usage is ' + sys.argv[0] + ' EMAILS_FILE')


CONFIRMATION_LINK_REGEX = \
'https://steamcommunity.com/market/confirmlisting/[0-9]*\?accountid=[0-9]*&amp;confirmation_code=[0-9]*'

# putting some random delay between each request in case steam is
# looking for scripts...
# minimum offset is 1, max is 3
# then for each url we ad another delay to this offset which is between 0 and 2
# of course this is not perfect but unless you have 100+ items ton confirm
# nobody will notice
DELAY_OFFSET=random.random()*2 + 1

with open(EMAILS_FILENAME, 'r') as emails_file:
    emails_string = emails_file.read().replace('\n', '')
    compiled_re = re.compile(CONFIRMATION_LINK_REGEX)
    urls = compiled_re.findall(emails_string)
    print('Found ' + str(len(urls)) + ' confirmation urls')
    counter = 1

    for url in urls:
        requests.get(url.replace('&amp;', '&'))
        print('Processed url #' + str(counter++) + ', now sleeping')
        time.sleep(DELAY_OFFSET + random.random()*2)
