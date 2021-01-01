from opa_client.opa import OpaClient
from st2common.runners.base_action import Action


class OpaBaseAction(Action):

    def __init__(self, config):
        super(OpaBaseAction, self).__init__(config)
        self.opa = self._get_client()

    def _get_client(self):
        url = self.config['url']
        port = self.config['port']
        version = self.config['version']
        ssl = self.config['ssl']
        certificate = self.config['certificate']

        client = OpaClient(
            host=url,
            port=port,
            version=version,
            ssl=ssl,
            cert=certificate,
          )
        return client