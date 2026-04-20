dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

test:
	docker compose -f docker-compose.test.yml up --build --abort-on-container-exit --exit-code-from api