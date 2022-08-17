# Install nginx listening on port 80

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
