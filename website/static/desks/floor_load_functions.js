//Need to add on click-handling:

const canvas_backdrop = document.createElement('img');

function loadFloorImage(image_link, canvas) {
  const context = canvas.getContext('2d');
  canvas_backdrop.src = image_link;
  context.clearRect(0, 0, canvas.width, canvas.height);
	context.drawImage(canvas_backdrop, 0, 0);
};

export function createButtons(floor_array, btn_group, canvas) {
  
  btn_group.replaceChildren();
  
  for (var i = 0; i < floor_array.length; i++) {
    
    var btn = document.createElement('input');
    btn.type = 'radio';
    btn.name = 'floor_buttons';
    btn.id = 'floor_button' + i;
    btn.value = floor_array[i].plan;
	  if (i == 0) {
      btn.checked = true;
	  };
    btn.classList.add('checked');
    btn.addEventListener('click', function() {
      for (var sibling of this.parentNode.children) {
        sibling.classList.remove('checked');
      }
      this.classList.add('checked');
      loadFloorImage($("input:radio[name=floor_buttons][class=checked]:first").val(), canvas);
      console.log($("input:radio[name=floor_buttons][class=checked]:first").val());
    });
    
    var label = document.createElement('label');
    label.htmlFor = 'option' + i;
    label.appendChild(document.createTextNode(floor_array[i].name));
	  
    btn_group.appendChild(btn);
    btn_group.appendChild(label);
  };
};