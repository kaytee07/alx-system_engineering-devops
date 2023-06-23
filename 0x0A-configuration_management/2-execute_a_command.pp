# use the exec to create a manifest that kills a process killmenow

exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/bin',
  logoutput => true,
}
