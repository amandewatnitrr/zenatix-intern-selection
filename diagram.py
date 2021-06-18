from diagrams import Diagram, Edge
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.gcp.iot import IotCore
from diagrams.firebase.develop import RealtimeDatabase
from diagrams.programming.language import Python

from diagrams.aws.network import ELB

with Diagram("IoT Architecture", show=False):
    Python("Server") >> Edge(color="black",style="bold",label="Pushing status 0 if data not recieved after 60 sec interval") >> RealtimeDatabase("Database") >> Edge(color="black",style="bold",label="Reading 'status' for data succesfully recieved or not") >> Python("Buffering Data using queueing mechanism")
    IotCore("Sensor") >> Edge(color="black",style="bold",label="Reading data from Sensor") >> Python("Edge") >> Edge(color="black",style="bold",label="Pushing Sensor data to Firebase")>> RealtimeDatabase("Database") >> Edge(color="black",style="bold",label="Reading data from Firebase") >> Python("Server")>> Edge(color="black",style="bold",label="Saving data in CSV on Server Side") >> RDS("Serer Database")
    