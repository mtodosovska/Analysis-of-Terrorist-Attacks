# Analysis of Terrorist Attacks - Report
###Project in Data Mining by:
[![](https://avatars1.githubusercontent.com/u/8987819?v=3&s=150)](https://github.com/DajanaS "Dajana Stojchevska") [![](https://avatars0.githubusercontent.com/u/18115441?v=3&s=150)](https://github.com/mtodosovska "Marija Todosovska") <br />
## Introduction
Terrorism has become a common social issue. It is an unlawful act of violence which is used by the terrorists to make people fear and to threaten common public and government in order to achieve some goal.  Their primary target are the civilians of the country which could be any of us. It is pulling the human nation many years back from the proper development. This is why we have decided to research on this topic and make some data analysis, to see how terrorism "improves" and how much it can threaten our lives in future.
	
## Conclusions
Every year the number of terrorist attacks increases. Is the number alarming? Does the number of casualties increases as the number of attacks increases? The following graphs show us the number of attacks per year and casualties per year.
	
![Number of attacks per year](attacksPerYear.png)
![Casualties per year](casualtiesPerYear.png)	
	
Graphs look similar, so we can conclude that the general number of attacks per year has grown along with the number of casualties accordingly, which is not surprising.

Okay, but are all these attacks lethal? It wouldn't be that dangerous if the attackers' point was just to attract the public attention for some reason but without any victims... let's check this out.
	
![Lethal vs nonlethal attacks](lethal.png)

So, it is almost half-half, but still non-lethal attacks' number is bigger.

We decided to find the city that is the most dangerous. We started by finding what are the cities which have the most attacks. Then, we took the first 5, and checked the probabilities to be killed in any of the attacks in these cities.

 	Chances of being attacked in Baghdad: 0.0249951323988
 	Chances of being killed in an attack in Baghdad: 9.46914505998e-07
 	Chances of being attacked in Karachi: 0.0210257697456
 	Chances of being killed in an attack in Karachi: 3.05751649476e-07
 	Chances of being attacked in Lima: 0.0249976539039
 	Chances of being killed in an attack in Lima: 1.00908584235e-07
 	Chances of being attacked in Belfast: 0.0137818454292
 	Chances of being killed in an attack in Belfast: 1.28352449225e-06
 	Chances of being attacked in Santiago: 0.0192901234568
 	Chances of being killed in an attack in Santiago: 3.1941994905e-08

Conclusion is that one is most likely to be attacked in Lima, but most likely to be killed in Belfast if they are attacked.