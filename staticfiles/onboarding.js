const scrollers = document.querySelectorAll(".scroller");

// If a user hasn't opted in for recuded motion, then we add the animation
if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  addAnimation();
}

function addAnimation() {
  scrollers.forEach((scroller) => {
    // add data-animated="true" to every `.scroller` on the page
    scroller.setAttribute("data-animated", true);

    // Make an array from the elements within `.scroller-inner`
    const scrollerInner = scroller.querySelector(".scroller__inner");
    const scrollerContent = Array.from(scrollerInner.children);

    // For each item in the array, clone it
    // add aria-hidden to it
    // add it into the `.scroller-inner`
    scrollerContent.forEach((item) => {
      const duplicatedItem = item.cloneNode(true);
      duplicatedItem.setAttribute("aria-hidden", true);
      scrollerInner.appendChild(duplicatedItem);
    });
  });
}

// Function to display the popup message
function displayPopup() {
  // Define arrays for names, countries, and prices
  var names = ["Bob", "John", "Jerry", "Henry", "Ashley", "Micheal", "Emily", "Jane", "Cherry", "David", "Samuel"];
  var countries = ["Netherlands", "USA", "Switzerland", "Canada", "United Kingdom", "Slovakia", "Sweden", "UAE", "Mexico", "South Africa", "Italy", "Spain", "France", "Germany"];
  var prices = ["$100", "$1000", "$1500", "$2000", "$500", "$250", "$300", "$1200", "$700", "$350"];

  // Generate random values for name, country, and price
  var name = names[Math.floor(Math.random() * names.length)];
  var country = countries[Math.floor(Math.random() * countries.length)];
  var price = prices[Math.floor(Math.random() * prices.length)];

  // Construct the popup message
  var popupMessage = name + " from " + country + " just deposited " + price;

  // Get the h1 element by its ID
  var popupElement = document.getElementById("popupMessage");

  // Update the content of the h1 element with the popup message
  popupElement.textContent = popupMessage;
}

// Call the displayPopup function every 5000 milliseconds (5 seconds)
setInterval(displayPopup, 5000);

// Call the displayPopup function once initially to display the first message immediately
displayPopup();