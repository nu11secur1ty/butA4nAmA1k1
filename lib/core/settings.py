#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022 

import os
import sys
import string

from lib.utils.file import FileUtils

# Version format: <major version>.<minor version>.<revision>[.<month>]
VERSION = "1.4"

BANNER = f"""
 ██▓ ███▄    █   ██████ ▓█████  ▄████▄  ▄▄▄█████▓
▓██▒ ██ ▀█   █ ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░
░██░▓██▒  ▐▌██▒  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ 
░██░▒██░   ▓██░▒██████▒▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ 
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░ ░ ░  ░  ░  ▒       ░    
 ▒ ░   ░   ░ ░ ░  ░  ░     ░   ░          ░      
 ░           ░       ░     ░  ░░ ░               
                               ░                                    
   .               .                                   .         
  | o             |           o            ,- o       |         
,-| . ;-. ,-. ,-. |-  ,-. ;-. . ,-. ,-.    |  . ;-. ,-| ,-. ;-. 
| | | |   |-' |   |   | | |   | |-' `-.    |- | | | | | |-' |   
`-' ' '   `-' `-' `-' `-' '   ' `-' `-'    |  ' ' ' `-' `-' '   
                                          -'                    v{VERSION}                      
"""

SCRIPT_PATH = FileUtils.parent(__file__, 3)

IS_WINDOWS = sys.platform in ("win32", "msys")

DEFAULT_ENCODING = "utf-8"

NEW_LINE = os.linesep

INVALID_CHARS_FOR_WINDOWS_FILENAME = ('"', "*", "<", ">", "?", "\\", "|", "/", ":")

INVALID_FILENAME_CHAR_REPLACEMENT = "_"

OUTPUT_FORMATS = ("simple", "plain", "json", "xml", "md", "csv", "html", "sqlite")

COMMON_EXTENSIONS = ("php", "jsp", "asp", "aspx", "do", "action", "cgi", "html", "htm", "js", "tar.gz")

MEDIA_EXTENSIONS = ("webm", "mkv", "avi", "ts", "mov", "qt", "amv", "mp4", "m4p", "m4v", "mp3", "swf", "mpg", "mpeg", "jpg", "jpeg", "pjpeg", "png", "woff", "svg", "webp", "bmp", "pdf", "wav", "vtt")

EXCLUDE_OVERWRITE_EXTENSIONS = MEDIA_EXTENSIONS + ("axd", "cache", "coffee", "conf", "config", "css", "dll", "lock", "log", "key", "pub", "properties", "ini", "jar", "js", "json", "toml", "txt", "xml", "yaml", "yml")

CRAWL_ATTRIBUTES = ("action", "cite", "data", "formaction", "href", "longdesc", "poster", "src", "srcset", "xmlns")

CRAWL_TAGS = ("a", "area", "base", "blockquote", "button", "embed", "form", "frame", "frameset", "html", "iframe", "input", "ins", "noframes", "object", "q", "script", "source")

AUTHENTICATION_TYPES = ("basic", "digest", "bearer", "ntlm", "jwt", "oauth2")

PROXY_SCHEMES = ("http://", "https://", "socks5://", "socks5h://", "socks4://", "socks4a://")

STANDARD_PORTS = {"http": 80, "https": 443}

INSECURE_CSV_CHARS = ("+", "-", "=", "@")

DEFAULT_TEST_PREFIXES = (".",)

DEFAULT_TEST_SUFFIXES = ("/",)

DEFAULT_TOR_PROXIES = ("socks5://127.0.0.1:9050", "socks5://127.0.0.1:9150")

DEFAULT_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

DEFAULT_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "*",
    "Keep-Alive": "timeout=15, max=1000",
    "Cache-Control": "max-age=0",
}

DEFAULT_SESSION_FILE = "session.pickle"

REFLECTED_PATH_MARKER = "__REFLECTED_PATH__"

WILDCARD_TEST_POINT_MARKER = "__WILDCARD_POINT__"

EXTENSION_TAG = "%ext%"

EXTENSION_RECOGNITION_REGEX = r"\w+([.][a-zA-Z0-9]{2,5}){1,3}~?$"

QUERY_STRING_REGEX = r"^(\&?([^=& ]+)\=([^=& ]+)?){1,200}$"

READ_RESPONSE_ERROR_REGEX = r"(ChunkedEncodingError|StreamConsumedError|UnrewindableBodyError)"

URI_REGEX = r"^[a-z]{2,}:"

ROBOTS_TXT_REGEX = r"(?:Allow|Disallow): /(.*)"

UNKNOWN = "unknown"

TMP_PATH = "/tmp/dirsearch"

DUMMY_DOMAIN = "example.com"

DUMMY_URL = "https://example.com/"

DUMMY_WORD = "dummyasdf"

SOCKET_TIMEOUT = 6

RATE_UPDATE_DELAY = 0.15

MAX_MATCH_RATIO = 0.98

ITER_CHUNK_SIZE = 1024 * 1024

MAX_RESPONSE_SIZE = 80 * 1024 * 1024

TEST_PATH_LENGTH = 6

MAX_CONSECUTIVE_REQUEST_ERRORS = 75

PAUSING_WAIT_TIMEOUT = 7

URL_SAFE_CHARS = string.punctuation

TEXT_CHARS = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F})
