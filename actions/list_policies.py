import opa_client.opa
from lib import action


class ListPolicies(action.OpaBaseAction):

    def run(self):
        return self.opa.get_policies_list()