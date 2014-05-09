InvoiceManager
==============

I was working on my own invoice manager, as I did not find any software that did what I needed and was open source. I have since abandoned this project, so don't expect any updates to this repository, unless I have way too much time.

I put the code up anyway as it may serve as a viable basis for others to write their programs, and because I liked some of the things I wrote, like the dynamic generation of data types (see [data/datatype.py](https://github.com/malexmave/python-invoice-manager/blob/development/data/datatype.py), or [the related blog post](https://blog.velcommuta.de/2014/dynamically-generating-data-types-in-python/)).

# Branches
The standard branch of this project is "development". There is also another branch containing code for dynamic generation of SQLite interfaces for the data types, which generally works but contains failing tests, as the dynamic tests do not take foreign key constraints into account.

# Dependencies
* [nose](https://nose.readthedocs.org/en/latest/)

# License
[BSD 2-clause license](https://github.com/malexmave/python-invoice-manager/blob/development/LICENSE)
