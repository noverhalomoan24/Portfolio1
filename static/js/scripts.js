
const tabmenu = document.querySelector(".tab-menu");

console.log(tabmenu)

function menuBtnFunction(menuBtn) {
    menuBtn.classList.toggle("active");
    tabmenu.classList.toggle("hidden-play");
    console.log(tabmenu);
}



