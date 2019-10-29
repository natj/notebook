import re

# message divider
REmsgb = re.compile(r"\s*[-]{40}")

# name H1 (# blaa)
REname = re.compile(r"^[#]{1}\s(.*)")

# subtitle H2 (## blaa)
REtitle = re.compile(r"^[#]{2}\s(.*)")

# date
REdate = re.compile(r"\s*created:\s*(.*)")
REmdate = re.compile(r"\s*modified:\s*(.*)")

# hash
REhash = re.compile(r"\s*---:(.*)")

# beautifying note division line (for skipping)
REdiv = re.compile(r"^[-]{62}")


# detect any task list; see https://www.debuggex.com/#cheatsheet

#almost working oneliner (python regex bug prevents this)
#REtasks = re.compile(r"\s*-\s*(?:\[\s*\S*\s*\])??(?:\[\s*\])?\s*(.+)")
REtasks = re.compile(r"\s*-\s*(?:\[\s*\])?\s*(.+)")
REtask_compl = re.compile(r"\[\s*\S?\s*\]\s*(.*)")
