#! /bin/sh
# /etc/init.d/noip 

### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       A simple script from www.stuffaboutcode.comwhich will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting noip"
    # run application you want to start
    cd /
    cd home/pi/PiMov
    sudo python PiMov.py
    cd /
    ;;
  stop)
    echo "Stopping noip"
    # kill application you want to stop
    killall python
    ;;
  *)
    echo "Usage: /etc/init.d/launcher {start|stop}"
    exit 1
    ;;
esac

exit 0