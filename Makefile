PYTHON  := .venv/bin/python
PIP     := .venv/bin/pip
MYPY    := .venv/bin/mypy
BLACK   := .venv/bin/black
RUFF    := .venv/bin/ruff

SRC     := src
REQS    := requirements.txt

.PHONY: venv install run check-requirements typecheck format lint check clean help

# ── environment ──────────────────────────────────────────────────────────────

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install --quiet -r $(REQS) -r requirements-dev.txt

# ── execution ─────────────────────────────────────────────────────────────────

run: install
	$(PYTHON) $(SRC)/app.py

# ── quality checks ────────────────────────────────────────────────────────────

check-requirements: install
	$(PYTHON) scripts/check_imports.py $(SRC) $(REQS)

typecheck: install
	$(MYPY) $(SRC)

lint: install
	$(RUFF) check $(SRC)

# ── formatting (modifies files) ───────────────────────────────────────────────

format: install
	$(BLACK) $(SRC)

# ── composite ─────────────────────────────────────────────────────────────────

check: typecheck check-requirements lint

# ── cleanup ───────────────────────────────────────────────────────────────────

clean:
	rm -rf .venv __pycache__ .mypy_cache .ruff_cache

# ── help ──────────────────────────────────────────────────────────────────────

help:
	@echo "Available targets:"
	@echo "  venv               create .venv with python3 -m venv"
	@echo "  install            install runtime + dev dependencies into .venv"
	@echo "  run                run src/app.py using .venv interpreter"
	@echo "  check-requirements verify all src imports are declared in requirements.txt"
	@echo "  typecheck          static type check via mypy"
	@echo "  lint               code-style check via ruff (read-only)"
	@echo "  format             auto-format src/ via black (modifies files)"
	@echo "  check              run typecheck + check-requirements + lint"
	@echo "  clean              remove .venv and all tool caches"
