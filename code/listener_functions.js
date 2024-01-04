//HTML reference variables:
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const desired_period = document.getElementById

//Value-holder variables:
const backdrop = document.createElement('img');

//Function to update the floor plan interface when selected floor changes:
function updateCanvas(plan_image, desk_positions, desk_availability) {
	
	//Store the floor plan in the backdrop object:
	backdrop.src = plan_image;
	
	//Clear the canvas, then render the floor plan as a backdrop:
	context.clearRect(0, 0, canvas.width, canvas.height);
	context.drawImage(backdrop, 0, 0);
	
	console.log('drawn');
	
}

//Function to update the floor selection menu when selected site changes:
function updateFloorChoices(floor_objects) {
	
	//Identify and clear the floor_buttons element:
	var div = document.getElementById('floor_buttons');
	console.log(div);
	//div.replaceChildren();
	console.log(div);
	//div.innerHTML = '';
	
	//Insert the floor buttons in descending order and make the last active:
	for (var i = floor_objects.length - 1; i >= 0; i--) {
		
		var btn = document.createElement('button');
		btn.classList.add('btn', 'floor_btn', 'btn-outline-primary');
		if (i == 0) {
			btn.classList.add('active');
		}
		btn.setAttribute('value', floor_objects[i].get('name'));
		var plan = floor_objects[i].get('plan');
		btn.setAttribute('data-image', floor_objects[i].get('plan'));
		div.appendChild(btn);
		
	}
	var newElement2 = document.createElement("p");
	newElement2.textContent = "New Paragraph 2";
	div.appendChild(newElement2);
}