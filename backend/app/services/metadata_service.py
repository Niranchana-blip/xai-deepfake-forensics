import subprocess
import json


def extract_metadata(file_path):

    try:

        result = subprocess.run(
            ["exiftool", "-j", file_path],
            capture_output=True,
            text=True
        )

        metadata = json.loads(result.stdout)

        return metadata[0]

    except Exception as e:

        return {
            "error": str(e)
        }
    