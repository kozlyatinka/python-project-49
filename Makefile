install:
	poetry install

brain_games:
	poetry run brain-games

.PHONY: brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
