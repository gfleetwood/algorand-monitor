from diagrams import Cluster, Diagram
from diagrams.programming.language import Python
from diagrams.programming.language import Bash
from diagrams.generic.storage import Storage
from diagrams.generic.blank import Blank
from diagrams.generic.database import SQL

with Diagram("Algorand Monitor", show = True):

    Blank("Coin Martket Cap API") >> \
    Python("Read Data") >> \
    Storage("Datalake") >> \
    Python("write Data") >> \
    SQL("Datawarehouse") >> \
    Blank("R Shiny App")
