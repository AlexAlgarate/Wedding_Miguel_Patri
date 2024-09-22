python -m pip install --upgrade pip
pip install -r requirements.txt
rm -fr public
isort wedding_miguel_patri/
black wedding_miguel_patri/
ruff check wedding_miguel_patri/ --fix
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip