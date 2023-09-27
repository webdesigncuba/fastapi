# Update poetry.lock

install:
	@poetry lock --no-update
	@poetry install

update:
	@poetry update

shell:
	@poetry shell

exitshell:
	exit

server:
	@poetry run uvicorn app.main --port 8000 --workers 3 --reload 