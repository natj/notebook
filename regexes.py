import re

#message divider
REmsgb  = re.compile(r'\s*[-]{40}')

#name H1 (# blaa)
REname  = re.compile(r'^[#]{1}\s(.*)')

#subtitle H2 (## blaa)
REtitle = re.compile(r'^[#]{2}\s(.*)')

#date
REdate  = re.compile(r'\s*created:\s*(.*)')
REmdate = re.compile(r'\s*modified:\s*(.*)')

#hash
REhash  = re.compile(r'\s*---:(.*)')






