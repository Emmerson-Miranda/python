# https://www.gnu.org/software/make/manual/html_node/One-Shell.html
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.ONESHELL:
.PHONY: clean lint test run

VENV = ./venv
BIN=$(VENV)/bin

venv/bin/activate: requirements.txt
	python3 -m venv venv
	$(BIN)/pip3 install -r requirements.txt

clean:
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
	find . -type d -name .pytest_cache -delete

lint: venv/bin/activate
	$(BIN)/flake8 ./app/

test: lint
	$(BIN)/pytest --cache-clear -v .

run: test
	$(BIN)/python3 -m app.main


