from document import APIDoc
import connexion
from connexion.resolver import RestyResolver

doc = APIDoc(
    title = 'yolo',
    version = '1.0',
    swagger = '2.0'
)

doc.add_apis('mapreduce', 'keyvalue')

app = connexion.App(__name__)
app.add_api(doc.to_dict(), resolver = RestyResolver('controllers'))
app.run()
#print(doc.paths)
