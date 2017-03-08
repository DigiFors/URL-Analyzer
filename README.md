# URL-Analyzer

In order to unshorten URL's and display http-header fragments,
this tool uses a python request to gain important intel from 
the given URL(e.g. Location, Server, Expiring-Date) and creates
a .csv-file, called Results.csv. By using a .txt-file with 
different user-agents the tool allows to unshorten the URL and 
therfore to trace possible different sources depending on the 
user-agent.

Both user_agents.txt and the .py script have to be executed
from the main Python folder. Keep in mind, the Results.csv will
overwrite any pre-existing .csv with the same name in that directory.

We recommend to use OpenOffice to open the .csv, since it wil ask
you by default to change the delimiter to "," and thus to place 
each output in a seperate field. Othwise you won't be able to see
all data or can't figure out in which column it belongs. 

by HH and CK
