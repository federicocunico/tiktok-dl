import os
from datetime import datetime
from tqdm import tqdm 
from time import sleep
import argparse

parser = argparse.ArgumentParser(description="Download videos from TikTok links stored in a file.")
parser.add_argument("--file_with_links", type=str, default="links.txt",
                    help="File containing TikTok video links and destination names (default: links.txt)")
args = parser.parse_args()

query = args.file_with_links.split("_")[1]  # Extract query from file name

folder = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')} - {query}"
if not os.path.exists(folder):
    os.makedirs(folder)

# cmd = "yt-dlp --cookies-from-browser firefox {0}"
cmd = f'yt-dlp --cookies-from-browser firefox -q -o "{folder}/{{1}}.%(ext)s" {{0}}'


def main():
    file_with_links = args.file_with_links

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