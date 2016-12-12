clean:
	rm -rf ./venv
develop:
	if ! ls -l ./venv >& /dev/null ; then \
		conda create --yes -p ./venv --file conda-requirements.txt ; \
	else \
		(source activate ./venv && conda install --yes --file conda-requirements.txt) ; \
	fi
	(source activate ./venv && pip install -r pip-requirements.txt)
run:
	(source activate ./venv && python plot.py)
