fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    console.log(data.results[0]);
    for (const each of data.results) {
      const newText = document.createTextNode(each.title);
      const newNode = document.createElement('li');
      newNode.appendChild(newText);
      document.querySelector('#list_movies').appendChild(newNode);
    }
  });
