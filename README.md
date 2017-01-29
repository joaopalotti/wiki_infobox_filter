# Wiki Infobox Filter

How about going through all wikipedia articles in a xml dump and filtering the ones that contain a pre-defined set of keywords in their infobox?

That's the aim of this small project.

## USING

Edit keywords.def as you need and them run parser.py with the Wikipedia xml dump that you wish. Example:

``` bash
>> python parser.py dump-simplewiki-example.xml > titles.txt
```

Afterwards, you can download the pages (articles) from any wiki language using "download_pages.py".

``` bash
>> mkdir downloaded_pages
>> python download_pages.py titles downloaded_pages
```

Alternatively, you can modify parser.py to extract from the dumps the content of the files you wish to save.
I am doing that in two steps because I need to access different wikipedia, but your needs surely will differ from mine.


## MISSING:

1. Tests
2. I should avoid asking users to modify the first line of dumps.

