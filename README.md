# Article Recommender

The goal of this project is to learn how to make a simple article recommendation engine using a semi-recent advance in natural language processing called word2vec (or just word vectors). In particular, I've used Stanford's GloVe vectors trained on a dump of Wikipedia.

Around the recommendation engine, I've built a web server that displays a list of BBC articles for URL http://localhost:5000 (testing) or whatever the IP address is of server (deployment).

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles.
