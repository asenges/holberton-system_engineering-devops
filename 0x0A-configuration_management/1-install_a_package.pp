# install flask using pip3
exec { 'puppet-lint':
  command => '/bin/pip3 install flask -v 2.1.0',
}
