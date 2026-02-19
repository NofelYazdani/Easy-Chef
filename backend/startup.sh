A=$(pwd)
B="/venv/bin/activate"
FULL="${A}${B}"

virtualenv -p `which python3` venv
source $FULL
pip install -r requirements.txt
python3 backend/manage.py migrate
