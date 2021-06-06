# A fond la forme tul

![Screenshot du programme](.github/images/screenshot.png)

Ce projet est réalisé dans le cadre d'un cours dispensé en semestre 9 à l'[Ecole Nationale d'Ingénieurs de Tarbes](https://www.enit.fr/)
Projet permettant de gérer une compétition d'épreuves combinnées outdoor. Les épreuves implementées sont :
- Décathlon (10 épreuves)
- Heptathlon (7 épreuves)

## Configuration requise
- Sytème de la famille UNIX (Windows non supporté)
- [Python 3.9](https://www.python.org/downloads/) minimun

## Installation
Pour installer le logiciel, il faut d'abord installer les modules *pip*. Il est recommandé d'utiliser un environnement virtual type *virtualenv*.
```
pip install -r requirements.txt
```

Pour installer les compétitions pré-installées, il faut créer un dossier *storage* et excécuter le script *data.py*
```
mkdir storage
python data.py
```

## Modules utilisés
- [prettytable](https://pypi.org/project/prettytable/) par Luke Maurits
- [simple-term-menu](https://pypi.org/project/simple-term-menu/) par Ingo Meyer
- [wcwidth](https://pypi.org/project/wcwidth/) par Jeff Quast