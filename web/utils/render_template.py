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
    base_for_join = STREAM_URL
    if base_for_join and not base_for_join.endswith('/'):
        base_for_join += '/'
    elif not base_for_join:
        if base_for_join == "":
            base_for_join = "/"
    media_content_src = urllib.parse.urljoin(base_for_join, str(message_id))

    audio_formats = ['audio/mpeg', 'audio/mp4', 'audio/x-mpegurl', 'audio/vnd.wav', 'audio/ogg', 'audio/aac']
    video_formats = ['video/mp4', 'video/avi', 'video/ogg', 'video/h264', 'video/h265', 'video/x-matroska', 'video/webm']

    if mime_type.lower() in video_formats:
        async with aiofiles.open('web/template/req.html', mode='r') as r:
            heading = 'Watch {}'.format(file_name)
            html_template = await r.read()
            context = {
                "page_title": heading,
                "h1_title": file_name,
                "video_src": media_content_src,
                "mx_player_intent_url_part": media_content_src,
                "mx_player_title": file_name,
                "vlc_player_url": media_content_src
            }
            html = html_template.format(**context)
    elif mime_type.lower() in audio_formats:
        async with aiofiles.open('web/template/req.html', mode='r') as r:
            heading = 'Listen {}'.format(file_name)
            html_template = await r.read()
            context = {
                "page_title": heading,
                "h1_title": file_name,
                "video_src": media_content_src, # Plyr uses <video> for audio too
                "mx_player_intent_url_part": media_content_src,
                "mx_player_title": file_name,
                "vlc_player_url": media_content_src
            }
            html = html_template.format(**context)
    else:
        async with aiofiles.open('web/template/dl.html', mode='r') as r:
            heading = 'Download {}'.format(file_name)
            file_size_str = "N/A" # Default file size
            try:
                async with aiohttp.ClientSession() as s:
                    async with s.get(media_content_src) as u:
                        if u.status == 200 or u.status == 206:
                             content_length = u.headers.get('Content-Length')
                             if content_length:
                                 file_size_str = get_size(content_length)
            except Exception as e:
                print(f"Error fetching file size for {media_content_src}: {e}")

            html_template = await r.read()
            context = {
                "page_title": heading,
                "file_name_display": file_name,
                "download_url": media_content_src,
                "file_size": file_size_str
            }
            html = html_template.format(**context)
    return html