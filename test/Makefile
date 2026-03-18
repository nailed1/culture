.PHONY: create-structure test-pytest install-dep install test-pytest test

create-structure:
	mkdir -p src docs tests
	touch docs/DOMAIN.md
	touch src/.gitkeep
	touch tests/.gitkeep
	touch requirements.txt setup.py README.py

deps:
	pip install --upgrade pipreqs
	pipreqs . --force --savepath requirements.txt

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	pytest

test: deps install-dep install test-pytest