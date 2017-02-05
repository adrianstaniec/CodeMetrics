# Macro for printing a colored message to stdout
print_msg = @printf "\n\033[1;34m***%s***\033[0m\n" "$(1)"

all: lint test

lint: pep8 pylint flake8

pep8:
	$(call print_msg, Running pep8... )
	pep8 codemetrics

pylint:
	$(call print_msg, Running pylint... )
	pylint codemetrics 

flake8:
	$(call print_msg, Running flake8... )
	flake8 codemetrics

test:
	$(call print_msg, Running tests... )
	py.test --cov-report= --cov=codemetrics tests

