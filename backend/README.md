# Virtual envariment

Create virtual envariment:

```bash
virtualenv .venv -p python
python -m venv venv
```

Activate virtual envariment:

```bash
source .venv/bin/activate
source venv/bin/activate
```

Activate virtual envariment:

```bash
deactivate
```

Save package list to text file:

```bash
pip freeze > requirements.txt
```

Save packages to folder:

```bash
pip wheel --wheel-dir=./wheels -r requirements.txt
```

Install packages:

```bash
pip install -r requirements.txt
```

or

```bash
pip install --no-index --find-links=./wheels -r requirements.txt
```
