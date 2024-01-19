# 1-install_a_package.pp

# Install flask package with version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
