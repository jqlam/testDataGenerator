from pathlib import Path
import hashlib
from datetime import datetime
import pandas as pd

def generateManifest(path: str):
    now = datetime.now()
    upload_date = now.strftime("%Y-%m-%d %H:%M:%S")

    if (path[-1] == "/"):
        path = path[:-1]
    # Create a path object
    dir_path = Path(path)

    manifestData = {"ESS File Path": [],
                    "Display Name": [],
                    "size": [],
                    "Date of Upload": [],
                    "sha256": []}

    # Recursive traversal using rglob
    for item in dir_path.rglob("*"):
        if item.is_file():
            file_size = item.stat().st_size
            with open(item, "rb") as f:
                digest = hashlib.file_digest(f, "sha256")
                file_sha256 = digest.hexdigest()
            manifestData.get("ESS File Path").append(item)
            manifestData.get("Display Name").append(item.name)
            manifestData.get("size").append(file_size)
            manifestData.get("Date of Upload").append(upload_date)
            manifestData.get("sha256").append(file_sha256)
        
        # elif item.is_dir():
        #     print(f"Folder: {item}")
    df = pd.DataFrame(manifestData)
    pathName = path + (f"/Manifest_{dir_path.name}.xlsx")
    df.to_excel(pathName, index=False)
    print("Manifest File Generated")