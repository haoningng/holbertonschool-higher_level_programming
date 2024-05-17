const header = document.querySelector('header');
header.classList.add('red');
const toggleHeader = document.getElementById('toggle_header');
toggleHeader.addEventListener('click', () => {
  header.classList.toggle('green');
});