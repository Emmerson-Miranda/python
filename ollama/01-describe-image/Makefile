# https://www.gnu.org/software/make/manual/html_node/One-Shell.html
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.ONESHELL:
.PHONY: clean lint test run venv

BIN=./venv/bin

venv: requirements.txt
	python3 -m venv ./venv
	$(BIN)/pip3 install -r requirements.txt

clean:
	rm -rf venv
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf generated

lint: venv
	$(BIN)/flake8 ./app/

test: lint
	rm -rf generated

run: test
	$(BIN)/python3 -m app.main
