
<p align="center">
	<a href="https://pypi.org/project/bible_male_names"><img src="https://cdn.abraham.gq/projects/bible-male-names/abraham.png" width="30%" height="30%"></a>
	<br>
	<br>
	<br>
	<a href="https://pypi.org/project/bible_male_names">bible_male_names</a>: get male names from <a href="https://www.google.com/search?q=The+Bible">The Bible</a>
</p>

<p align="center">
	<!-- Travis CI -->
	<a href="https://travis-ci.org/abranhe/bible-male-names.py"><img src="https://img.shields.io/travis/abranhe/bible-male-names.py.svg?logo=travis" /></a>
	<!-- LICENSE -->
	<a href="https://github.com/abranhe/bible-male-names.py/blob/master/LICENSE"><img src="https://img.shields.io/github/license/abranhe/bible-male-names.py.svg" /></a>
	<!-- pip Version -->
	<a href="https://pypi.org/project/bible-male-names"><img src="https://img.shields.io/pypi/v/bible_male_names.svg"></a>
	<!-- @abranhe -->
	<a href="https://github.com/abranhe"><img src="https://abranhe.com/badge.svg"></a>
	<!-- Cash me -->
	<a href="https://cash.me/$abranhe"><img src="https://cdn.abraham.gq/badges/cash-me.svg"></a>
	<!-- Patreon -->
	<a href="https://www.patreon.com/abranhe"><img src="https://cdn.abraham.gq/badges/patreon.svg" /></a>
	<!-- Paypal -->
	<a href="https://paypal.me/abranhe/10"><img src="https://cdn.abraham.gq/badges/paypal.svg" /></a>
</p>
</p>

# Install

```
$ pip install bible_male_names
```

Names from [biblegateway.com](https://www.biblegateway.com/resources/all-men-bible/Alphabetical-Order-All-Men)

# Usage

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

# API

**rand()**

> Return a random Bible male name

**get(number)**

> Return 'number' names

**.all()**

>Return over [2000+](https://github.com/abranhe/bible-male-names/blob/master/bible-male-names.json) male names from The Bible.


# Team

|[![Carlos Abraham Logo](https://avatars3.githubusercontent.com/u/21347264?s=50&v=4)](https://19cah.com)|
| :-: |
| [Carlos Abraham](https://github.com/abranhe) |

# Related

- [bible-male-names](https://github.com/abranhe/bible-male-names): same thing but in **JS**
- [bible-female-names](https://github.com/abranhe/bible-female-names):  📖  get female names from The Bible in JS


# License

[MIT](https://github.com/abranhe/bible-male-names/blob/master/LICENSE) License © [Carlos Abraham](https://github.com/abranhe/)
