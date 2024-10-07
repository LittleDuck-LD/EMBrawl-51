import csv


class Random_Chest:
    def getBoxDataByName(self, BoxName="NewHeroBoxPaidSmall"):
        with open('Classes/Files/assets/csv_logic/random_chest.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            AllBoxData = {}
            LastBoxName = ""
            for row in csv_reader:
                if line_count <= 1:
                    line_count += 1
                elif row[14] != "1":
                    line_count += 1
                elif row[0] != "":
                    LastBoxName = row[0]
                    AllBoxData[LastBoxName] = [{
                        "RewardName" : row[7],
                        "Rate" : row[8],
                        "GuaranteedDrop": row[16]
                        }]
                    line_count += 1
                elif row[0] == "":
                    AllBoxData[LastBoxName].append({
                        "RewardName" : row[7],
                        "Rate" : row[8],
                        "GuaranteedDrop": row[16]
                    })
                    line_count += 1
                else:
                    line_count += 1
        
        return AllBoxData[BoxName]