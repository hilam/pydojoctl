.PHONY: install format lint test sec

run=poetry run

install:
	@poetry install
format:
	${run} blue .
	${run} isort .
lint:
	${run} prospector
	${run} blue --check .
	${run} isort --check .
test:
	${run} pytest -v
sec:
	${run} bandit -r .
	${run} pip-audit
