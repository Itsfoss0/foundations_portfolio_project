#!/usr/bin/env puppet

package { 'mysql-server':
  ensure => installed,
}

package { 'mysql-client':
  ensure => installed,
}

package {'python3:
  ensure => installed,
}

package {'python3-pip':
  ensure => installed,
  require => Package['python3'],
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

exec { 'install_python_packages':
  command     => 'pip install -r ./requirements.txt',
  path        => '/usr/local/bin:/usr/bin:/bin',
  refreshonly => true,
}
