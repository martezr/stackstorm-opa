from lib import action
import opa_client.opa


class CheckConnection(action.OpaBaseAction):

    def run(self):
        return self.opa.check_connection()