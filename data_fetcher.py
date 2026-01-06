
# Configuration

CSV_PATH = "train_cdc.csv"
OUT_DIR = Path("/content/drive/MyDrive/satell_images_cdc_zoom15/")
OUT_DIR.mkdir(exist_ok=True)

LAT_COL = "lat"
LON_COL = "long"
ID_COL  = "id"  # set to None if not present

ZOOM = 15
IMG_SIZE = 256
SLEEP_TIME = 0.05

assert MAPBOX_TOKEN.startswith("pk."), "Invalid Mapbox public token"

# Load data
df = pd.read_csv(CSV_PATH)
print(f"Loaded {len(df)} rows")

# Helper: fetch one image

def fetch_image(lat, lon, save_path):
    url = (
        f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
        f"{lon},{lat},{ZOOM}/"
        f"{IMG_SIZE}x{IMG_SIZE}"
        f"?access_token={MAPBOX_TOKEN}"
    )

    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(r.content)
        return True
    else:
        return False


# Batch fetch

success, failed = 0, 0

for idx, row in tqdm(df.iterrows(), total=len(df)):
    lat, lon = row[LAT_COL], row[LON_COL]

    if ID_COL and ID_COL in df.columns:
        fname = f"{row[ID_COL]}.png"
    else:
        fname = f"{idx}.png"

    save_path = OUT_DIR / fname

    # Skip if already exists (cache)
    if save_path.exists():
        continue

    ok = fetch_image(lat, lon, save_path)
    if ok:
        success += 1
    else:
        failed += 1

    time.sleep(SLEEP_TIME)

print(f"Done. Success: {success}, Failed: {failed}")