import opa_client.opa
from lib import action


class UpdateUrlPolicy(action.OpaBaseAction):

    def run(self, url, policyendpoint):
        return self.opa.update_opa_policy_fromurl(url, endpoint=policyendpoint)