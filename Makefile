plugin=klaus
prefix=/usr

all:

clean:
	fixme

install:
	install -d -m 0755 "$(DESTDIR)/$(prefix)/lib64/pservers/plugins"
	cp -r $(plugin) "$(DESTDIR)/$(prefix)/lib64/pservers/plugins"
	find "$(DESTDIR)/$(prefix)/lib64/pservers/plugins/$(plugin)" -type f | xargs chmod 644
	find "$(DESTDIR)/$(prefix)/lib64/pservers/plugins/$(plugin)" -type d | xargs chmod 755

uninstall:
	rm -rf "$(DESTDIR)/$(prefix)/lib64/pservers/plugins/$(plugin)"

.PHONY: all clean install uninstall
