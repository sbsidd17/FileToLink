from info import BIN_CHANNEL, STREAM_URL, temp
from web.utils.custom_dl import TGCustomYield
import urllib.parse
import secrets
import mimetypes
import aiofiles
import aiohttp


def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

async def fetch_properties(message_id):
    media_msg = await temp.BOT.get_messages(BIN_CHANNEL, message_id)
    file_properties = await TGCustomYield().generate_file_properties(media_msg)
    file_name = file_properties.file_name if file_properties.file_name \
        else f"{secrets.token_hex(2)}.jpeg"
    mime_type = file_properties.mime_type if file_properties.mime_type \
        else f"{mimetypes.guess_type(file_name)}"
    return file_name, mime_type


async def render_page(message_id):
    file_name, mime_type = await fetch_properties(message_id)
    src = urllib.parse.urljoin(STREAM_URL, str(message_id))

    audio_formats = ['audio/mpeg', 'audio/mp4', 'audio/x-mpegurl', 'audio/vnd.wav', 'audio/ogg', 'audio/aac'] # Added common audio types
    video_formats = ['video/mp4', 'video/avi', 'video/ogg', 'video/h264', 'video/h265', 'video/x-matroska', 'video/webm'] # Added webm

    if mime_type.lower() in video_formats:
        async with aiofiles.open('web/template/req.html') as r:
            heading = 'Watch {}'.format(file_name)
            # req.html has 6 placeholders: page title, h1 title, video src, mx player src, mx player title, vlc src
            html = (await r.read()) % (heading, file_name, src, src, file_name, src)
    elif mime_type.lower() in audio_formats:
        async with aiofiles.open('web/template/req.html') as r:
            heading = 'Listen {}'.format(file_name)
            # req.html has 6 placeholders: page title, h1 title, video src, mx player src, mx player title, vlc src
            # Using <video> tag for audio as well, Plyr handles it.
            html = (await r.read()) % (heading, file_name, src, src, file_name, src)
    else:
        async with aiofiles.open('web/template/dl.html') as r:
            heading = 'Download {}'.format(file_name) # Define heading for dl.html
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u: # src here is the download link
                    file_size = get_size(u.headers.get('Content-Length'))
                    # dl.html has 4 placeholders: page title, h1 title, download link, file size
                    html = (await r.read()) % (heading, file_name, src, file_size)
    return html