document.getElementById('add_item').addEventListener('click', () => {
  const newElement = document.createElement('li');
  const newText = document.createTextNode('Item');
  newElement.appendChild(newText);
  const myList = document.querySelector('.my_list');
  myList.appendChild(newElement);
})