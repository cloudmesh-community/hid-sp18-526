from document import APIDoc
from resolver import CMResolver
import connexion

doc = APIDoc(
    title = 'yolo',
    version = '1.0',
    swagger = '2.0'
)

controller_dispatch = doc.set_apis(['services', 'store'])

app = connexion.App(__name__)
app.add_api(doc.to_dict(), resolver = CMResolver(controller_dispatch))
app.run(port = 8080)
