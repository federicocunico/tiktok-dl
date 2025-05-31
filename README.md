# TokTok video downloader


## Installations

### FFMPEG
Install ffmpeg: 

```bash
winget install ffmpeg
```

### Firefox
```bash
winget intstall Mozilla.Firefox
```

### Log In
Login with TikTok on firefox, leave it open!

### get MS_token
From cookies, get ms_token and save it in `ms_token.txt`

### Launch

```bash
python get_dl_links.py <username>
python downlaod_from_file.py
```

