GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}

.PHONY: help clean test run

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make docker:"
	@echo "       Run app with docker and docker-compose"
	@echo ""
	@echo "make dockerdown:"
	@echo "       Remove app from docker with docker-compose down"
	@echo ""

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf

docker:
	@echo "---- Building & Up Container ----"
	@docker-compose -f compose-kafka.yml down
	@docker-compose -f compose-kafka.yml up -d
	@sleep 3
	@docker-compose down
	@docker-compose build	
	@docker-compose up -d
	@sleep 5
	@echo "---- EndPoints ----"
	@echo "---- Producer API - http://127.0.0.1:8080/api-docs/ ----"
	@echo "---- Consumer API - http://127.0.0.1:8084/index ----"

dockerdown:
	@docker-compose down
	@docker-compose -f compose-kafka.yml down