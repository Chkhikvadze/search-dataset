This project helps upload a search dataset to Hugging Face's dataset repository. The uploaded dataset can be found at [junzhang1207/search-dataset](https://huggingface.co/datasets/junzhang1207/search-dataset).

## Setup

### 1. Environment Setup

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

### 2. Hugging Face Access Token

1. Create an account on [Hugging Face](https://huggingface.co/)
2. Go to your [Settings > Access Tokens](https://huggingface.co/settings/tokens)
3. Create a new token with write permissions
4. Save your token in a `.env` file:

```bash
# .env
HUGGINGFACE_TOKEN=your_token_here
```

### 3. Running the Upload Script

Execute the upload script:
```bash
python upload_dataset.py
```

## Dataset Structure

The dataset contains question-answer pairs organized with the following fields:
- `id`: Unique identifier
- `question`: Query text
- `expected_answer`: Correct answer
- `category`: Topic category
- `area`: Broader classification (News/Knowledge)

## Categories

The dataset covers various domains including:
- Entertainment
- Sports
- Technology
- General News
- Finance
- Architecture
- Arts
- Astronomy
- Auto (Automotive)
- E-sports
- Fashion
