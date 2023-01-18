"""
Create a script to install items without needing to search for the links ever again.

run the code for windows 'python main.py windows'
built on 18-01-2023
"""

import argparse
import webbrowser
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="specify windows, mac, linux or chrome")
args = parser.parse_args()


def freshinstall():
    """Windows - Opens Browser and opens tabs
    Mac - Opens Browser and opens tabs
    Linux - Runs Linux commands
    :return:
    """
    if args.arg1 == "windows":

        url_list = [
            # flux
            "https://justgetflux.com/",
            # Git, a distributed version control system for software development
            "https://git-scm.com/download/win",
            # Git GUI
            "https://www.sourcetreeapp.com/",
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
            # Malyware bytes, protection for PC
            "https://www.malwarebytes.com/mwb-download/thankyou",
            # Trello, board list
            "https://apps.microsoft.com/store/detail/trello/9NBLGGH4XXVW?hl=en-us&gl=us&rtc=1",
            # Plex, media server
            "https://www.plex.tv/media-server-downloads/?lang=en-au#plex-app",
            # Rescue Time,
            "https://www.rescuetime.com/download",
            # Postman, a tool for API development and testing
            "https://www.postman.com/downloads/",
        ]

        for url in url_list:
            webbrowser.open(url)
            print(url)
            if "https://ninite.com/":
                print(""" Select Items
                            Zoom, a popular video conferencing software
            Discord, a popular communication and chat platform for gamers
            VLC, a media player
            Spotify, a music streaming service
            Krita, a digital painting and illustration software
            Greenshot, a screenshot software
            Google Earth, a virtual globe and map software
            Steam, a digital distribution platform for video games
            7-zip, a file archiving software
            Anaconda, a distribution of the Python and R programming languages
                """
                      )


    elif args.arg1 == "mac":
        url_list = [
            # flux
            "https://justgetflux.com/",
            # Sublime Text, a popular text editor
            "https://www.sublimetext.com/download",
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
            "https://www.exodus.com/download/",
            # Plex, media server
            "https://www.plex.tv/media-server-downloads/?lang=en-au#plex-app",
            # Rescue Time, time management
            "https://www.rescuetime.com/download",
            # Postman, a tool for API development and testing
            "https://www.postman.com/downloads/",
        ]

        for url in url_list:
            webbrowser.open(url)
            print(url)

    elif args.arg1 == "linux":

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

    elif args.arg1 == "chrome":
        extensions = [
            # AdBlock Plus, an ad blocker
            ("AdBlock Plus", "https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb"),
            # Grammarly, a grammar and spelling checker
            ("Grammarly",
             "https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen"),
            # LastPass, a password manager
            ("LastPass",
             "https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd"),
            # uBlock Origin, an ad blocker
            ("uBlock Origin",
             "https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm"),
            # Evernote Web Clipper, a note-taking and web-clipping tool
            ("Evernote Web Clipper", "https://chrome.google.com/webstore/detail"),
            # Google Translate, a translation tool
            ("Google Translate",
             "https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb"),
            # Save to Pocket, a tool for saving web pages to read later
            ("Save to Pocket",
             "https://chrome.google.com/webstore/detail/save-to-pocket/niloccemoadcdkdjlinkgdfekeahmflj"),
            # Awesome Screenshot, a screen capture tool
            ("Awesome Screenshot",
             "https://chrome.google.com/webstore/detail/awesome-screenshot/nlipoenfbbikpbjkfpfillcgkoblgpmj"),
            # OneTab, a tool for managing tabs
            ("OneTab", "https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall"),
            # The Great Suspender, a tool for suspending tabs to save memory
            ("The Great Suspender",
             "https://chrome.google.com/webstore/detail/the-great-suspender/klbibkeccnjlkjkiokjodocebajanakg"),
            # StayFocusd, a tool for managing time spent on distracting websites
            ("StayFocusd", "https://chrome.google.com/webstore/detail/stayfocusd/laankejkbhbdhmipfmgcngdelahlfoji"),
            # RescueTime, a tool for tracking time spent on websites and apps
            ("RescueTime", "https://chrome.google.com/webstore/detail/rescuetime/bmnlcjabgnpnenekpadlanbbkooimhnj"),
            # Boomerang for Gmail, a tool for scheduling and tracking emails
            ("Boomerang for Gmail",
             "https://chrome.google.com/webstore/detail/boomerang-for-gmail/mdanidgdpmkimeiiojknlnekblgmpdll"),
            # Todoist, a to-do list and task management tool
            ("Todoist",
             "https://chrome.google.com/webstore/detail/todoist-to-do-list-task-l/jldhpllghnbhlleeobkclaookdhncomo"),
            # Buffer, a tool for scheduling social media posts
            ("Buffer", "https://chrome.google.com/webstore/detail/buffer/noojglkidnpfjbincgijbaiedldjfbhh"),
            # Hootsuite Hootlet, a tool for scheduling and tracking social media posts
            ("Hootsuite Hootlet", "https://chrome.google.com/webstore/detail"),
            # Full Page Screen Capture, a tool for capturing full webpage screenshots
            ("Full Page Screen Capture",
             "https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl"),
            # Grammarly for Microsoft Office, an extension for grammar and spelling check in Microsoft Office
            ("Grammarly for Microsoft Office",
             "https://chrome.google.com/webstore/detail/grammarly-for-microsoft-o/eljapbgkmlngdpckoiiibecpddcmgdlh"),
            # Tampermonkey, a userscript manager
            ("Tampermonkey", "https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo"),
            # Wappalyzer, a tool for identifying web technologies used on websites
            ("Wappalyzer", "https://chrome.google.com/webstore/detail/wappalyzer/gppongmhjkpfnbhagpmjfkannfbllamg"),
            # Postman, a tool for API development and testing
            ("Postman", "https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop")

        ]

        for extension in extensions:
            print(extension[0])
            webbrowser.open(extension[1])


if __name__ == '__main__':
    freshinstall()
