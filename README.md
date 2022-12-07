# awscli-v1-completer

awscli-v1-completer is autocompleter server and client for shell.  
aws_completer of aws-cli is too slow to complete the suggestion

awscli-v1-completer server receives the cmdline from shell and give the result back to the client along with the shell

# Install

## prerequisite

install aws-cli v1 on your host and check if `aws` is working well 

## setup

### steps

```   
# for the package
$ make install
$ make uninstall

# for the linux service
$ make install_linux
$ make uninstall_linux

```

### setup bash completion

add `complete -C /usr/local/bin/awscli-v1-completer aws` to your `.bashrc`  

### use it

check if `aws ec2 [TAB]` is working well and feel it 



