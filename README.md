# MiniMenu for PiHole

This is a simple program that simply turn PiHole on or off and provide its status.

The ip address and web password are kept clear in the data.txt file, this data are saved every time you enable or disable piholes through this program.

You can get the web password by running this command on the machine where pihole run:

    sudo cat /etc/pihole/setupVars.conf | grep PASSWORD

I'm not affiliated with PiHole in any way
