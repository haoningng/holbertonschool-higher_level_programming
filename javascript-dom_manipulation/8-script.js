fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(res => res.json())
  .then(data => {
    document.getElementById('hello').textContent = data.hello;
  })