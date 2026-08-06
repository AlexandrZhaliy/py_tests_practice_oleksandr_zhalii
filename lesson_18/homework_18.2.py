import requests
from pathlib import Path
current_dir = Path(__file__).parent
image_path = current_dir / "mars_photo1.jpg"

from urllib.parse import quote
BASE_URL = "http://127.0.0.1:8080"

# ================= POST =================
with open(image_path, "rb") as image:
    files = {
        "image": image
    }
    response = requests.post(f"{BASE_URL}/upload", files=files)

response.raise_for_status()
image_url = response.json()["image_url"]
print("POST:", image_url)

# ================= GET =================
filename = image_url.split("/")[-1]
filename = quote(filename)
response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={"Content-Type": "text"}
)
response.raise_for_status()
print("GET:", response.json())

# ================= DELETE =================
response = requests.delete(f"{BASE_URL}/delete/{filename}")
response.raise_for_status()
print("DELETE:", response.json())