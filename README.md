# Shinobi-PMing-Tool
Un outil pour aider à l'envoi de MP en masse sur Shinobi.fr, et créer des listes d'envoi à partir du classement.

## L'outil de recherche
Permet de créer une liste de pseudos en parcourant le classement sur certains critères :
- pages du classement
- classement hebdo ou général (influe sur les pages recherchées)
- fourchette de niveau
- classement par village ou général (influe sur les pages recherchées)
- classe
- équipe
- points minimum (dépend du classement général ou hebdo)
- fourchette d'évolution du jour
\nAffiche la liste dans l'outil et l'enregistre dans le fichier dont on a précisé le nom.

## L'outil d'envoi de MP
/!\ Cet outil n'est accessible qu'avec la bonne configuration. Me contacter. /!\\

On entre les destinataires (un par ligne - potentiellement récupérés avec l'outil recherche), le sujet du MP, le contenu, on entre les identifiants du compte servant à envoyer le MP et on envoie !

Facile, rapide et pas cher.

La variable %pseudo% est remplacée par le pseudo du destinataire à l'envoi dans le titre comme dans le corps du message. Cool non ?

## Le filtrage de la liste d'envoi
Le fichier "Ennemis.txt" permet de préciser des pseudos qui, s'ils s'ont inclus dans la liste d'envoi du MP, ne recevront quand même pas le MP.

Il faut entrer à la main les pseudos dans le fichier, en mettant un pseudo par ligne (comme pour la liste des destinataires dans "Destinataires.txt").

## Téléchargement
Télécharger la dernière [release](https://github.com/Kaoline/Shinobi-PMing-Tool/releases), dézipper et lancer le .exe.