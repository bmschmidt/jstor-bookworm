

foldername:=DFR-59_2015-03-04T16-57-43.322923



input.txt:
	find $(foldername) -name "*.json" | xargs python parseJSON.py


db:
	git clone git@github.com:Bookworm-Project/BookwormDB $@
	cd db; make


topic_model:
	mkdir -p db/extensions
	git clone git@github.com:bmschmidt/Bookworm-Mallet db/extensions/Bookworm-Mallet
	cd db/extensions/Bookworm-Mallet; make

