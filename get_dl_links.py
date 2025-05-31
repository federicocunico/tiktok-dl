import asyncio
import os
import yt_dlp
from TikTokApi import TikTokApi
import argparse

parser = argparse.ArgumentParser(description="Fetch TikTok trending videos and save their download links.")
parser.add_argument("username", type=str, help="TikTok username to fetch videos from")
parser.add_argument("--count", type=int, default=10, help="Number of videos to fetch (default: 10)")

args = parser.parse_args()

ms_token = open("ms_token.txt", "r").read().strip()
with open("links.txt", "w") as f:
    f.write("")  # Clear the file before writing new links


async def fetch_trending_videos(count=10):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))

        username = args.username
        if not username.startswith("@"):
            username = "@" + username

        # get user info
        user = api.user(username)
        user_data = await user.info()
        user_id = f'@{user_data["userInfo"]["user"]["uniqueId"]}'

        async for video in user.videos(count=10):
            print(video)
            print(video.as_dict)
            video_url = "https://www.tiktok.com/{}/video/{}".format(user_id, video.id)
            fname = f"{username}_{video.id}"

            with open("links.txt", "a") as f:
                f.write(f"{video_url}|{fname}\n")
            
            asyncio.sleep(0.1)


async def main():
    await fetch_trending_videos(count=10)


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