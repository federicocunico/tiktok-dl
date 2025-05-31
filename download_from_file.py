import os
from datetime import datetime
from tqdm import tqdm 
from time import sleep

folder = f"saved_videos-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
if not os.path.exists(folder):
    os.makedirs(folder)

# cmd = "yt-dlp --cookies-from-browser firefox {0}"
cmd = f'yt-dlp --cookies-from-browser firefox -q -o "{folder}/{{1}}.%(ext)s" {{0}}'

file_with_links = "links.txt"

def main():
    if not os.path.exists(file_with_links):
        print(f"File {file_with_links} does not exist.")
        return

    with open(file_with_links, "r") as file:
        links = file.readlines()

    for link in tqdm(links, desc="Downloading...", total=len(links)):
        link = link.strip()
        link, dst = link.split("|")
        if link:
            command = cmd.format(link, dst)
            print(f"Executing: {command}")
            os.system(command)
            sleep(0.5)

if __name__ == "__main__":
    main()