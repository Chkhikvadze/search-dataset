from huggingface_hub import HfApi
import json
from collections import Counter
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize API with token
api = HfApi(token=os.getenv('HUGGINGFACE_TOKEN'))

HF_DATASET_URL = "junzhang1207/search-dataset"

files_to_upload = {
    'HF_README.md': 'README.md',
    '.gitignore': '.gitignore',
    'data.jsonl': 'data.jsonl',
    'data-samples.json': 'data-samples.json',
    'dataset_info.json': 'dataset_info.json'
}

for local_file, repo_path in files_to_upload.items():
    print(f"Uploading {local_file}...")
    api.upload_file(
        path_or_fileobj=local_file,
        path_in_repo=repo_path,
        repo_id=HF_DATASET_URL,
        repo_type="dataset"
    )

