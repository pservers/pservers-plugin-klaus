plugin=klaus
prefix=/usr

all:

clean:
        fixme

install:
        install -d -m 0755 "$(DESTDIR)/$(prefix)/lib64/pservers/plugins.d"
        cp -r $(plugin) "$(DESTDIR)/$(prefix)/lib64/pservers/plugins.d"
        find "$(DESTDIR)/$(prefix)/lib64/pservers/plugins.d/$(plugin)" -type f | xargs chmod 644
        find "$(DESTDIR)/$(prefix)/lib64/pservers/plugins.d/$(plugin)" -type d | xargs chmod 755
        find "$(DESTDIR)/$(prefix)/lib64/pservers/plugins.d/$(plugin)" -name "*.py" | xargs chmod 755

uninstall:
        rm -rf "$(DESTDIR)/$(prefix)/lib64/pservers/plugins.d/$(plugin)"

.PHONY: all clean install uninstall
