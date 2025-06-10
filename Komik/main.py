import requests

# === 1. Generate cerita dari prompt ===
def generate_story(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",  # Olama Mistral API
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json()['response']

# === 2. Pecah cerita jadi 3 panel ===
def split_story_to_panels(story, num_panels=3):
    sentences = story.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    panels = sentences[:num_panels]
    return panels

# === 3. Generate gambar pakai Stable Diffusion lokal ===
def generate_image(prompt, panel_id):
    response = requests.post(
        "http://127.0.0.1:7860/sdapi/v1/txt2img",  # Ganti sesuai SD kamu
        json={
            "prompt": prompt,
            "steps": 20,
            "cfg_scale": 7.5,
            "width": 512,
            "height": 512
        }
    )
    result = response.json()
    image_data = result['images'][0]

    import base64
    image_bytes = base64.b64decode(image_data.split(",", 1)[-1])
    with open(f"panel_{panel_id}.png", "wb") as f:
        f.write(image_bytes)

# === 4. Simpan jadi HTML ===
def save_as_html(panels):
    with open("comic.html", "w", encoding="utf-8") as f:
        f.write("<html><body>\n")
        for i, text in enumerate(panels, 1):
            f.write(f"<h2>Panel {i}</h2>\n")
            f.write(f"<img src='panel_{i}.png' width='300'><br>\n")
            f.write(f"<p>{text}</p>\n")
        f.write("</body></html>")

# === Jalankan alur ===
if __name__ == "__main__":
    prompt = "Buatkan 3 panel cerita komik tentang kucing ninja yang melawan tikus mafia."
    story = generate_story(prompt)

    print("\n=== Hasil Cerita Komik ===")
    print(story)

    panels = split_story_to_panels(story)

    for i, panel in enumerate(panels, 1):
        print(f"\n[+] Panel {i}: {panel}")
        generate_image(panel, i)

    save_as_html(panels)
    print("\n✅ Komik selesai! Lihat file: comic.html")
