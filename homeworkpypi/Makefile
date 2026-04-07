.PHONY: create-structure test install build upload-testpypi clean

create-structure:
	mkdir -p src docs tests
	touch docs/DOMAIN.md
	touch src/.gitkeep
	touch tests/.gitkeep
	touch requirements.txt setup.py README.py

test:
	python tests/test_calculator.py

test-pytest:
	pytest

install:
	pip install -e .

build: clean
	python -m build

upload-testpypi: build
	python -m twine upload --repository testpypi dist/*

clean:
	rm -rf build/ dist/ *.egg-info/
