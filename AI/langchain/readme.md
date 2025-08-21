# Setup

Install Python 3.12.2

```bash
python3 --version
python3 -m venv venv
source ./venv/bin/activate
```

Install requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

OpenAI Key (in my case is inside a text file)
```bash
export OPENAI_API_KEY=$(cat $HOME/Downloads/openai-api-assistant-model.txt)
```

Run Jupyter notebook
https://docs.jupyter.org/en/latest/running.html

```bash
jupyter notebook
```