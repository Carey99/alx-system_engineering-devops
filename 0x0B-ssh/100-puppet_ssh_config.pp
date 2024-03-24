file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0644',
  content => template('module_name/ssh_config.erb'),
  notify  => Service['ssh'],
}

service { 'ssh':
  ensure  => running,
  enable  => true,
  require => File['/etc/ssh/ssh_config'],
}
