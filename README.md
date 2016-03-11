# Classifier protopye

This python tool aims to help you identify papers based on your interest. Via a small gui you can select papers from a shortlist, which will get fed into a machine learning system (in our case a neural net), which will learn your interests. It does so by comparing features of a paper (some metadata like authors, title, journal, keywords, and features extracted by ContentMine tools such as species counts). At the end it hopefully helps you in discovering papers relevant to you in the large corpus you collected.

## Dependencies

To your virtualenv add:

* [pycproject](https://github.com/ContentMine/pyCProject/)
	* which in turn requires `pip install Image`
* [word_cloud](https://github.com/amueller/word_cloud)
* [pybrain](https://github.com/pybrain/pybrain)
