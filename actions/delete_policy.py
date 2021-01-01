import opa_client.opa
from lib import action


class DeletePolicy(action.OpaBaseAction):

    def run(self, policy):
        return self.opa.delete_opa_policy(policy)