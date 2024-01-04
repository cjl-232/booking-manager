document.addEventListener('DOMContentLoaded', function() {
		var buttons = document.querySelectorAll('.floor_btn');
		var floor_plan = document.getElementById('floor_plan');
		buttons.forEach(function(button) {
			button.addEventListener('click', function() {
				var value = this.getAttribute('data-image');
			});
		});
	});

function toggleButton(button) {
	var group = button.closest('btn-group')
	let x = 3;
	var y = 14;
	console.log(y)
	console.log(button.innerText)
	console.log($('.btn-group-vertical > .btn.active')[0]);
}
