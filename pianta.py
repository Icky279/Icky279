import requests
import base64

API_KEY = 'LA_API_KEY'
API_URL = "https://api.plant.id/v2/identify"

def get_image_data(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def identify(image_file):
    img_b64 = get_image_data(image_file)

    data = {
        "api_key": API_KEY,
        "images": [img_b64],
        "modifiers": ["crops_fast", "similar_images"],
        "plant_language": "it",
        "plant_details": ["common_names", "url", "wiki_description"]
    }

    r = requests.post(API_URL, json=data)

    if r.ok:
        out = r.json()
        plants = out.get("suggestions", [])
        if not plants:
            print("Nessun risultato.")
            return
        for p in plants[:2]:
            sci_name = p.get("plant_name", "N/D")
            score = p.get("probability", 0)
            aliases = p.get("plant_details", {}).get("common_names", [])
            print(f"\n🌱Nome scientifico? {sci_name}")
            print(f"Quanto è rara?: {int(score * 100)}%")
            if aliases:
                print("Altri nomi:", ", ".join(aliases))
    else:
        print("Errore:", r.status_code)
        print(r.text)