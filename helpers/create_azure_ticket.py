from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import os
from dotenv import find_dotenv, load_dotenv

find_dotenv()
load_dotenv()


# Retrieve personal access token from environment variable
personal_access_token = os.getenv("PERSONAL_ACCESS_TOKEN")

organization_url = "https://dev.azure.com/NRG-Acceleration/"
project = 'NRG-Acceleration'

# Connect to Azure DevOps
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Access work item tracking client
wit_client = connection.clients.get_work_item_tracking_client()

epic_id = 1060 
area_path = 'NRG_Agile_Enablement'
work_item_type = "Issue"

def create_azure_issue(title,description,anforderer, atc_id, location_id, ne_id, project_id):
    
    new_work_item = [
            {
               "op": "add",
                "path": "/fields/System.Title",
                "from": None,
               "value": title
            },
            {
               "op": "add",
                "path": "/fields/Microsoft.VSTS.CodeReview.ContextOwner",
                "from": None,
                "value": anforderer
            },
            {
                "op": "add",
                "path": "/fields/System.Description",
                "from": None,
                "value": f"{description}\nATC-Nummer: {atc_id}\nStandort-Nummer: {location_id}\nNE-Nummer: {ne_id}'\nProjekt-ID:{project_id}"
            },
            {
                "op": "add",
                "path": "/fields/System.Parent",
                "from": None,
                "value": epic_id
            },
            {
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": f"{organization_url}/{project}/_apis/wit/workItems/{epic_id}",
                    "attributes": {
                        "comment": "Parent link to Epic"
                    }
                }
            },
            
            {
                "op": "add",
                "path": "/fields/System.AreaPath",
                "from": None,
                "value":f"{project}\\{area_path}" 
            }
        ]
    created_work_item = wit_client.create_work_item(project=project,document=new_work_item, type=work_item_type)
    return created_work_item