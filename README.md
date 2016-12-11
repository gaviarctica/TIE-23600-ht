# TIE-23600-ht

## Suunnitelma:
Luodaan palvelu, joka etsii tietoa videopeleistä Steam-palvelun rajapinnasta sekä tarjoaa peleistä lisätietoa ainakin hakemalla niihin liittyviä videoita Youtube-palvelusta. Mahdollisesti haetaan lisätietoa myös esimerkiksi Reddit-keskustelujen muodossa. 

### Ryhmän jäsenet:
* Teemu Kuikka, teemu.kuikka@student.tut.fi
* Toni-Erik Martin, toni-erik.martin@student.tut.fi

<br>

**Järjestelmä löytyy Herokusta osoitteella:** https://sgif.herokuapp.com/

<br>

<h1> Järjestelmän REST-rajapinta </h1>

<h2> /api/search?q={string} </h2>
* HTTP: GET
* Argumentit: <br>
**q**: Haetun Steam-pelin ID
* Palauttaa listan tuloksista, joita löytyy q:n perusteella JSON-muodossa.
* Esimerkki: /api/search?q=my%20summer%20car
```
[
	{
		"appid": 516750,
		"name": "My Summer Car"
	}
]
```
* Virheellisellä syötteellä palauttaa virheselitteen JSON-muodossa
* Esimerkki: /api/search?q=
```
{
	"message": "No query string was given! Use argument 'q' to assign a query string.",
	"success": false
}
```

<h2> /api/game?appid={int}&videos={int}&discussions={int}</h2>

* HTTP: GET
* Argumentit: <br>
	**appid**: Haetun Steam-pelin ID <br>
	**videos** (*valinnainen*): Haettavien peliin liittyvien Youtube-videoiden lukumäärä, oletusarvo = 0 <br>
	**discussions** (*valinnainen*): Haettavien peliin liittyvien Reddit-keskustelujen lukumäärä, oletusarvo = 0
* Palauttaa appid:ta vastaavan pelin tiedot JSON-muotoisena. Lisäksi palauttaa peliin liittyviä videoita ja keskusteluja riippuen valinnaisista argumenteista.
* Esimerkki: /api/game?appid=10&discussions=1&videos=2
```
{
	"success": true,
	"gameId": "10",
	"gameName": "Counter-Strike",
	"gameDescription": "Play the world's number 1 online action game. Engage in an incredibly realistic brand of terrorist warfare in this wildly popular team-based game. Ally with teammates to complete strategic missions. Take out enemy sites. Rescue hostages. Your role affects your team's success. Your team's success affects your role.",
	"gamePrice": 249,
	"gameImage": "http://cdn.akamai.steamstatic.com/steam/apps/10/header.jpg?t=1447887426",
	"gameDevelopers": [
		"Valve"
	],
	"gamePublishers": [
		"Valve"
	],
	"gameGenres": [
		"Action"
	],
	"gameCategories": [
		"Multi-player",
		"Valve Anti-Cheat enabled"
	],
	"videoIDs": [
		"-kkEj4rI2t8",
		"5Cjrp23lBSM"
	],
	"redditDiscussions": [
		{
			"url": "https://www.reddit.com/r/GlobalOffensive/comments/5ebwcz/i_play_csgo_with_one_hand/",
			"permalink": "/r/GlobalOffensive/comments/5ebwcz/i_play_csgo_with_one_hand/?ref=search_posts",
			"subreddit": "GlobalOffensive",
			"title": "I Play CSGO with One Hand"
		}
	]
}
```
* Virheellisellä syötteellä palauttaa virheselitteen JSON-muodossa
* Esimerkki: /api/game?appid=8&discussions=1&videos=2
```
{
	"message": "Game was not found with this appid!",
	"success": false
}
```

<h2> /api/history/popular?count={int} </h2>
* HTTP: GET
* Argumentit: <br>
	**count** (*valinnainen*): Palautettavien suosittujen pelihakujen lukumäärä. Oletusarvo = 5
* Palauttaa listan tämän palvelun suosituimmista pelihauista JSON-muodossa.
* Esimerkki: /api/history/popular?count=2
```
[
	{
		"appid": 10,
		"searchCount": 58,
		"name": "Counter-Strike"
	},
	{
		"appid": 570,
		"searchCount": 26,
		"name": "Dota 2"
	}
]
```
* Virheellisellä syötteellä palautetaan oletusarvon mukainen määrä tuloksia.

<h2> /api/history/recent?count={int} </h2>
* HTTP: GET
* Argumentit: <br>
	**count** (*valinnainen*): Palautettavien suosittujen pelihakujen lukumäärä. Oletusarvo = 5
* Palauttaa listan tässä palvelussa viimeisimmäksi tehdyistä pelihauista JSON-muodossa.
* Esimerkki: /api/history/recent?count=2
```
[
	{
		"appid": 10,
		"name": "Counter-Strike"
	},
	{
		"appid": 48000,
		"name": "LIMBO"
	}
]
```
* Virheellisellä syötteellä palautetaan oletusarvon mukainen määrä tuloksia.
