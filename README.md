Gruppuppgift: Bygg ett API i Flask eller FastAPI
Krav
API:t ska:
Kommunicera data via JSON.
Ha endpoints för minst två av följande HTTP-verb: GET, POST, PUT, DELETE.
Varje endpoint ska kunna returnera HTTP-responser både vid misslyckande och framgång, t.ex.,
200, 422, 404.
Detta kan hanteras både manuellt och/eller med inbyggda verktyg.
Vara väl dokumenterat/kommenterat.
Förslag på Projekt
Gruppen får själva bestämma vad API:et ska vara till för, men här kommer några förslag:
1. Bokningssystem för Klassrum
Beskrivning: Bygg ett API där elever kan boka klassrum. Funktioner:
Lista tillgängliga klassrum baserat på tid och datum.
Boka ett klassrum.
Avboka eller ändra bokningar.
2. Recepthanteringssystem
Examensuppgifter.md 2024-10-23
2 / 2
Beskrivning: Skapa en applikation där användare kan lägga till, söka efter och spara recept. Funktioner:
Användare kan skapa och uppdatera recept med ingredienser och steg.
Söka efter recept baserat på ingredienser och kategori (t.ex., frukost, middag, dessert).
Möjlighet för användare att betygsätta och recensera recept.
3. Enkel Bloggplattform
Beskrivning: Skapa en bloggplattform där användare kan skapa inlägg, läsa andras inlägg och kommentera
dem. Funktioner:
Användare kan skapa ett konto, logga in och skapa blogginlägg.
Lista och visa blogginlägg från alla användare.
Kommentarsfunktion för inlägg (kommentarer ska också ha CRUD-funktionalitet)