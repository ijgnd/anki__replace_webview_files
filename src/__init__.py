# Copyright: ijgnd
#            Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html 

import os

from anki.utils import pointVersion

from aqt import mw
from aqt import gui_hooks


css_folder_for_anki_version = {
    "21": "21",
    "22": "21",  # for Anki version 22 use the contents of the folder 21 
}
js_folder_for_anki_version = {
}


v = pointVersion()
if v in css_folder_for_anki_version:
    my_css_folder = css_folder_for_anki_version[v]
else:  # for newer Anki versions try the latest version and hope for the best
    my_css_folder = css_folder_for_anki_version[max(css_folder_for_anki_version, key=int)]

addon_path = os.path.dirname(__file__)
addonfoldername = os.path.basename(addon_path)
my_css_folder_absolute = os.path.join(addon_path, "web", "css", my_css_folder)

mycssfiles = [os.path.basename(f) for f in os.listdir(my_css_folder_absolute) if f.endswith(".css")]

regex = r"(web.*)"
mw.addonManager.setWebExports(__name__, regex)


def replace_css(web_content, context):
    for idx, filename in enumerate(web_content.css):
        if filename in mycssfiles:
            web_content.css[idx] = f"/_addons/{addonfoldername}/web/css/{my_css_folder}/{filename}"
gui_hooks.webview_will_set_content.append(replace_css)
