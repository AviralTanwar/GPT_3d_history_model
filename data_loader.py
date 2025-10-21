# data_loader.py
import json
import os
import io
from typing import Union

def load_conversations(src: Union[str, os.PathLike, io.IOBase]):
    """Load ChatGPT conversations from a path or an in-memory uploaded file."""
    # Case 1: a string/path-like → open and json.load
    if isinstance(src, (str, os.PathLike)):
        with open(src, "r", encoding="utf-8") as f:
            return json.load(f)

    # Case 2: Stream/UploadedFile → read bytes, decode, json.loads
    # Streamlit's UploadedFile has .getvalue(); generic file-like has .read()
    if hasattr(src, "getvalue"):
        data = src.getvalue()                     # bytes
    else:
        data = src.read()                         # bytes or str

    if isinstance(data, bytes):
        data = data.decode("utf-8")               # to str

    return json.loads(data)

def get_title_text_map(conversations):
    """Extract a mapping of title -> concatenated chat text."""
    title_text_map = {}
    for convo in conversations:
        title = convo.get("title", "Untitled")
        messages = convo.get("mapping", {}).values()
        all_text = []
        for msg in messages:
            message = msg.get("message")
            if not message:
                continue
            parts = message.get("content", {}).get("parts", [])
            if parts:
                first_part = parts[0]
                all_text.append(first_part if isinstance(first_part, str) else str(first_part))
        title_text_map[title] = " ".join(all_text)
    return title_text_map
