# N.B.A.A.-Never-Broke-Again-Algorithm-
Neural network built w/ Tensorflow that aims to predict NBA games for the purpose of sports betting. (Work In Progress, tips and recommendations welcome.)

Data is pulled from https://pypi.org/project/nba-api/

To do

-add the file that pulls seasonal data (makes a csv file of a whole season and then stacks them together.)

-current success rate is 70% but that is by testing any random 2018-2019 game. I could possibly improve success rate by retraining model after every 2018-19 game with a weight bias against the respectice teams. (team strength changes more season per season than overall trends(ex. more 3pt shooting now) in the NBA that may affect team win rates)

-add a check to see if teams inputted are the same. MIA vs. MIA is invalid

-possible something has been overlooked. my stats holding data structures dont reset season to season. Meaning that the 1st season holds the data from season 1, season 2 from 1 and 2, and season 3 from 1,2,and 3. No way of knowing yet if this helped my model in the end but it would reward teams that did good during that period. If I did that the last 30 years instead where the average stats may be more similar, this would make my model do worse. Have to check model with stats resetting and with less seasons(currently at 5)
                           
