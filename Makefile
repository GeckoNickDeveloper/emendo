# Makefile for Python library testing
PYTHON ?= python3
PYTEST ?= $(PYTHON) -m pytest
COV ?= $(PYTHON) -m pytest --cov=emendo --cov-report=term-missing

.PHONY: test coverage clean

# Run all tests
test:
	$(PYTEST) tests/

# Run tests with coverage report
coverage:
	$(COV) tests/

# Clean pyc and __pycache__
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete