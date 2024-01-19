# This creates a file in /tmp/school
# The following attributes must be in place
# path  /tmp/school, perm 0744, owner:group www-data, content I love Puppet

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet'
}
