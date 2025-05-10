class Student:
    name =''
    scores={}
    score_average =0
    def __init__(self,nam,alg,eng,chem):
        self.name=nam
        self.scores={"Algebra":alg,
             "English":eng,
             "Chemistry":chem}
    
    @classmethod
    def from_strings(cls,input_strings):
        na,alg,eng,chem=input_strings.split(',')
        return  cls(na,int(alg),int(eng),int(chem))
    
    @staticmethod
    def get_school_info():
        return "Harvard"
    
    def score_averag(self):
        score_average =sum(self.scores.values())/len(self.scores)
        return score_average

    def rank (std1):
        std1.score_average=std1.score_averag()
        avg_score=int(std1.score_average)
        if avg_score>=9:
            return "A"
        elif avg_score >=8:
            return "B"
        elif avg_score >=7:
            return "C"
        elif avg_score >=6:
            return "D"
        elif avg_score >=5:
            return "E"
        else:
            return "F"

            
    def information(std1):
        print("Student's information:")
        print("Name:",std1.name)
        for key in std1.scores:
            print(f"Score{key}:{std1.scores[key]}")
        average_return=std1.score_averag()
        average_return=round(average_return,2)
        print("Average score of 3 subject:",average_return)
        print("Student's Rank:",std1.rank())





input_string=input("Please fill the information of the student:")
std1=Student.from_strings(input_string)
std1.information()

std2 = Student("Nguyen Van A", 8, 9, 10)

