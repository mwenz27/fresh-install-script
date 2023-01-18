"""
Create a script to install items without needing to search for the links ever again.

Windows - Opens Browser and opens tabs
Mac - Opens Browser and opens tabs
Linux - Runs Linux commands


run the code for windows 'python main.py window'
built 18-01-2023
"""

import argparse
import webbrowser
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="specify windows, mac or linux")
args = parser.parse_args()


def freshinstall():
    if args.arg1 == "windows":

        url_list = [
            # Git, a distributed version control system for software development
            "https://git-scm.com/download/win",
            # Software for the Arduino platform
            "https://www.arduino.cc/en/software",
            # Sublime Text, a popular text editor
            "https://www.sublimetext.com/download",
            # Ninite, a website that allows you to easily download multiple popular software programs
            "https://ninite.com/",
            # Zoom, a popular video conferencing software
            # Discord, a popular communication and chat platform for gamers
            # VLC, a media player
            # Spotify, a music streaming service
            # Krita, a digital painting and illustration software
            # Greenshot, a screenshot software
            # Google Earth, a virtual globe and map software
            # Steam, a digital distribution platform for video games
            # 7-zip, a file archiving software
            # Anaconda, a distribution of the Python and R programming languages
            "https://www.anaconda.com/",
            # Telegram, a messaging app
            "https://telegram.org/apps",
            # Signal, a secure messaging app
            "https://signal.org/download/windows/",
            # WhatsApp, a messaging app
            "https://www.whatsapp.com/download",
            # MetaTrader 4, a trading platform for forex and other financial markets
            "https://www.metatrader4.com/en",
            # PyCharm, an integrated development environment (IDE) for Python
            "https://www.jetbrains.com/pycharm/download",
            # Brave, a web browser
            "https://brave.com/download/",
            # Visual Studio Code, a text editor and integrated development environment (IDE)
            "https://code.visualstudio.com/download",
            # Private Internet Access, a virtual private network (VPN) service
            "https://www.privateinternetaccess.com/download/windows-vpn",
            # Slack, a communication and collaboration platform
            "https://slack.com/intl/en-au/download",
            # Exodus, a cryptocurrency wallet
            "https://www.exodus.com/download/",
        ]

        for url in url_list:
            webbrowser.open(url)
            print(url)

    elif args.arg1 == "mac":
        url_list = [
            # Git, a distributed version control system for software development
            "https://git-scm.com/download/win",
            # Visual Studio Code, a text editor and integrated development environment (IDE)
            "https://code.visualstudio.com/download",
            # Anaconda, a distribution of the Python and R programming languages for scientific computing and data
            # science
            "https://www.anaconda.com/products/distribution",
            # PyCharm, an integrated development environment (IDE) for Python
            "https://www.jetbrains.com/pycharm/download",
            # Steam, a digital distribution platform for video games
            "https://store.steampowered.com/about/",
            # Discord, a popular communication and chat platform for gamers
            "https://discord.com/download",
            # VLC, a media player
            "https://www.videolan.org/vlc/index.html",
            # Spotify, a music streaming service
            "https://www.spotify.com/download/",
            # Google Earth, a virtual globe and map software
            "https://www.google.com/earth/versions/download-earth.html",
            # Slack, a communication and collaboration platform
            "https://slack.com/intl/en-au/download",
            # Zoom, a popular video conferencing software
            "https://zoom.us/download",
            # Telegram, a messaging app
            "https://telegram.org/apps",
            # Signal, a secure messaging app
            "https://signal.org/download/windows/",
            # WhatsApp, a messaging app
            "https://www.whatsapp.com/download",
            # MetaTrader 4, a trading platform for forex and other financial markets
            "https://www.metatrader4.com/en",
            # Brave, a web browser
            "https://brave.com/download/",
            # Private Internet Access, a virtual private network (VPN) service
            "https://www.privateinternetaccess.com/download/windows-vpn",
            # Ninite, a website that allows you to easily download multiple popular software programs
            "https://ninite.com/",
            # 7-zip, a file archiving software
            "https://www.7-zip.org/download.html",
            # Exodus, a cryptocurrency wallet
            "https://www.exodus.com/download/"
        ]

        for url in url_list:
            webbrowser.open(url)
            print(url)

    else:

        apps = [
            # Google Chrome, a web browser
            "google-chrome-stable",
            # VLC, a media player
            "vlc",
            # GIMP, an image editing software
            "gimp",
            # Git, a version control system
            "git",
            # htop, a process monitoring tool
            "htop",
            # Sublime Text, a text editor
            "sublime-text",
            # Terminator, a terminal emulator
            "terminator",
            # Spotify, a music streaming service
            "spotify-client",
            # Synaptic Package Manager, a package management tool
            "synaptic",
            # VirtualBox, a virtualization software
            "virtualbox",
            # Slack, a communication and collaboration platform
            "slack-desktop",
            # Dropbox, a file hosting service
            "dropbox",
            # Skype, a communication software
            "skypeforlinux",
            # Steam, a digital distribution platform for video games
            "steam",
            # Atom, a text editor and integrated development environment (IDE)
            "atom",
            # Chromium, an open-source web browser
            "chromium-browser",
            # Inkscape, a vector graphics editor
            "inkscape",
            # Krita, a digital painting and illustration software
            "krita",
            # Thunderbird, an email client
            "thunderbird",
            # KeePassXC, a password manager
            "keepassxc"
        ]

        for app in apps:
            subprocess.run(["sudo", "apt-get", "install", "-y", app], shell=False)
            print(app)


if __name__ == '__main__':
    freshinstall()
