all:
	uv run pytest

gold:
	./test_golden.sh

format:
	uv run ruff format .
