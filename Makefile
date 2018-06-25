VE ?= ./ve
REQUIREMENTS ?= requirements.txt
PIP ?= $(VE)/bin/pip
WHEEL_VERSION ?= 0.31.0

create:
	rm -rf $(VE)
	python3 -m venv $(VE)
	$(PIP) install wheel==$(WHEEL_VERSION)
	$(PIP) install --use-wheel --requirement $(REQUIREMENTS)
	
clean:
	rm -rf ve
	
	