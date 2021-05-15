import math
import sys

# "course abbreviation": [hole 1, hole 2, ... , hole 17, hole 18]
courses = {
    "PCC": [4, 4, 4, 5, 3, 4, 5, 3, 4, 4, 5, 4, 3, 5, 4, 3, 4, 4], #Portsmouth
    "RCC": [4, 5, 4, 3, 4, 5, 3, 4, 4, 4, 5, 3, 4, 4, 5, 3, 4, 4], #Rochester
    "CCC": [4, 4, 3, 4, 4, 4, 4, 5, 3, 4, 4, 3, 4, 4, 3, 5, 4, 4], #Cochecho
    "OAK": [4, 4, 3, 5, 3, 4, 4, 4, 4, 4, 5, 4, 3, 4, 4, 3, 4, 5], #Oaks
    "PGC": [5, 5, 3, 4, 4, 4, 4, 4, 3, 4, 3, 4, 5, 3, 5, 3, 4, 4]  #Peace
}

# "course abbreviation": [full name, rating, slope]
course_info = {
    "PCC": ["Portsmouth Country Club"],
    "RCC": ["Rochester Country Club"],
    "CCC": ["Cochecho Country Club"],
    "OAK": ["The Oaks Golf Links"],
    "PGC": ["Peace Golf Course"]
}


class Round(object):
    hole_1 = []
    hole_2 = []
    hole_3 = []
    hole_4 = []
    hole_5 = []
    hole_6 = []
    hole_7 = []
    hole_8 = []
    hole_9 = []
    hole_10 = []
    hole_11 = []
    hole_12 = []
    hole_13 = []
    hole_14 = []
    hole_15 = []
    hole_16 = []
    hole_17 = []
    hole_18 = []
    holes = [hole_1, hole_2, hole_3, hole_4, hole_5, hole_6, hole_7, hole_8, hole_9,
             hole_10, hole_11, hole_12, hole_13, hole_14, hole_15, hole_16, hole_17, hole_18]

    #hole_array = [hole num, par, score, num of putts, fairway, +/- for hole, green in regulation, up & down]
    #hole_num   = [    0,    1,     2,       3,          4,           5,              6,               7    ]


    filter_array = []

    def __init__(self, round_num, pars, score, putts, fairway):
        self.round_num = round_num
        self.pars = pars #array range: 3 - 5
        self.score = score #array range: 1 - inf
        self.putts = putts #array range: 0 - 4
        self.fairway = fairway #array  char: L (left), H (hit), R (right), S (short), T (through)

    def hole_info(self):
        #re-initializing holes array
        for i in range(18):
            del self.holes[i] [:]
        #par, score, and putts
        for i in range(18):
            self.holes[i].append(i + 1)
            self.holes[i].append(self.pars[i])
            self.holes[i].append(self.score[i])
            self.holes[i].append(self.putts[i])
            self.holes[i].append(self.fairway[i])

        #determine what they got on the hole
        for i in range(18):
            if self.pars[i] == self.score[i]:
                self.holes[i].append(0) #0 = par
            elif (self.pars[i] + 1) == self.score[i]:
                self.holes[i].append(1) #+1 = bogey
            elif (self.pars[i] + 2) == self.score[i]:
                self.holes[i].append(2) #+2 = double bogey
            elif (self.pars[i] + 2) < self.score[i]:
                self.holes[i].append(3) #3 = more than double bogey
            elif (self.pars[i] - 1) == self.score[i]:
                self.holes[i].append(-1) #-1 = birdy
            elif (self.pars[i] - 2) == self.score[i]:
                self.holes[i].append(-2) #-2 = eagle
            elif (self.pars[i] - 3) == self.score[i]:
                self.holes[i].append(-3) #-3 = albatross
            else:
                self.holes[i].append(-4) #-4 = shit that's a hole in one on a par five

        #green in regulation
        for i in range(18):
            if (self.score[i] - self.putts[i]) == (self.pars[i] - 2):
                self.holes[i].append(0) #0 = green in regulation
            elif (self.score[i] - self.putts[i]) > (self.pars[i] - 2):
                self.holes[i].append(1) #+1 = green over regulation
            else:
                self.holes[i].append(-1) #-1 = green under regulation

        #up & downs
        for i in range(18):
            if self.score[i] >= self.pars[i]: #if you get a birdy is that considered up & down?
                if self.putts[i] == 1:
                    self.holes[i].append(True) #went up & down
                else:
                    self.holes[i].append(False) #didn't go up & down
            else:
                self.holes[i].append(None) #need a null or nil or something, does not apply

    def create_filter_array_single_round(self, filter):
        del self.filter_array [:]
        if filter.lower() == "none":
            self.filter_array = self.holes
        elif filter.lower() == "par 3" or "par three":
            for i in range(18):
                if self.pars[i] == 3:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "par 4" or "par four":
            for i in range(18):
                if self.pars[i] == 4:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "par 5" or "par five":
            for i in range(18):
                if self.pars[i] == 5:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "pars":
            for i in range(18):
                if self.score[i] == self.pars[i]:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "bogey":
            for i in range(18):
                if self.score[i] == (self.pars[i] + 1):
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "bogey +" or "bogey plus":
            for i in range(18):
                if self.score[i] > self.pars[i]:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "birdy":
            for i in range(18):
                if self.score[i] == (self.pars[i] - 1):
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "birdy -" or "birdy minus":
            for i in range(18):
                if self.score[i] < self.pars[i]:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "1 putts" or "one putts":
            for i in range(18):
                if self.putts[i] == 1:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "2 putts" or "two putts":
            for i in range(18):
                if self.putts[i] == 2:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "2 putts -" or "two putts -" or "2 putts minus" or "two putts minus":
            for i in range(18):
                if self.putts[i] <= 2:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "3 putts" or "three putts":
            for i in range(18):
                if self.putts[i] == 3:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "3 putts +" or "three putts +" or "3 putts plus" or "three putts plus":
            for i in range(18):
                if self.putts[i] > 2:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "fairway":
            for i in range(18):
                if self.holes[i][4].upper() == 'H':
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "greens":
            for i in range(18):
                if self.holes[i][6] <= 0:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "front" or "front 9" or "front nine":
            for i in range(18):
                if self.holes[i][0] < 10:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "back" or "back 9" or "back nine":
            for i in range(18):
                if self.holes[i][0] > 9:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "up and down":
            for i in range(18):
                if self.holes[i][7]:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "failed up and downs" or "up and down fails":
            for i in range(18):
                if not self.holes[i][7]:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "scramble" or "scrambling":
            for i in range(18):
                if self.holes[i][7] and self.score[i] == self.pars[i]:
                    self.filter_array.append(self.holes[i])
        elif filter.lower() == "scramble fails" or "scrambling fails" or "failed scramble" or "failed scrambling":
            for i in range(18):
                if not self.holes[i][7] and (self.score[i] - self.putts[i]) == (self.pars[i] - 1):
                    self.filter_array.append(self.holes[i])
        else:
            print ("not a current filter")
            sys.exit()


    #calcuate states for the holes
    def print_stats_single_round(self, category):
        if category.lower() == "score":
            print (" hole   par   score   +/-")
            for i in range(len(self.filter_array)):
                space1 = math.trunc(math.log10(18 - self.filter_array[i][0] + 1))
                if self.filter_array[i][5] > 0:
                    print ("".ljust(space1 + 2) + str(self.filter_array[i][0]) + "     " + str(self.filter_array[i][1]) + "      " + str(self.filter_array[i][2]) + "     +" + str(self.filter_array[i][5]))
                elif self.filter_array[i][5] == 0:
                    print ("".ljust(space1 + 2) + str(self.filter_array[i][0]) + "     " + str(self.filter_array[i][1]) + "      " + str(self.filter_array[i][2]) + "      " + str(self.filter_array[i][5]))
                else:
                    print ("".ljust(space1 + 2) + str(self.filter_array[i][0]) + "     " + str(self.filter_array[i][1]) + "      " + str(self.filter_array[i][2]) + "     " + str(self.filter_array[i][5]))
            par_total = 0
            score_total = 0
            for i in range(len(self.filter_array)):
                par_total += self.filter_array[i][1]
                score_total += self.filter_array[i][2]
            if (score_total - par_total) > 0:
                print (" Total   " + str(par_total) + "     " + str(score_total) + "    +" + str(score_total - par_total))
            elif (score_total - par_total) == 0:
                print(" Total   " + str(par_total) + "     " + str(score_total) + "     " + str(score_total - par_total))
            else:
                print (" Total   " + str(par_total) + "     " + str(score_total) + "    " + str(score_total - par_total))
            return [par_total, score_total, score_total - par_total, len(self.filter_array)]

        elif category.lower() == "putts":
            putt_total = 0
            for i in range(len(self.filter_array)):
                putt_total += self.filter_array[i][3]
            print ("Total putts: " + str(putt_total))
            print ("Average number of putts per hole: " + str(float(putt_total)/len(self.filter_array)))
            return [putt_total, len(self.filter_array)]

        elif category.lower() == "greens":
            in_reg_total = 0
            over_reg_total = 0
            under_reg_total = 0
            for i in range(len(self.filter_array)):
                if self.filter_array[i][6] == 0:
                    in_reg_total += 1
                elif self.filter_array[i][6] == 1:
                    over_reg_total += 1
                elif self.filter_array[i][6] == -1:
                    under_reg_total += 1
            print ("green...")
            print ("in regulation: " + str((float(in_reg_total)/len(self.filter_array)) * 100) + "%")
            print ("over regulation: " + str((float(over_reg_total)/len(self.filter_array)) * 100) + "%")
            print ("under regulation: " + str((float(under_reg_total)/len(self.filter_array)) * 100) + "%")
            return [in_reg_total, over_reg_total, under_reg_total, len(self.filter_array)]

        elif category.lower() == "fairway":
            hit_total = 0
            left_total = 0
            right_total = 0
            short_total = 0
            through_total = 0
            for i in range(len(self.filter_array)):
                if self.filter_array[i][4].upper() == 'H':
                    hit_total += 1
                elif self.filter_array[i][4].upper() == 'L':
                    left_total += 1
                elif self.filter_array[i][4].upper() == 'R':
                    right_total += 1
                elif self.filter_array[i][4].upper() == 'S':
                    short_total += 1
                elif self.filter_array[i][4].upper() == 'T':
                    through_total += 1
            print ("fairway...")
            print ("Hit: " + str((float(hit_total)/len(self.filter_array)) * 100) + "%")
            print ("Left: " + str((float(left_total)/len(self.filter_array)) * 100), "%")
            print ("Right: " + str((float(right_total)/len(self.filter_array)) * 100), "%")
            print ("Short: " + str((float(short_total)/len(self.filter_array)) * 100), "%")
            print ("Through: " + str((float(through_total)/len(self.filter_array)) * 100), "%")
            return [hit_total, right_total, left_total, short_total, through_total, len(self.filter_array)]

        elif category.lower() == "average pars":
            num_par3 = 0
            num_par4 = 0
            num_par5 = 0
            score_par3 = 0
            score_par4 = 0
            score_par5 = 0

            for i in range(len(self.filter_array)):
                if self.filter_array[i][1] == 3:
                    num_par3 += 1
                    score_par3 += self.filter_array[i][2]
                elif self.filter_array[i][1] == 4:
                    num_par4 += 1
                    score_par4 += self.filter_array[i][2]
                else:
                    num_par5 += 1
                    score_par5 += self.filter_array[i][2]

            if num_par3 == 0:
                print ("Par 3 Average: n/a")
            else:
                print ("Par 3 Average: " + str(float(score_par3)/num_par3))

            if num_par4 == 0:
                print ("Par 4 Average: n/a")
            else:
                print ("Par 4 Average: " + str(float(score_par4)/num_par4))

            if num_par5 == 0:
                print ("Par 5 Average: n/a")
            else:
                print ("Par 5 Average: " + str(float(score_par5)/num_par5))
            return [num_par3, num_par4, num_par5, score_par3, score_par4, score_par5, len(self.filter_array)]

        elif category.lower() == "up and down":
            yes = 0
            no = 0
            for i in range(len(self.filter_array)):
                if self.filter_array[i][7]:
                    yes += 1
                elif not self.filter_array[i][7]:
                    no += 1
            print ("Total up & downs: " + str(yes))
            print ("up & down percentage: " + str((float(yes)/(yes + no)) * 100) + "%")
            print ("Total failed up & downs: " + str(no))
            print ("up & down fails percentage: " + str((float(no)/(yes + no)) * 100) + "%")
            return [yes, no, len(self.filter_array)]

        elif category.lower() == "scramble" or "scrambling":
            yes = 0
            no = 0
            for i in range(len(self.filter_array)):
                if self.filter_array[i][7] and self.filter_array[i][2] == self.filter_array[i][1]:
                    yes += 1
                elif not self.filter_array[i][7] and (self.filter_array[i][2] - self.filter_array[i][3]) == (self.filter_array[i][1] - 1):
                    no += 1
            print ("Total scrambling pars: " + str(yes))
            print ("scramble percentage: " + str((float(yes)/(yes + no)) * 100) + "%")
            print ("Total failed scrambling pars: " + str(no))
            print ("scramble fails percentage: " + str((float(no)/(yes + no)) * 100) + "%")
            return [yes, no, len(self.filter_array)]

        else:
            print ("not a current statistic I'm tracking")
            sys.exit()

    #stats on multiple rounds
    #round_numbers is an array the names of the actual rounds themselves
    def print_stats_multiple_rounds(self, rounds, filter, statistic):
        return_stats = []
        total_holes_played = 0
        for i in range(len(rounds)):
            print ("round " + str(i + 1) + ":")
            rounds[i].hole_info()
            rounds[i].create_filter_array_single_round(filter)
            return_stats.append(rounds[i].print_stats_single_round(statistic))
            print ("")
        for i in range(len(return_stats)):
            total_holes_played += return_stats[i][len(return_stats) - 1]

        if statistic.lower() == "score":
            #return_stats = [par_total, score_total, score_total - par_total (plus/minus_total), len(self.filter_array)]
            par_total_all_rounds = 0
            score_total_all_rounds = 0
            for i in range(len(return_stats)):
                par_total_all_rounds += return_stats[i][0]
                score_total_all_rounds += return_stats[i][1]
            print ("Average Par: " + str(float(par_total_all_rounds)/len(return_stats)))
            print ("Average Score: " + str(float(score_total_all_rounds)/len(return_stats)))
            if (score_total_all_rounds - par_total_all_rounds) <= 0:
                print ("Total +/-: " + str(score_total_all_rounds - par_total_all_rounds))
            else:
                print ("Total +/-: +" + str(score_total_all_rounds - par_total_all_rounds))

        elif statistic.lower() == "putts":
            #return_stats = [putt_total, len(self.filter_array)]
            putt_total_all_rounds = 0
            for i in range(len(return_stats)):
                putt_total_all_rounds += return_stats[i][0]
            print ("Average number of putts per round: " + str(float(putt_total_all_rounds)/len(return_stats)))
            print ("Average number of puts per hole: " + str(float(putt_total_all_rounds)/total_holes_played))

        elif statistic.lower() == "greens":
            #return_stats = [in_reg_total, over_reg_total, under_reg_total, len(self.filter_array)]
            in_reg_total_all_rounds = 0
            over_reg_total_all_rounds = 0
            under_reg_total_all_rounds = 0
            for i in range(len(return_stats)):
                in_reg_total_all_rounds += return_stats[i][0]
                over_reg_total_all_rounds += return_stats[i][1]
                under_reg_total_all_rounds += return_stats[i][2]
            print ("Average green in regulation: " + str((float(in_reg_total_all_rounds)/total_holes_played) * 100) + "%")
            print ("Average green over regulation: " + str((float(over_reg_total_all_rounds)/total_holes_played) * 100) + "%")
            print ("Average green under regulation: " + str((float(under_reg_total_all_rounds)/total_holes_played) * 100) + "%")
        elif statistic.lower() == "fairway":
            #return_stats = [hit_total, right_total, left_total, short_total, through_total, len(self.filter_array)]
            hit_total_all_rounds = 0
            left_total_all_rounds = 0
            right_total_all_rounds = 0
            short_total_all_rounds = 0
            through_total_all_rounds = 0
            for i in range(len(return_stats)):
                hit_total_all_rounds += return_stats[i][0]
                left_total_all_rounds += return_stats[i][1]
                right_total_all_rounds += return_stats[i][2]
                short_total_all_rounds += return_stats[i][3]
                through_total_all_rounds += return_stats[i][4]
            print ("Average fairways hit: " + str((float(hit_total_all_rounds)/total_holes_played) * 100) + "%")
            print ("Average fairways missed left: " + str((float(left_total_all_rounds)/total_holes_played) * 100) + "%")
            print ("Average fairways missed right: " + str((float(right_total_all_rounds)/total_holes_played) * 100) + "%")
            print ("Average fairways left short: " + str((float(short_total_all_rounds)/total_holes_played) * 100) + "%")
            print ("Average fairways run through: " + str((float(through_total_all_rounds)/total_holes_played) * 100) + "%")

        elif statistic.lower() == "average pars":
            #return_stats = [num_par3, num_par4, num_par5, score_par3, score_par4, score_par5, len(self.filter_array)]
            num_par3_all_rounds = 0
            num_par4_all_rounds = 0
            num_par5_all_rounds = 0
            score_par3_all_rounds = 0
            score_par4_all_rounds = 0
            score_par5_all_rounds = 0
            for i in range(len(return_stats)):
                num_par3_all_rounds += return_stats[i][0]
                num_par4_all_rounds += return_stats[i][1]
                num_par5_all_rounds += return_stats[i][2]
                score_par3_all_rounds += return_stats[i][3]
                score_par4_all_rounds += return_stats[i][4]
                score_par5_all_rounds += return_stats[i][5]
            if num_par3_all_rounds == 0:
                print ("Par 3 Average: n/a")
            else:
                print ("Par 3 Average: " + str(float(score_par3_all_rounds)/num_par3_all_rounds))

            if num_par4_all_rounds == 0:
                print ("Par 4 Average: n/a")
            else:
                print ("Par 4 Average: " + str(float(score_par4_all_rounds)/num_par4_all_rounds))

            if num_par5_all_rounds == 0:
                print ("Par 5 Average: n/a")
            else:
                print ("Par 5 Average: " + str(float(score_par5_all_rounds)/num_par5_all_rounds))

        elif statistic.lower() == "up and down":
            #return_stats = [yes, no, len(self.filter_array)]
            yes_all_rounds = 0
            no_all_rounds = 0
            for i in range(len(return_stats)):
                yes_all_rounds += return_stats[i][0]
                no_all_rounds += return_stats[i][1]
            print ("Average up & downs per round: " + str(float(yes_all_rounds)/len(return_stats)))
            print ("up & down percentage: " + str(float(yes_all_rounds)/(yes_all_rounds + no_all_rounds) * 100) + "%")
            print ("Average failed up & downs per round: " + str(float(no_all_rounds)/len(return_stats)))
            print ("up & down fails percentage: " + str(float(no_all_rounds)/(yes_all_rounds + no_all_rounds) * 100) + "%")

        elif statistic.lower() == "scramble" or "scrambling":
            #return_stats = [yes, no, len(self.filter_array)]
            yes_all_rounds = 0
            no_all_rounds = 0
            for i in range(len(return_stats)):
                yes_all_rounds += return_stats[i][0]
                no_all_rounds += return_stats[i][1]
            print ("Average scrambling pars per round: " + str(float(yes_all_rounds)/len(return_stats)))
            print ("scramble percentage: " + str(float(yes_all_rounds)/(yes_all_rounds + no_all_rounds) * 100) + "%")
            print ("Average failed scrambling pars per round: " + str(float(no_all_rounds)/len(return_stats)))
            print ("scramble fails percentage: " + str(float(no_all_rounds)/(yes_all_rounds + no_all_rounds) * 100) + "%")
        else:
            print ("not a current statistic I'm tracking")
            sys.exit()


Eric_Keilty = Round(0, courses["PCC"], [], [], [])
Eric_Evans = Round(0, courses["PCC"], [], [], [])

#"PCC":            [4, 4, 4, 5, 3, 4, 5, 3, 4, 4, 5, 4, 3, 5, 4, 3, 4, 4], #Portsmouth
EK_round_1_score = [4, 4, 4, 5, 3, 4, 5, 4, 4, 3, 5, 5, 3, 4, 3, 3, 4, 5]
EK_round_1_putts = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2]
EK_round_1_fairway = ['h', 'l', 'r','h', 'l', 's','h', 'l', 't','h', 't', 'r', 'h', 's', 'r', 'h', 'h', 'r']
EK_round_1 = Round(1, courses["PCC"], EK_round_1_score, EK_round_1_putts, EK_round_1_fairway)

EK_round_2_score = [5, 4, 3, 4, 3, 4, 5, 6, 4, 3, 5, 4, 3, 4, 3, 3, 4, 5]
EK_round_2_putts = [2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 3, 2, 2, 0, 2, 1, 1, 2]
EK_round_2_fairway = ['h', 'l', 'r','h', 'l', 's','h', 'l', 't','h', 't', 'r', 'h', 's', 'r', 'h', 'h', 'r']
EK_round_2 = Round(2, courses["PCC"], EK_round_2_score, EK_round_2_putts, EK_round_2_fairway)

Eric_Keilty.print_stats_multiple_rounds([EK_round_1, EK_round_2], "par", "up and down")

#Leading Stats on tour
#average putts per round: 27.45
#sand saves: 68.75%
#bounce back: 33.33% - making a birdy or better after making a bogey or worse

#you have some math errors to fix there bud
