qa = $(wildcard ./questions_answers/*.csv)

docs/index.html: $(qa) gen_index.py
	python3 ./gen_index.py > docs/index.html

.PHONY: clean
clean:
	rm docs/index.html