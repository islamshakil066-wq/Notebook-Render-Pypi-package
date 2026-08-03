from NotebookVideoRenderer.custom_exception import InvalidURLException
from NotebookVideoRenderer.logger import logger
import re
from IPython.display import HTML, display


def render_youtube_video(url: str, width: int = 800, height: int = 315):
    try:
        regex = (
            
            r"(?:https?://)?"
            r"(?:www\.|m\.)?"
            r"(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)"
            r"([A-Za-z0-9_-]{11})"
        )

        match = re.search(regex, url)
        
        
        if not match:
            raise InvalidURLException(f"Invalid YouTube URL : {url}.")
        
        video_id = match.group(1)
        embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}" 
        
        iframe = f"""
        <iframe width="{width}" height="{height}" 
        src="{embed_url}" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen>
        </iframe>
        """
        display(HTML(iframe))
        logger.info(f"** youtube video rendered Successfully ** ")
        return "success"
            
    
    except Exception as e:
        raise e    
        
    