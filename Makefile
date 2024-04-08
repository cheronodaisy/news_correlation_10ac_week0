init:
	python3 -m pip install --user pylint black poetry pipenv bandit mypy flake8


install:
	poetry install

lint:
	poetry run pylint --rcfile=.pylintrc src
	poetry run black --check src
	poetry run bandit -r src
	poetry run mypy src
	poetry run flake8 src


run:
	poetry run python3 main.py

test:
	poetry run pytest tests
