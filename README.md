# Mökkilaskuri
Tällä nettisivlla voidaan laskea mökkireissun maksujako ihmisten välillä. Sivusto on vielä hyvin kesken eräinen.
Osoite: https://mokkilaskuri.herokuapp.com/

## Laskurit:

### Keskiarvo:
Tällä voidaan laskea nopeasti ja vaivattomasti monen eri päivän mökkireisuun maksujakauma, vaikka jotkin reisuun lähtijät olisivatkin
eri päivinä/öinä mukana.

Miinus puolena on, että maksu ei jokaiselle ole välttämättä oikea summa. Jos esim kahdella eri päivällä on eri määrä porukkaa, laksuri ei osaa antaa oikeaa tulosta
eri päivänä oleville. Eli ne jotka ovat viettävät vähemmän aikaa mökillä, joutuvat maksamaan hieman enemmän kuin taas ne jotka ovat kauemmin maksavat hieman vähemmän kuin pitäisi.
Tämä on usein vain muutamia senttejä korkeintaan pari euroa. Riippuu tosin paljon öiden määrästä ja miten ihmiset jakaantuvat eripäivillä.  
Jos kaikki olisivat koko mökkiajan, niin tämä laskuri antaa oikean tuloksen nopeasti.

### Tarkkaosuus:
Tämä laskuri on vielä kesken. Mutta laskuri pyytää jokaisen ihmisen tulo- ja lähtöpäivän sekä nimimerkin. Laskuri laskee jokaiselle oikean summan mitä joutuu maksamaan, ja näin kukaan ei joudu maksamaan ylimääräistä tai maksa liian vähän muihin verrattuna. Miinuksena on, että jos tulee paljon porukkaa, pitää jokaisen ihmisen läsnäolopäivät merkata tarkkaan laskuriin.
  
  
  
Molemmat laskurit eivät kuitenkaa "hävitä" rahaa oikeasta summasta. Eli kaikkien ihmisten yhteissumma on oikea mökin hinta.

## Muuta:
Nettisivu ei valitettavasti toimi (ainakaan tällähetkellä) ilman, että Javascripti on pistetty pois päältä. Laskenta tapahtuu dynaamisesti, kun käyttäjä syöttää tietoja.
Laskut tapahtuvat Javascriptillä.
Nettisivujen siirtymät on toteutettu Pythonia ja Flaskia käyttämällä. Nettisivun isännöi Heroku.com  

Jatkokehitys ideana on, että voidaan tallentaa Tarkkaosuus laskurin tulokset ylös, mutta vain itselle näkyviksi. Tämä voisi toimia, että se tallenetaan evästeisiin tai Herokuun SQL tietokantaa käyttäen, jolloin kyllä tarvittaisiin myös sivulle jonkinlainen kirjautumis toiminto.
