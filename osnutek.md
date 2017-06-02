# Draft

## Description of the data set

Our team chose **Global Terrorism** as a topic of this project. We are going to work with the *Global Terrorism Database* which can be found at the following link: [https://www.kaggle.com/START-UMD/gtd](https://www.kaggle.com/START-UMD/gtd)

The database is given in ***CSV*** (comma-separated values) format, where each line of the file is a data record and information are separated by commas.

The data set contains the information for over 150 000 terrorist attacks that have occurred around the world between 1970 and 2015 (except for 1993). It contains above 100 attributes describing the attacks. Often times, more than one attribute is used to describe the same variable.

For example, there are 4 attributes used in order to determine the date when the attack occurred, the day, month, and year of the attack, and in case these are absent an approximate date.

As well as this we have 2 attributes used to express the length of the attack, one of them - `extended`, expresses whether the attack lasted for more than 24 hours, `resolution` shows the date when the situation (attack, hostage situation) ended.

Also, we have a wide variety of attributes explaining the place where the event occurred, for example, country, region, city, latitude and longitude. As well as these attributes explaining whether the incident occurred in the city itself or in its vicinity, and the specificity, described as follows:

- 1 = event occurred in city/village/town and lat/long is for that location;
- 2 = event occurred in city/village/town and no lat/long could be found, so coordinates are for the centroid of smallest sub-national administrative region identified;
- 3 = event did not occur in city/village/town, so coordinates are for the centroid of smallest sub-national administrative region identified;
- 4 = no 2nd order or smaller region could be identified, so coordinates are for the center of 1st order administrative region;
- 5 = no 1st order administrative region could be identified for the location of the attack, so latitude and longitude are unknown.

Next, we have 3 criteria defining, respectively, whether the attack was tended towards:

- political, economic, religious or social goal;
- intention to coerce, intimidate or publicize to larger audience(s);
- outside international humanitarian law.

These attributes can get the values of 1, 0, or no value, depending on whether there is information about the attack in order to be put in a given category.

`gname` is the attribute that shows the group that carried out the attack.

Next, there is the `doubtterr` attribute, describing whether there is doubt if the attack was an act of terrorism (1 - yes, 0 - no, -9 - the entry was added before this attribute was added, generally for the data before 1997). If there was any doubt that the attack was an act of terrorism, then the next attribute `alternative` will have a value (1 - insurgency/guerilla attack, 2 - other crime type, 3 - inter/intra group conflict, 4 - lack of internationality, 5 - state actors (systematically coded after 2012)). `multiple` is a field describing whether the attack was a part of multiple incidents (0/1). The last two fields are systematically available after 1997.

Attributes `success` and `suicide` define whether the attack was successful, and whether it was a suicide attack, respectively.
There are multiple attributes defining the attack type, but only the first one `attacktype1_txt` seems to have values for most of the attacks, hence that is the one we will be using in our analysis.

Next, we have a few attributes describing the target, such as: `type`, `subtype`, `nationality`.
As well as this, we have the name of the group that carried out the attack. There is a field containing the motive for the attack, but it is surprisingly sparse. Also, there is a weapon type, again, surprisingly sparse.


`npreps` indicates the number of terrorists that took part in the incident, while `nperpcap` shows the number of perpetrators taken into custody.

`claimed` - whether responsibility was claimed for the attack and `claimmode` - the way the claim was made, `compclaim` - whether multiple claims were made.

`nkill` - number of people killed in the incident, `nkillus` - number of US citizens killed in the incident.

`nkillter` - number of perpetrator fatalities.

`nwound` - number of people injured non-fatally in the incident, `nwoundus` - number of us citizens injured non-fatally in the incident.

`nwoundtex` - number of perpetrator injuries.

`property` - whether the incident resulted into property damage, `propvalue` - the value of the damage.

`ishostkid` - whether there were hostages and `nhostkid` - number of hostages, sparse, `nhostkidus` - US hostages.


There are multiple attributes concerning ransom for hostages, how much was asked, how much was given. As well as this, the outcome of the kidnapping, how many people survived, etc. Then, there is a group of attributes concerning whether the attack was carried out internationally or domestically.


## Goals for our project

The data represents all recorded terrorist attacks form 1973, to 2015. We have chosen the following goals:
	
- Number of attacks every year;
- Number of casualties every year;
- Numbers of lethal and non-lethal attacks;
- Correlation between success, suicide attacks;
- What is the most dangerous city/country to live in;
- What is the most dangerous profession to be a part of;
- What is the weapon that is used the most;
- Which are the groups that claim responsibility most often;
- What is the correlation between the number of attacks they have claimed and the number of members they have.
- ISI's analysis: number of attacks they had carried out per year, the most common weapon they use, their most common target etc.



## Most popular
- The places where terrorist attacks happen most often (country, city, etc.)
- Most popular goal of the attack
- Most popular type of the attack
- The correlation between the goal and the type of the attack
- General description of targets (position, nationality...) most popular
	
## Other
- Number of attacks every year, visualise, and show a trend
- Number of casualties every year, visualise, and show a trend
- Numbers of lethal and non-lethal attacks and show them visually
- [possible, if it makes sense] Clusters of geographical locations where attacks happened, the conclusion would be where most attacks occur
- Is there a correlation between success, suicide, and/or multiple incidents (any combination of two will do, whichever makes the most sense)
## Phase 2

- Draw a map of attacks in an important area (scatter plot)
- Find the probability that you will be attacked and killed in a cerrtain city (eg. Baghdad)
- By finding probabilities find the typical attacks
- Find the city in which you are most likely to be attacked and killed
- Draw a bars stacked graph for weapons and countries
- Check if ISIS is attacking Europe more 
- Make moving averages by 5 year periodes and show than (in respect to attack, ir group)
- Try to do some regression in order to determine unknown values
- Cluster by time in order to determine if there is a corrleation between multiple attacks (not sure if this makes sense).

## Specific goals

Find more specific goals (what is the most dangerous city to live in, how is the Syria war affecting people, what about the migration crisis, groups claiming responsibility, find their characteristics, can you predict them)

- What is the most dangerous city/country to live in [what city has most attacks, what city has most casualties]
- What is the most dangerous profession to be a part of [what profession is attacked the most, what profession has the most victims]
- What is the weapon that is the most used, which is the one that has killed the most people, can we create a distribution of which weapon kills how many people (or at least a distribution of how many it's killed so far)
- Is there a correlation between the location of the attack and the type/weapon of the attack
- What are the groups that claim responsibility most often (are ISIS and Al-Qaida included)
- What is the correlation between the number of attacks they've claimed and the number of members they have [maybe clustering them would be a better option]
- Correlation between the number of members and location and type of attacks
- ISIS
	- A map of their attacks
	- Distribution of the number of attacks (do they grow over time, is the organisation expanding)
	- Have they started attacking Europe more lately (is it correlated to the migration crisis)
	- [optional]Did they cause the migration crisis (Did they attack a lot before and around the time it started)
	- Can we find a typical attack (weapon, target, location) [find what they use most often]
	- What are the chances that they'll claim responsibility if the attack had a certain weapon, target, location...[number of attacks they've claimed responsibility for / number of attacks that are typical]
- The difference between ISIS and Al-Qaida [maybe we can do this later]
	- Where they attack (Al-Qaida prefers the west)
	- What were their targets
	- The distribution of their attack weapons
	- Is there a correlation between the attacks [the times, can the places be grouped (did they both attack in Europe in the span of a few days)]
	- Typical attacks, is it the one or the other
