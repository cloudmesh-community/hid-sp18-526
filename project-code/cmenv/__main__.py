import connexion
import yaml
from cmenv.document import APIDoc
from cmenv.resolver import CMResolver
import cmenv.constants as constants
import cmenv.config as config

def main():
    doc = APIDoc(
        title = 'CMENV',
        version = '1.0',
        swagger = '2.0'
    )

    controller_dispatch = doc.set_apis(config.apis)

    app = connexion.App(__name__)
    app.add_api(doc.to_dict(), resolver = CMResolver(controller_dispatch))
    app.run(port = 8080)
