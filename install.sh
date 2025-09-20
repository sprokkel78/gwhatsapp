#!/bin/sh
#
# THIS SCRIPT WILL INSTALL THE gwhatsapp APP SYSTEM WIDE
# THE SCRIPT MUST BE RUN WITH SUDO
#
# It will create a startup shell script named gwhatsapp in /usr/bin,
# the app will be placed in /usr/share/gwhatsapp-sprokkel78
# The .desktop file will be placed in /usr/share/applications/ as com.sprokkel78.gwhatsapp.desktop

mkdir -p /usr/share/gwhatsapp-sprokkel78
cp -r ./* /usr/share/gwhatsapp-sprokkel78/
echo "#!/bin/sh" > /usr/bin/gwhatsapp
echo "cd /usr/share/gwhatsapp-sprokkel78" >> /usr/bin/gwhatsapp
echo "WEBKIT_USE_SINGLE_WEB_PROCESS=1 python3 ./gwhatsapp.py" >> /usr/bin/gwhatsapp
cp ./gwhatsapp.desktop /usr/share/applications/com.sprokkel78.gwhatsapp.desktop
chmod 755 /usr/bin/gwhatsapp
chmod 664 /usr/share/gwhatsapp-sprokkel78/*
