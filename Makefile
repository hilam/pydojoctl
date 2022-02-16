.PHONY: install format lint test sec

run=poetry run

install:
	@poetry install
format:
	${run} blue src/
	${run} isort src/
lint:
	${run} prospector
	${run} blue --check src/
	${run} isort --check src/
test:
	${run} pytest -v
sec:
	${run} bandit -r src/
	${run} pip-audit
