/*
const myHeading = document.querySelector('h3'); // Storing reference to h3 element
myHeading.textContent = "Hello World!";

// Provides pop-up box at top of page
// alert(myHeading.textContent);

function multiply(a, b) {
  return a * b;
}

console.log(multiply(2, 3));
console.log(multiply(50, 600));
console.log(multiply(3, 3));

const entirePage = document.querySelector('html');
entirePage.addEventListener('click', () => {alert("Ouch! Stop poking me, you nitwit!")});
*/

const myImage = document.querySelector('img');

myImage.addEventListener('click', () => {
  const address = myImage.getAttribute('src');
  if (address === "images/Peach_brand_design.PNG") {
    myImage.setAttribute('src', "images/Peachy_Pink.png");

  } else {
    myImage.setAttribute('src', "images/Peach_brand_design.PNG")
  }
});

let myButton = document.querySelector('button');
let myHeader = document.querySelector('h3');

if (localStorage.getItem('name')) {
  localStorage.removeItem('name');
}

function setUserName() {
  let myName = prompt("What's your ding dang name?");
  if (!myName) {
    setUserName();

  } else {
    localStorage.setItem('name', myName);
    myHeader.textContent = `Mozilla ain't cool, ${myName}`;
  }
}

if (!localStorage.getItem('name')) {
  setUserName()

} else {
  myHeader.textContent = `Mozilla ain't cool, ${localStorage.getItem('name')}`;
}

myButton.onclick = () => setUserName();