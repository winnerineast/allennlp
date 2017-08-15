// Initialize Syntax Highlighting
hljs.initHighlightingOnLoad();

// Add Selected class to nav link that matches page ID
let pageId;

function matchPage(e) {
  if (e.getAttribute("data-page") === pageId) {
    e.classList.add("nav__link--selected");
  }
}

const navLinks = Array.prototype.slice.call(document.querySelectorAll("header nav li[data-page]"));
if (document.body.hasAttribute("data-page")) {
  pageId = document.body.getAttribute("data-page");
  navLinks.forEach(matchPage);
}

// Toggle MOW menu
let mowActive = false;
const headerNav = document.querySelector("header nav");

document.getElementById("header__mow-nav-trigger").onclick = function() {
  if (!mowActive) {
    headerNav.classList.add("nav--mow-active");
    mowActive = true;
  } else {
    headerNav.classList.remove("nav--mow-active");
    mowActive = false;
  }
}
