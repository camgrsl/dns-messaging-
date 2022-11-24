COMPOSE = docker-compose

.PHONY: up
up:
	@$(COMPOSE) up --build

.PHONY: mock-data
mock-data:
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM
	docker exec client /usr/local/bin/python client.py $$RANDOM

.PHONY: test-connection
test-connection:
	docker exec client /usr/local/bin/python test_connection.py