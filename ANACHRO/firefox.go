package main

import (
	"fmt"
	"net/http"
)

type link struct {
	name    string
	address string
}

func index(w http.ResponseWriter, r *http.Request) {
	SOFTWARE := []link{
		{"BalenaEtcher", "https://www.balena.io/etcher/"},
		{"CAVA", "https://github.com/karlstav/cava"},
		{"GIMP Resynthesizer", "https://github.com/bootchk/resynthesizer"},
		{"GLava", "https://github.com/bootchk/resynthesizer"},
		{"Gogh", "https://github.com/Mayccoll/Gogh"},
		{"KDE Connect", "https://kdeconnect.kde.org/"},
		{"Kdenlive", "https://kdenlive.org/en/"},
		{"MEGA CMD", "https://mega.nz/cmd"},
		{"ProtonVPN", "https://protonvpn.com/download"},
		{"RetroArch", "https://github.com/libretro/RetroArch"},
		{"Ventoy", "https://github.com/ventoy/Ventoy"},
		{"VirtualBox", "https://www.virtualbox.org/wiki/Linux_Downloads"},
		{"Webcamoid", "http://webcamoid.github.io/"},
		{"youtube-dlp", "https://github.com/yt-dlp/yt-dlp"},
	}

	FIREFOX := []link{
		{"Crono", "https://addons.mozilla.org/en-US/firefox/addon/crono-app/"},
		{"Ctrl+Number", "https://addons.mozilla.org/en-US/firefox/addon/ctrl-number-to-switch-tabs/"},
		{"Custom New Tabs", "https://addons.mozilla.org/en-US/firefox/addon/custom-new-tabs/"},
		{"Dark Reader", "https://addons.mozilla.org/en-US/firefox/addon/darkreader/"},
		{"Duplicate Tab", "https://addons.mozilla.org/en-US/firefox/addon/duplicate-tab-shortcut/"},
		{"Stylus Themes", "https://github.com/StylishThemes"},
		{"Stylus", "https://addons.mozilla.org/en-US/firefox/addon/styl-us/"},
		{"Tampermonkey", "https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/"},
		{"Video Download Helper", "https://addons.mozilla.org/en-US/firefox/addon/video-downloadhelper/"},
		{"Video Speed", "https://addons.mozilla.org/en-US/firefox/addon/videospeed/"},
		{"uBlock Origin", "https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/"},
	}

	CHROME := []link{
		{"Allow Right-Click", "https://chrome.google.com/webstore/detail/allow-right-click/hompjdfbfmmmgflfjdlnkohcplmboaeo?hl=en"},
		{"Bypass Paywalls", "https://github.com/iamadamdev/bypass-paywalls-chrome"},
		{"Image Downloader", "https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj?hl=en-US"},
		{"LastPass", "https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd?hl=en-US"},
		{"Stylus", "https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne?hl=en"},
		{"Tabliss", "https://chrome.google.com/webstore/detail/tabliss-a-beautiful-new-t/hipekcciheckooncpjeljhnekcoolahp"},
	}

	SOURCES := []string{"Software", "Firefox", "Chrome"}

	// software
	for i, n := range [][]link{SOFTWARE, FIREFOX, CHROME} {
		fmt.Fprintf(w, "<h1>%s</h1>\n", SOURCES[i])
		fmt.Fprintf(w, "<ul>\n")
		for _, l := range n {
			fmt.Fprintf(w, "<li><h2><a href=%q target=\"_blank\">%s</a></h2></li>\n", l.address, l.name)
		}
		fmt.Fprintf(w, "</ul>\n")
	}
}

func main() {
	http.HandleFunc("/", index)
	fmt.Println("Server is running...")
    fmt.Println("http://localhost:3000")
	http.ListenAndServe(":3000", nil)
}
