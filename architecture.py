from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage
# diagrams.generic.os.Ubuntu
# diagrams.generic.blank.Blank
# diagrams.programming.flowchart.Database
#diagrams.programming.language.Python
#diagrams.programming.language.R
#diagrams.programming.language.Bash
#https://diagrams.mingrammer.com/docs/nodes/gcp


with Diagram("Algorand Monitor", show = True):
    SQL("supabase") >> EC2("web")
