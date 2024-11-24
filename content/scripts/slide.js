// The JS below is so you can click and drag to scroll on desktop
// @source https://codepen.io/thenutz/pen/VwYeYEE
const slider = document.querySelector(".slides");
let isDown = false;
let startY;
let scrollTop;

slider.addEventListener("pointerdown", (e) => {
	isDown = true;
	slider.classList.add("dragging");
	startY = e.pageY - slider.offsetTop;
	scrollTop = slider.scrollTop;
});
slider.addEventListener("pointerleave", () => {
	isDown = false;
	slider.classList.remove("dragging");
});
slider.addEventListener("pointerup", () => {
	isDown = false;
	slider.classList.remove("dragging");
});
slider.addEventListener("pointermove", (e) => {
	if (!isDown) return;
	e.preventDefault();
	const y = e.pageY - slider.offsetTop;
	const walk = (y - startY) * 3; //scroll-fast
	slider.scrollTop = scrollTop - walk;
});
