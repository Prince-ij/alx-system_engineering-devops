# Install flask 2.1.0

exec { 'flask':
  command => 'sudo apt-get install -y python3-flask=2.1.0',
  path    => '/usr/bin:/bin'
}
