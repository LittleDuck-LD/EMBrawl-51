import csv


class Random_Chest_Rewards:
    def getRewardDataByName(self, RewardName="Coins S"):
        with open('Classes/Files/assets/csv_logic/random_chest_rewards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            AllRewardData = {}
            LastRewardName = ""
            for row in csv_reader:
                if line_count <= 1:
                    line_count += 1
                elif row[0] != "":
                    LastRewardName = row[0]
                    AllRewardData[LastRewardName] = {
                        "TypeName" : row[1],
                        "AmountMin" : row[2],
                        "AmountMax": row[3],
                        "FallbackTypeName": row[4],
                        "FallbackAmount": row[5],
                        "SetCount": row[6],
                        "SetName": row[7]
                        }
                    line_count += 1
                else:
                    line_count += 1
        
        return AllRewardData[RewardName]