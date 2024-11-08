# type: ignore
import re
import yt_dlp

# Video Platform URL Patterns
VIDEO_URL_PATTERNS = [r"(youtube\.com|youtu\.be)", r"vimeo\.com"]

# Check if a URL points to a video based on patterns
def is_video_url(url):
    for pattern in VIDEO_URL_PATTERNS:
        if re.search(pattern, url):
            return True
    return False

# Extract video metadata using yt-dlp, including caption availability
def extract_video_metadata(url):
    ydl_opts = {'skip_download': True, 'quiet': True}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        title = info_dict.get('title', 'N/A')
        description = info_dict.get('description', 'N/A')
        
        # Get subtitles (captions), if available, in the 'en' language
        subtitles = info_dict.get('subtitles', {}).get('en', [])
        
        has_captions = bool(subtitles)  # Check if captions are present
        
        return {
            'title': title,
            'description': description,
            'subtitles': subtitles,   # List of subtitle dictionaries (if available)
            'has_captions': has_captions  # Boolean flag for caption detection
        }
    
# Process and format subtitles into a string
def process_subtitles(subtitles):
    subtitle_text = ""
    for sub in subtitles:
        subtitle_text += sub.get('text', '') + "\n"
    return subtitle_text