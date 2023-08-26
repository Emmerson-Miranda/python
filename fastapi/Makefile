# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.PHONY: clean test

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv

test: venv/bin/activate
	pytest --cache-clear -v .

run: test
	python3 -m app.main


