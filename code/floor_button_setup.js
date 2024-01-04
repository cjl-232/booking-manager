const map1 = new Map();
map1.set('name', 'B1');
map1.set('plan', 'sdmioa.img');
const arr = [map1, map1];

document.addEventListener('DOMContentLoaded', function() {
	console.log('Startup handled.');
		updateCanvas('floor_plans/friends.jpg', 1);
		//var buttons = document.querySelectorAll('.floor_btn');
		//var floor_plan = document.getElementById('floor_plan');
		//buttons.forEach(function(button) {
		//	button.addEventListener('click', function() {
		//		var value = this.getAttribute('data-image');
		//		floor_plan.textContent = value;
		//		buttons.forEach(function(button) {
		//			button.classList.remove('active');
		//		});
		//		this.classList.add('active');
		//		updateFloorChoices(arr);
		//	});
		//});
	});