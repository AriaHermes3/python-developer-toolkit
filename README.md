# Python Developer Toolkit 🛠️

A curated collection of production-ready, lightweight utility scripts designed to streamline everyday software engineering workflows.

## Features
- **Benchmarking Tools**: Microsecond-precision timing decorators.
- **Data Transformers**: Clean serialization and nested dictionary navigation.
- **File System Utilities**: Safe atomic file writes and recursive directory walking.

## Installation
```bash
git clone https://github.com/AriaHermes3/python-developer-toolkit.git
cd python-developer-toolkit
pip install -r requirements.txt
```

## Quick Start
```python
from utils.benchmark import timing_decorator

@timing_decorator
def process_data():
    return sum(i * i for i in range(100_000))

process_data()
```

## License
MIT License.
