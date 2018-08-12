import sys
from os.path import dirname, abspath, basename
import subprocess

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from os.path import dirname, join

__author__ = 'shamanon'

class WebSearchSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(WebSearchSkill, self).__init__(name="WebSearchSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    @intent_handler(IntentBuilder("").require("WebSearch").require("For").require("ForKeywords").require("search"))
    def handle_web_search_intent(self, message):
        site = message.data.get("ForKeywords")
        term = message.data.get("search")
        if site == "pirate bay":
            url = "https://thepiratebay.org/search/" + term.replace(" ", "%20") + "/0/99/0"
        else:
            url = "https://google.com/search?q=" + term.replace(" ", "+")
            	
        self.speak_dialog("search.for", {"term": term, "site": site} )
        subprocess.run(["google-chrome", url])
        
def create_skill():
    return WebSearchSkill()
