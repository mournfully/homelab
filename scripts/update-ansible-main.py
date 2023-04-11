import os
import glob

INPUT_DIR = "/mnt/data/work/homelab/ansible/playbooks"
PATTERN = "*.yml"
OUTPUT_FILE = "/mnt/data/work/homelab/ansible/main.yml"

# get absolute playbook file paths
files = []
files = glob.glob(os.path.join(INPUT_DIR, PATTERN))
files.sort()

# get playbook name function
def get_name(file):
    with open (file, 'r') as lines:
        for line in lines:
            for word in line.split():
                if word == 'name:':
                    return line.replace("- name: ","").replace("\n","")

# append formatted output
with open(OUTPUT_FILE, 'a') as f:
    f.write("\n")
    for file in files:
        f.write("- name: " + get_name(file) + "\n")
        f.write("  import_playbook: playbooks/" + os.path.basename(file) + "\n")
        f.write("\n")
