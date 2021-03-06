
<p align="center">
	<a href="https://pypi.org/project/bible-male-names"><img src="https://cdn.abranhe.com/projects/bible-male-names/abraham.png" width="30%" height="30%"></a>
	<br>
	<br>
	<br>
	<a href="https://pypi.org/project/bible-male-names">bible-male-names</a>: get male names from <a href="https://www.google.com/search?q=The+Bible">The Bible</a>
</p>

<p align="center">
	<!-- Travis CI -->
	<a href="https://travis-ci.org/abranhe/bible-male-names.py"><img src="https://img.shields.io/travis/abranhe/bible-male-names.py.svg?logo=travis" /></a>
	<!-- LICENSE -->
	<a href="https://github.com/abranhe/bible-male-names.py/blob/master/license"><img src="https://img.shields.io/github/license/abranhe/bible-male-names.py.svg" /></a>
	<!-- pip Version -->
	<a href="https://pypi.org/project/bible-male-names"><img src="https://img.shields.io/pypi/v/bible_male_names.svg"></a>
	<!-- @abranhe -->
	<a href="https://github.com/abranhe"><img src="https://abranhe.com/badge.svg"></a>
	<!-- Cash me -->
	<a href="https://cash.me/$abranhe"><img src="https://cdn.abranhe.com/badges/cash-me.svg"></a>
	<!-- Patreon -->
	<a href="https://www.patreon.com/abranhe"><img src="https://cdn.abranhe.com/badges/patreon.svg" /></a>
	<!-- Paypal -->
	<a href="https://paypal.me/abranhe/10"><img src="https://cdn.abranhe.com/badges/paypal.svg" /></a>
</p>

## Install

```
$ pip install bible-male-names
```

Names from [biblegateway.com](https://www.biblegateway.com/resources/all-men-bible/Alphabetical-Order-All-Men)

## Usage

```py
import bible_male_names

print (bible_male_names.rand())
# => Abraham

print (bible_male_names.get(3))
# Felix
# Elon
# Jesus

print (bible_male_names.all())
# Aaron
# Abagtha
# ...
```

## Api

### `rand()`

> Return a random Bible male name

### `get(number)`

> Return 'number' names

### `.all()`

> Return over [2000+](https://github.com/abranhe/bible-male-names/blob/master/bible-male-names.json) male names from The Bible.


## Related

- [bible-female-names.py](https://github.com/abranhe/bible-female-names.py):  📖  get female names from The Bible
- [bible-male-names](https://github.com/abranhe/bible-male-names): same thing but in JavaScript
- [bible-female-names](https://github.com/abranhe/bible-female-names):  📖  get female names from The Bible in JavaScript

## Team

|[![Carlos Abraham Logo](https://avatars3.githubusercontent.com/u/21347264?s=50)](https://abranhe.com)|
| :-: |
| [Carlos Abraham](https://github.com/abranhe) |


## License

[MIT](https://github.com/abranhe/bible-male-names/blob/master/license) License © [Carlos Abraham](https://github.com/abranhe/)
