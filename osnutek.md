# Draft

The definition of our goals realised in `README.md` and `Appendix.md` files follows.

## Description of the data set

Our team chose **Global Terrorism** as a topic of this project. We are going to work with the *Global Terrorism Database* which can be found at the following link: [https://www.kaggle.com/START-UMD/gtd](https://www.kaggle.com/START-UMD/gtd)

The database is given in ***CSV*** (comma-separated values) format, where each line of the file is a data record and information are separated by commas.

The data set contains the information for over 150 000 terrorist attacks that have occurred around the world between 1970 and 2015 (except for 1993). It contains above 100 attributes describing the attacks. Often, more than one attribute is used to describe the same variable.

For example, there are 4 attributes used in order to determine the date when the attack occurred, the day, month, and year of the attack, and in case these are absent an approximate date.

As well as this we have 2 attributes used to express the length of the attack, one of them - `extended`, expresses whether the attack lasted for more than 24 hours, `resolution` shows the date when the situation (attack, hostage situation) ended.

Also, we have a wide variety of attributes explaining the place where the event occurred, for example, country, region, city, latitude and longitude. As well as these attributes explaining whether the incident occurred in the city itself or in its vicinity, and the specificity, described as follows:

- 1 = event occurred in city/village/town and lat/long is for that location;
- 2 = event occurred in city/village/town and no lat/long could be found, so coordinates are for the centroid of smallest sub-national administrative region identified;
- 3 = event did not occur in city/village/town, so coordinates are for the centroid of smallest sub-national administrative region identified;
- 4 = no 2nd order or smaller region could be identified, so coordinates are for the centre of 1st order administrative region;
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

`nwound` - number of people injured non-fatally in the incident, `nwoundus` - number of US citizens injured non-fatally in the incident.

`nwoundtex` - number of perpetrator injuries.

`property` - whether the incident resulted into property damage, `propvalue` - the value of the damage.

`ishostkid` - whether there were hostages and `nhostkid` - number of hostages, sparse, `nhostkidus` - US hostages.


There are multiple attributes concerning ransom for hostages, how much was asked, how much was given. As well as this, the outcome of the kidnapping, how many people survived, etc. Then, there is a group of attributes concerning whether the attack was carried out internationally or domestically.


## Goals for our project

### Main goals
In the main goals of our projects belong the following:

- Number of attacks per year, visualise, and show a trend;
- Number of casualties every year, visualise, and show a trend;
- Numbers of lethal and non-lethal attacks and show them visually;
- Show a map of geographical locations where attacks happened, visualise where most attacks occurred;
- Find the probability that you will be attacked and killed in a certain city (eg. Baghdad);
- Find the city in which you are most likely to be attacked and killed;
- Analysis about Europe: chances of being in an attack, chances of being killed in an attack and using linear regression predict the number of attacks in the next 5 years;
- Analysis of Western and Eastern Europe: number of attacks per year in each, find the probability (chances) of being in an attack in each, as well as probability to be killed.

Results for the above goals can be found in the main Report - `README.md` file.

### Additional goals
There are also additional goals that we have set which helped for the main goals and here belong the following:

- Correlation between success, suicide attacks (dependence of an attack being the one or another);
- What is the most dangerous city/country to live in according to number of attacks and according to number of victims, respectively;
- Top 10 countries with most victims and top 10 most attacked countries;
- What is the most dangerous profession to be a part of - top 10 most attacked professions, as well as killed;
- What is the weapon that is used the most and respectively that has killed the most;
- Which are the most common types of attacks;
- Which are the most deadliest types of attacks;
- Which are the groups that claim responsibility most often for the attacks and which are the ones that claim responsibility most often for the lives;
- Is there a dependency between the number of attacks they have claimed and the number of members they have;
- List of all the countries with corresponding number of attacks for each, needed for producing the map of all countries;
- ISI's analysis: number of attacks they had carried out per year, the most common weapon they use, their most common target;
- Other more popular terrorist organizations analysis.

Results for the above goals can be found in the additional - `Appendix.md` file.

### Conclusion

Analysing the above goals we can easily conclude what is the most dangerous city/country to live in, what is the most dangerous profession to be a part of, what is the weapon that is the most used, which is the one that has killed the most people, the most "popular" terrorist groups. Knowing this information we can think of where to move next and how risky it is for us to visit a certain country/region.