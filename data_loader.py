import json

def load_conversations(filepath):
    """Load ChatGPT conversations JSON."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

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
                if isinstance(first_part, str):
                    all_text.append(first_part)
                else:
                    all_text.append(str(first_part))
        title_text_map[title] = " ".join(all_text)
    return title_text_map
