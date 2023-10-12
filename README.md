# social-ops
![image](https://github.com/ILC4osint/social-ops/assets/89794666/57b62bd8-957c-4d41-bffa-a14e26a8ce70)

## Installation
(create virtual environment)
pip install -r requirements.txt
pip install -e .
## Test
cd social-ops
pytest
mypy socint/
## Pylint
./run_pylint.sh
# Run
## As a module
python -m socint --query "hamas" --source ventric
## As CLI
```socint --query "hamas" --source ventric```
