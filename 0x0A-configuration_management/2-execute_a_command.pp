# kills a process named killmenow
# use exec resource
# command pkill -f killmenow, path /usr/bin:/bin, refreshonly true

exec {'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
