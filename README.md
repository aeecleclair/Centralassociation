# Centralisation

Le site Web Centralassociation sert d’agrégateur de liens pour les Centraliens : sur cette même page sont centralisés les liens vers les réseaux sociaux de chaque association de l'école.


## Le projet

La page principale est générée automatiquement par un script `Python` (3.9) et utilise la librairie `Jinja2` pour automatiser l'écriture du `html`. Une documentation complète de la librairie est disponible sur le site officiel. Cependant, notre projet emploie uniquement les fonctionnalités de base.

Le choix d'une génération automatique s'explique par la redondance du code HTML de la page et dans l'ambition de faire un projet clair, facilement compréhensible et modifiable.

Pour faire bref :

- Les différents liens, leurs noms et descriptions sont écrits au format `YAML` dans le fichier [assos_links.yaml](./assos_links.yaml).
- Le script Python `build.py` lit le fichier YAML et construit la page HTML à partir de celui-ci.
- Le fichier final est enregistré dans le dossier `./dist` aux côtés des feuilles de styles CSS et des images.


## Environnement de compilation

Pour mettre à jours le site, clonez le projet sur votre PC.

```bash
git clone https://github.com/aeecleclair/Centralassociation.git
```

Déplacez-vous dans le dossier du projet

```bash
cd ./centralassociation
```

Modifiez le fichier `assos_links.yaml` à votre guise.

Pour construire la page il faut exécuter le script Python. Assurez-vous d'avoir `Python3.9` où supérieur installé avec la librairie `Jinja2` et `PyYAML`. L'utilisation d'un environnement virtuel avec [Poetry](https://python-poetry.org/) permet d'installer ces éléments.

## Compilation

Avec Poetry :

```bash
poetry run python ./build.py
```

Sinon simplement,

```bash
python ./build.py
```

Récupérer le résultat dans le dossier `./dist`

## Docker
[! TODO: Change process]
Pour faciliter le déploiement, une image docker est fournie. Pour créer l'image : `docker build -t centralisation .` et créer le conteneur `docker run -it -d -p 80:80 centralisation`.

Un fichier `docker-compose.yml` peut être édité :

```yml
version: "3"
services:
  web:
    image: centralisation
    container_name: centralisation
    restart: unless-stopped
    ports:
      - "80:80"
```
