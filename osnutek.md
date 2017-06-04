# Draft

The definition of our goals realised in `README.md` and `Appendix.md` files follows.

## Description of the data set

Our team chose **Global Terrorism** as a topic of this project. We are going to work with the *Global Terrorism Database* which can be found at the following link: [https://www.kaggle.com/START-UMD/gtd](https://www.kaggle.com/START-UMD/gtd)

The database is given in ***CSV*** (comma-separated values) format, where each line of the file is a data record, and information is separated by commas.

The data set contains the information for over 150 000 terrorist attacks that have occurred around the world, between 1970 and 2015 (except for 1993). It contains above 100 attributes describing the attacks. Often, more than one attribute is used to describe the same variable. For example, there are 4 attributes used in order to determine the date when the attack occurred, the day, month, and year of the attack, and in case these are absent an approximate date. As well as this we have 2 attributes used to express the length of the attack, one of them - `extended`, expresses whether the attack lasted for more than 24 hours, `resolution` shows the date when the situation (attack, hostage situation) ended.

We have a wide variety of attributes explaining the place where the event occurred, for example, country, region, city, latitude and longitude. As well as these attributes explaining whether the incident occurred in the city itself or in its vicinity, and the specificity, described as follows:

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

As terrism has been discussed as a problem more and more lately, we have tried to focus on things of importance, i.e. things that we, as regular people, would like to know about terrorism. As a result we have focused on a couple of different things.

We have looked at the world as a whole and researched whether the number of attacks on a global scale has been rising recently. As well as this, we have researched which countries are most susceptible to terrorist attacks. We have tried to find what the most dangerous city on Earth is, as well as what the chances of being killed of one has been in an attack are.
Because of the simple reason that we live in Europe, we were interested in its relationship with terrorism. More and more attacks are being reported every year, we wanted to know whether indeed, there are more attacks in Europe. As well as this, we were interested which is the most dangerous country in Europe, and what the chances of being in an attack are.
We hear the names of certain terroristic groups in the news constantly. We were interested in whether these groups were the ones that carried out most attacks.
