# use the exec to create a manifest that kills a process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
