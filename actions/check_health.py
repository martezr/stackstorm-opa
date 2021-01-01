from st2common.runners.base_action import Action


class CheckHealth(Action):

    def run(self):
        return self.check_connection()