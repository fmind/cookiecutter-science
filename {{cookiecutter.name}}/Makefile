venv:
	python{{cookiecutter.python}} -m venv venv --clear
	venv/bin/pip install -r requirements.txt

work: venv
	venv/bin/jupyter lab
