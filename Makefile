.PHONY: build run remove

build:
	docker build -t zeaburextendtria .

run:
	docker rm -f zeaburextendtria || true
	docker run --name  zeaburextendtria zeaburextendtria


remove:
	docker rm -f zeaburextendtria || true

dev:
	poetry run dev

start:
	poetry run start