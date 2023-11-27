import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch
import numpy as np

from config import YOUTUBE_IMG_URL

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}_v4.png"): 
        return f"cache/{videoid}_v4.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/{videoid}_4.png", mode="wb" ) 
                    await f.write(await resp.read()) 
                    await f.close()

        return f"cache/{videoid}_4.png"
    except Exception:
        return YOUTUBE_IMG_URL