// Initialize Syntax Highlighting
hljs.initHighlightingOnLoad();

// Add Selected class to nav link that matches page ID
const pageID = document.body.getAttribute("data-page");
document.querySelector(`nav li[data-page="${pageID}"]`).classList.add("header__content__nav__link--selected");
