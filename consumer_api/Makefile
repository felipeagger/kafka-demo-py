GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}

.PHONY: help clean test run

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make setup"
	@echo "       Install dependencies"
	@echo "       set virtualenv on this path"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with pytest(necessary kafka ON)"
	@echo ""
	@echo "make rundev:"
	@echo "       Run the web application(necessary kafka ON)"
	@echo ""

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf

setup:
	@echo "---- Setting Enviroment ----"
	@virtualenv env
	@. env/bin/activate
	@echo "---- Installing Python dependencies ----"
	@pip3 install -r requirements.txt --upgrade

test:
	@pytest --verbose --disable-pytest-warnings --color=yes tests/

rundev:
	@gunicorn -c ./gunicorn.py app:app