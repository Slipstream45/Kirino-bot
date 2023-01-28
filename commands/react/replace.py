import os
import re

directory = '/home/sakai01/Documents/Discord-Bot-Stuff/commands/react'

for filename in os.listdir(directory):
    if filename.endswith('.py'):
        file_path = os.path.join(directory, filename)
        with open(file_path) as f:
            s = f.read()

        s = re.sub("run", "run", s)

        with open(file_path, "w") as f:
            f.write(s)

