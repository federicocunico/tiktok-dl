# def dump_link(output_file: str, video, username: str, user_id: str):

#     if not username.startswith("@"):
#         username = f"@{username}"
#     video_url = "https://www.tiktok.com/{}/video/{}".format(user_id, video.id)
#     fname = f'{username.replace("@", "")}_{video.id}'

#     with open(output_file, "a") as f:
#         f.write(f"{video_url}|{fname}\n")


def dump_link(output_file: str, video, username: str):

    if not username.startswith("@"):
        username = f"@{username}"
    video_url = "https://www.tiktok.com/{}/video/{}".format(username, video.id)
    fname = f'{username.replace("@", "")}_{video.id}'

    with open(output_file, "a") as f:
        f.write(f"{video_url}|{fname}\n")
