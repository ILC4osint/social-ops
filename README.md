# social-ops

## Installation
(create virtual environment)
pip install -r requirements.txt
pip install -e .
## Test
cd social-ops
pytest
mypy socint/
# Run
## As a module
python -m socint --query "hamas" --source ventric
## As CLI
```socint --query "hamas" --source ventric```
