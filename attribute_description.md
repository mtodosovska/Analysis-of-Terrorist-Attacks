The data set contains the information for over 150 000 terrorist attacks that have occured around the world between 1970 and 2015 (except for 1993). It contains has above 100 attributes describing the attacks. Often times, more than one attribute is used to describe the same variable. For example, there 4 attributes used in order to determine the date when the attack occured, the day, month, and year of the attack, and in case these are absent an approximate date. As well as this we have 2 attributes used to express the length of the attack, one of them, 'extended', expresses whether the attack lasted for more than 24 hours, 'resolution', shows the date when the situation (attack, hostage situation) ended. We, also, have a wide variety of attributes explaining the place where the event occured, for example, country, region, city, latitude, and longitude. As well as this attributes explaining whether the incident occured in the city itself or in its vincinity, and the specificity, discribed as follows:
1 = event occurred in city/village/town and lat/long is for that location

2 = event occurred in city/village/town and no lat/long could be found, so coordinates are for centroid of smallest subnational administrative region identified

3 = event did not occur in city/village/town, so coordinates are for centroid of smallest subnational administrative region identified

4 = no 2nd order or smaller region could be identified, so coordinates are for center of 1st order administrative region

5 = no 1st order administrative region could be identified for the location of the attack, so latitude and longitude are unknown

Next, we have 3 criteria defining, respectively, whether the attack was tended towards
	- POLITICAL, ECONOMIC, RELIGIOUS, OR SOCIAL GOAL
	- INTENTION TO COERCE, INTIMIDATE OR PUBLICIZE TO LARGER AUDIENCE(S)
	- OUTSIDE INTERNATIONAL HUMANITARIAN LAW
This attributes can get the values of 1, 0, or no value, depending on whether there is information to put the attack in the given category.
Then, there is the 'doubtterr' attribute, describing whether there is doubt if the attack was an act of terrorism (1 - yes, 0 - no, -9 - the entry was added before this attribute was added, generally for the data before 1997). If there was any doubt that the attack was an act of terrorism, then the next attribute 'alternative' will have a value (1 - insurgency/guerrila attack, 2 - other crime type, 3 - inter/intra group conflict, 4 - lack of internationality, 5 - state actors(systematically coded after 2012)). 'multiple' is a field describing whether the attack was a part of multiple incident [0/1]. The last two fields are systematically avilable after 1997. 'success' and 'suicide' define whether the attack was successeful, and whether it was a suicide attack, respectively.
There are multiple attributes defining the attack type, but only the first one 'attacktype1_txt
' seems to have values for most of the attacks, hence that is the one we will be using in our analysis.
Next, we have a few attributes describing the target, such as: type, subtype, nationality.
As well as this, we have the name of the group that carried out the attack. There is a field conating the motive for the attack, but it is surprisingly sparse. As well as this, there is a weapon type, again, surprisingly sparse.