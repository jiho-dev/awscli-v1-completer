# awscli-v1-completer

awscli-v1-completer is autocompleter server and client for shell.  
aws_completer of aws-cli is too slow to complete the suggestion

awscli-v1-completer server receives the cmdline from shell and give the result back to the client along with the shell

# Install

## prerequisite

install aws-cli v1 on your host and check if `aws` is working well


## setup bash completion

run `$ cp awscli-v1-completer /usr/local/bin/`
add `complete -C /usr/local/bin/awscli-v1-completer aws` to your `.bashrc`

## setup the server

copy `scripts/awscli-v1-completer.service` to `/etc/systemd/system/`
run  `$ sudo chmod 664 /etc/systemd/system/awscli-v1-completer.service.service`
run  `$ sudo systemctl daemon-reload`
run  `$ sudo systemctl start awscli-v1-completer`

run  `$ sudo systemctl stop awscli-v1-completer`
run  `$ sudo systemctl restart awscli-v1-completer`
run  `$ systemctl status awscli-v1-completer`

## check if `aws ec2 [TAB]` is working well and feel it



