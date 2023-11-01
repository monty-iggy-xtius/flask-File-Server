const input_value = document.getElementById('nuh');
const form = document.getElementById('form');
var errorMsg = document.getElementById('err-msg');
var typeMsg = document.getElementById('file-type-msg');
var sizeMsg = document.getElementById('file-size-msg');


form.addEventListener('submit', (e) => {
	// // prevent the form from submitting by default
e.preventDefault();
errorMsg.innerHTML = null;
//check if input field is empty
if(input_value.value == null || input_value.value == ''){
	typeMsg.innerHTML = null;
	sizeMsg.innerHTML = null;
	errorMsg.innerHTML = "please select a file";
}
else{
	errorMsg.innerHTML = null;
	var validated_form_input = new FormData(form);
	typeMsg.innerHTML = "Type: " + validated_form_input.get('coming').type;
	sizeMsg.innerHTML = "Size: " + Math.round(validated_form_input.get('coming').size/(1024*1024)) + "MB";
	
	var submit_form = form.submit();
	
	}

})
