class SetRewardToRiskRatio():

    def __init__(self, rewardRiskRatio):
        self.rrRatio = rewardRiskRatio

    def checkValueInRange(self):
        return self.rrRatio > 0