// var algoliasearch = require('algoliasearch');
// var algoliasearch = require('algoliasearch/reactnative');
// var algoliasearch = require('algoliasearch/lite');
// import * as algoliasearch from 'algoliasearch'; // When using TypeScript

// or just use algoliasearch if you are using a <script> tag
// if you are using AMD module loader, algoliasearch will not be defined in window,
// but in the AMD modules of the page

var client = algoliasearch('4RL7NRE3A4', '25445a8c9a3f15d6bc4c7718d8b452c9');
var index = client.initIndex('article');
var articleJason = require('./article.json');

index.addObjects(articleJason, function(err, content) {
  if (err) {
    console.error(err);
  }
});
