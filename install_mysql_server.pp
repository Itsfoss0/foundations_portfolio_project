#!/usr/bin/env puppet

package { 'mysql-server':
  ensure => installed,
}

package { 'mysql-client':
  ensure => installed,
}

service { 'mysql':
  ensure  => running,
  enable  => true,
  require => Package['mysql-server'],
}

exec { 'mysql_secure_installation':
  command     => 'mysql_secure_installation',
  path        => '/usr/bin',
  creates     => '/etc/mysql/my.cnf',
  refreshonly => true,
  require     => Package['mysql-server'],
}
