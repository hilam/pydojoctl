.PHONY: install format lint test sec

run=poetry run

install:
	@poetry install
format:
	${run} blue pydojoctl/
lint:
	${run} blue --check pydojoctl/
	${run} prospector --no-autodetect
test:
	${run} pytest -v
sec:
	${run} bandit -r pydojoctl/
	${run} pip-audit
