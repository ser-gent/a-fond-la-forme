from .Epreuve import Epreuve
import math


class Course(Epreuve):
    def __init__(self, distance, chrono, haies, genre):
        if haies:
            super(Course, self).__init__(str(distance) + "mH", "s")
        else:
            super(Course, self).__init__(str(distance) + "m", "s")
        self.distance = int(distance)
        self.perf = float(chrono)
        self.haies = haies
        self.score = self.calculerPoint(genre)

    def calculerPoint(self, genre):
        if genre == 1:
            if self.haies == False:
                CourseIndex_H = {
                    #          a     b     c
                    100: (25.4347, 18.0, 1.81),
                    400: (1.53775, 82.0, 1.81),
                    1500: (0.03768, 480.0, 1.85),
                }

                (a, b, c) = CourseIndex_H.get(self.distance)
            else:
                # 110mH
                a = 5.74352
                b = 28.50
                c = 1.92
        else:
            if self.haies == False:
                CourseIndex_F = {
                    #          a     b     c
                    200: (4.99087, 42.50, 1.81),
                    800: (0.11193, 254.00, 1.88),
                }

                (a, b, c) = CourseIndex_F.get(self.distance)
            else:
                # 100mH
                a = 9.23076
                b = 26.70
                c = 1.835

        P = a * (b - self.perf) ** c

        return math.floor(P)

    def details(self):
        print("----------------")
        if self.haies:
            print("Epreuve :" + str(self.distance) + "m haies")
        else:
            print("Distance : " + str(self.distance) + "m")

        print(
            "Temps réalisé : "
            + str(self.perf)
            + " "
            + self.unite
            + " - "
            + str(self.score)
            + " points"
        )
