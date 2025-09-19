![Screenshot](https://github.com/sprokkel78/gwhatsapp/blob/main/screenshots/title.png)

![Screenshot](https://github.com/sprokkel78/gwhatsapp/blob/main/screenshots/gwhatsapp-1.png)

A graphical user interface in PyGTK3 for using Whatsapp on Ubuntu and other Linux distro's. 
It requires Python3.10 and the PyGTK apps. Developed on Fedora 42 and tested on Ubuntu 24.04.

Runs out of the	box after default installation of Fedora or Ubuntu.

Installation on Fedora 42 & Ubuntu 24.04

1. $git clone https://github.com/sprokkel78/gwhatsapp.git
2. $cd gwhatsapp
3. $python3 ./gwhatsapp.py 

For System-Wide Installation, run:
- $sudo ./install.sh

Then start with:
- $gwhatsapp
- or by clicking the application icon.

Added 'install.sh' script for system-wide installation.
- The startup shell script will be /usr/bin/gwhatsapp
- The application is installed in /usr/share/gwhatsapp-sprokkel78
- The .desktop file is placed in /usr/share/applications/com.sprokkel78.gwhatsapp.desktop

Added 'uninstall.sh' script for system-wide uninstallation.
- This will delete /usr/bin/gwhatsapp and /usr/share/gwhatsapp-sprokkel78,
  This will also remove /usr/share/applications/com.sprokkel78.gwhatsapp.desktop

After uninstall it is optional to remove the gwhatsapp-cookies.db file and the .gwhatsapp directory in your homedirectory.

Check https://www.github.com/sprokkel78/gwhatsapp for contributing, development features and pre-releases.
