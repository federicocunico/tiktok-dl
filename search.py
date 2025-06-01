import asyncio
import datetime
import os
import yt_dlp
from TikTokApi import TikTokApi
import argparse

from tiktok_utils import dump_link

# parser = argparse.ArgumentParser(description="Fetch TikTok trending videos and save their download links.")
# parser.add_argument("username", type=str, help="TikTok username to fetch videos from")
# parser.add_argument("--count", type=int, default=10, help="Number of videos to fetch (default: 10)")

# args = parser.parse_args()

ms_token = open("ms_token.txt", "r").read().strip()

parser = argparse.ArgumentParser(description="Fetch TikTok trending videos and save their download links.")
parser.add_argument("--q", type=str, help="Search query to find videos (e.g., 'funny')")
parser.add_argument("--c", type=int, default=0, help="Cursor for pagination (default: 0)")
parser.add_argument("--o", type=str, default=None, help="Output file to save video links (default: 'links.txt')")

args = parser.parse_args()


async def search_videos(count=10):
    query = args.q
    output_file = args.o
    cursor = args.c
    if output_file is None:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        output_file = f"{today}_{query}_links.txt"

    with open(output_file, "w") as f:
        f.write("")  # Clear the file before writing new links

    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))

        tag = api.hashtag(name=query)
        async for video in tag.videos(cursor=cursor):
            username = video.author.username
            if username.startswith("@"):
                username = username[1:] # Remove '@' if present
            # user_id = video.author.user_id
            dump_link(output_file, video, username)



async def main():
    await search_videos(count=10)


if __name__ == "__main__":
    asyncio.run(main())




# async def get_video_example():
#     async with TikTokApi() as api:
#         await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))
#         video = api.video(
#             "https://www.tiktok.com/@therock/video/6829267836783971589"
#         )

#         async for related_video in video.related_videos(count=10):
#             print(related_video)
#             print(related_video.as_dict)

#         video_info = await video.info()  # is HTML request, so avoid using this too much
#         print(video_info)
#         video_bytes = await video.bytes()
#         with open("video.mp4", "wb") as f:
#             f.write(video_bytes)


# if __name__ == "__main__":
#     asyncio.run(get_video_example())