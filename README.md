# Article Recommender

The goal of this project is to learn how to make a simple article recommendation engine using a semi-recent advance in natural language processing called word2vec (or just word vectors). In particular, I've used Stanford's GloVe vectors trained on a dump of Wikipedia.

Around the recommendation engine, I've built a web server that displays a list of BBC articles for URL http://localhost:5000 (testing) or whatever the IP address is of server (deployment).

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles.

## Data :
- BBC articles corpus which is present in the repo

## Technique :
- Two words are related if their word vectors are close in 300 dimensional vector space. Similarly, if we compute the centroid of a document's cloud of word vectors, related articles should have centroids close in 300 dimensional vector space. Words that appear frequently in a document push the centroid in the direction of that word's vector. The centroid is just the sum of the vectors divided by the number of words in the article. Given an article, we can compute the distance from its centroid to every other article's centroid. The article centroids closest to the article of interest's centroid are the most similar articles. Surprisingly, this simple technique works well as you can see from the examples above.

## Result :
- Using the technique I calculate closest 5 articles to the current article and recommend them to the user.
