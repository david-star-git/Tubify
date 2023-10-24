# Tubify

## Sprachversionen
[![Englisch](https://img.shields.io/badge/Englisch-English-blue)](readme.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-German-blue)](readme_de.md)
[![Spanisch](https://img.shields.io/badge/Español-Spanish-blue)](readme_es.md)

## Zusammenfassung

Tubify ist ein Python-basiertes Dienstprogramm, mit dem Benutzer sowohl mit Spotify als auch mit YouTube arbeiten können. Dies ermöglicht das Abrufen und Herunterladen von Songlisten aus Spotify-Playlists sowie das Herunterladen von Audiodateien aus YouTube-Playlists oder -Videos. Es ist ein vielseitiges Werkzeug für Musikliebhaber, die offline Sammlungen ihrer Lieblingssongs erstellen möchten.

## Praktische Anwendungen

In einer Welt, in der Musik ein wesentlicher Bestandteil unseres Lebens ist, bietet unser Dienstprogramm eine kostengünstige Alternative, um Ihre Lieblingstitel ohne die Notwendigkeit von Premium-Abonnements zu genießen. Hier sind einige praktische Anwendungen:

- **Offline-Hören**: Sie können Ihre bevorzugten Songs direkt auf Ihrem Gerät speichern und so auf eine ständige Internetverbindung verzichten sowie den Datenverbrauch reduzieren.

- **Persönliche Sammlungen**: Erstellen Sie Ihre eigene personalisierte Sammlung von Songs aus verschiedenen Plattformen, um sie offline zu genießen. Schluss mit Streaming-Diensten mit begrenzter Verfügbarkeit.

- **Backup und Redundanz**: Behalten Sie eine Sicherungskopie Ihrer geschätzten Musik, falls sie jemals von den Streaming-Plattformen entfernt oder nicht mehr verfügbar wird. Ihre Musik, Ihre Kontrolle.

- **Werbefreies Erlebnis**: Verabschieden Sie sich von Unterbrechungen durch Werbung während Ihrer Musiksitzungen. Heruntergeladene Musik bedeutet ein ununterbrochenes Hörerlebnis.

- **Individuelle Mixtapes**: Erstellen Sie Ihre eigenen individuellen Mixtapes oder Wiedergabelisten, indem Sie Ihre Lieblingstitel auswählen und sie nach Ihren Wünschen organisieren.

Unser Dienstprogramm ermöglicht es Ihnen, die Kontrolle über Ihr Musikerlebnis zu übernehmen und bietet eine flexiblere und personalisiertere Möglichkeit, Musik nach Ihren eigenen Vorstellungen zu genießen.

## Anleitung

1. **Voraussetzungen**:
   - Installiertes Python auf Ihrem System.
   - Installation der erforderlichen Bibliotheken: `spotipy`, `youtubesearchpython`, `pytube` und `moviepy`.

2. **Beschaffung von API-Zugangsdaten**:
   - Wenn Sie die Spotify-Funktionalität nutzen möchten, müssen Sie Zugangsdaten für die Spotify-API beschaffen.
   - Bei der Arbeit mit YouTube benötigen Sie keine API-Schlüssel.

3. **Konfiguration der API-Zugangsdaten**:
   - Um die Spotify-Funktionalität zu nutzen, müssen Sie Zugangsdaten für die Spotify-API erhalten, darunter eine **Client-ID** und ein **Client-Secret**. Befolgen Sie diese Schritte, um sie zu erhalten:

     1. **Erstellen eines Spotify-Entwicklerkontos**:
        - Besuchen Sie die [Spotify for Developers](https://developer.spotify.com/dashboard/) Website.
        - Melden Sie sich an oder erstellen Sie ein Spotify-Konto, wenn Sie noch keines haben.

     2. **Erstellen einer neuen Spotify-App**:
        - Nach dem Einloggen gehen Sie zum Spotify Developer Dashboard.
        - Klicken Sie auf die Schaltfläche "App erstellen" oder "Client-ID erstellen".
        - Geben Sie die erforderlichen Informationen für Ihre App ein, wie den Namen und die Beschreibung.
        - Möglicherweise werden Sie aufgefordert, den Entwicklerbedingungen zuzustimmen.

     3. **Erhalt Ihrer Zugangsdaten**:
        - Nachdem Sie die App erstellt haben, erhalten Sie eine **Client-ID** und ein **Client-Secret**.
        - Ersetzen Sie `YOUR_SPOTIFY_CLIENT_ID` und `YOUR_SPOTIFY_CLIENT_SECRET` im Code durch die erhaltenen Zugangsdaten.

   - Wenn Sie das Dienstprogramm ausschließlich für Aufgaben im Zusammenhang mit YouTube verwenden, können Sie diesen Schritt überspringen, da die Funktionalität von YouTube keine API-Zugangsdaten erfordert.

4. **Ausführung des Werkzeugs**:
   - Führen Sie das Python-Skript aus.
   - Sie werden aufgefordert, eine Spotify- oder YouTube-Playlist-URL einzugeben.
   - Das Dienstprogramm erkennt den Typ der URL und führt die entsprechende Aktion aus:
     - Für Spotify-Playlists werden Songtitel abgerufen und von YouTube heruntergeladen.
     - Für YouTube-Playlists wird der Ton von jedem Video heruntergeladen.
     - Für YouTube-Videos wird der Ton direkt heruntergeladen.

5. **Ergebnis**:
   - Die Songs oder Audiodateien werden im angegebenen Verzeichnis (`save_directory`) gespeichert.

6. **Genießen Sie es**:
   - Sie können Ihre heruntergeladene Musik jetzt offline oder für jeden anderen Zweck genießen.

## Hinweis

- Beachten Sie die Nutzungsbedingungen und Urheberrechtsbeschränkungen beim Herunterladen von Inhalten von Online-Plattformen wie Spotify und YouTube. Respektieren Sie die Rechte der Content-Ersteller und beachten Sie alle gesetzlichen Vorschriften.

## Lizenz

Dieses Projekt steht unter der [GNU General Public License, Version 3.0](LICENSE). Den vollständigen Lizenztext finden Sie [hier](https://www.gnu.org/licenses/gpl-3.0.html).
