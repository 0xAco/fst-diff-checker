# FST differentation checker

C'est un petit programme utilitaire pour vérifier si les données sont significatives aux seuils 95%, 99% et 99,9%.

## Utilisation

> Pour lancer le programme, il faut avoir [python3](https://www.python.org/downloads/) d'installé.

Pour fonctionner, ce script a besoin de quelques fichiers. Ils doivent tous être au format `.csv` avec comme séparateur "**;**". Des exemples sont disponibles dans le dossier `data/`.

### Comment lancer le programme ?
1. ouvrir un terminal
2. se placer dans le répertoire du fichier `.py`
3. exécuter la commande ci-dessous

```sh
./fst-diff-check.py <SNP-file> <95LL> <95UL> <99LL> <99UL> <999LL> <999UL>
```

en remplaçant les valeurs entre chevrons par les chemins vers les fichiers correspondants. Voici à quoi ils correspondent :
- `SNP-file`: les différenciations mesurées
- `95LL` et `95UL`: respectivement les limites basses et hautes pour le seuil 95%
- `99LL` et `99UL`: idem pour le seuil 99%
- `999LL` et `999UL`: idem pour le seuil 99.9%

> [!NOTE] L'ordre des fichiers est important et vérifier que le formattage csv est bon (aucun test n'est effectué en guise de vérification)

### Exemple
```sh
python3 ./fst-diff-check.py ./data/SCO/PectenSNPs-HWE-PairwiseFst-SCO.csv ./data/SCO/SCO_FST_q95_LL.csv ./data/SCO/SCO_FST_q95_UL.csv ./data/SCO/SCO_FST_q99_LL.csv ./data/SCO/SCO_FST_q99_UL.csv ./data/SCO/SCO_FST_q999_LL.csv ./data/SCO/SCO_FST_q999_UL.csv
```
la réponse générée ressemblera alors à :
```txt
ARM<>DNZ ns
ARM<>ELO ns
ARM<>MOX ns
ARM<>ROS ns
AUB<>CAM ns
AUB<>DNZ ns
AUB<>ELO ns
AUB<>MOX ns
AUB<>ROS ns
CAM<>DNZ ns
CAM<>ELO ns
CAM<>MOX ns
CAM<>ROS ns
DNZ<>ELO ns
DNZ<>MOX ns
DNZ<>ROS ns
ELO<>MOX ns
ELO<>ROS ns
MOX<>ROS ns
```

> `ARM<>SNZ` représente la différenciation entre les sites ARM et SNZ. Ici, les valeurs sont non significatives (ns)

Voici les valeurs attendues en fonction de quels seuils sont atteints:
- `ns` si la valeur mesurée rentre dans le seuil **95%**
- `*` si la valeur sort des **95%** mais pas des **99%**
- `**` si la valeur sort des **99%** mais pas des **99.9%**
- `***` si la valeur sort des **99.9%**

### Export au format csv
Une fois les valeurs calculées, un fichier `diff-check.csv` est généré à la racine du dossier.

Voilà des bisous