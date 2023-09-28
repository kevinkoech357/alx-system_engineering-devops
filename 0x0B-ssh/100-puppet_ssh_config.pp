# Define a custom SSH client configuration

include stdlib

file_line {'turn off password authentication':
  path      => '/etc/ssh/ssh_config',
  line      => 'PasswordAuthentication no',
  replace   => true
}

file_line { 'Identity file':
  path      => '/etc/ssh/ssh_config',
  line      => 'IdentityFile ~/.ssh/school',
  replace   => true
}

