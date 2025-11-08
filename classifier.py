def classify_site(site):
    site = site.lower()

    study_keywords = ["study", "learn", "tutorial", "course", "wikipedia", "notes"]
    block_keywords = ["instagram", "reels", "game", "tiktok", "netflix", "primevideo"]

    if any(k in site for k in study_keywords):
        return "ALLOW"

    if any(k in site for k in block_keywords):
        return "BLOCK"

    return "UNKNOWN"
