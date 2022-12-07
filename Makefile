install:
	sudo pip3 install .

uninstall:
	sudo pip3 uninstall awscli-v1-completer

install_linux:
	sudo cp -f scripts/awscli-v1-completer.service /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl enable awscli-v1-completer
	sudo systemctl start awscli-v1-completer

uninstall_linux:
	sudo systemctl stop awscli-v1-completer
	sudo systemctl daemon-reload
	sudo rm -f /etc/systemd/system/awscli-v1-completer.service


