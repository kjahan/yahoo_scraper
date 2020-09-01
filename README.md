# yahoo-scraper
Yahoo finance scraper

## Setup environment

```
$ conda create -n crawly python=3.7
```

```
$ conda install -n crawly BeautifulSoup4
```

```
$ conda install -n crawly requests
```

```
$ mkdir logs
```

## To activate conda environment, run:

```
$ conda activate crawly
```
(On MacOS: `unset PYTHONPATH`)


## Run yahoo scraper:

```
$ python -m src.scraper
```

## To deactivate conda environment, run:

```
$ conda deactivate
```
