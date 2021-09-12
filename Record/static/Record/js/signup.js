var token = null
var loading = null

window.onload = function(){
  loading = document.getElementById('loading')
  //loading.hidden = false
}

function validate(event) {
  console.log("Form Submission");

  var error = document.getElementById("message");
  console.log(error);
  var message = null;
  var form = event.target

  var values = form.elements
  token = values.csrfmiddlewaretoken.value;

  var email = values.email.value;
  var name = values.name.value;


  message = validateForm(form)
  if (message) {
    error.innerHTML = message;
    error.hidden = false;
  } else {
    error.innerHTML = "";
    error.hidden = true;
  
  }
  event.stopPropagation();
  return false;
}


//for validation
function validateForm(form){
  var values = form.elements;
  var name = values.name.value;
  token = values.csrfmiddlewaretoken.value;
  var message = null
  var phone = values.phone.value;
  var email = values.email.value;
  var password = values.password.value;


  
  if (!name.trim()) {
    message = "Name is required.";
  } 
  else if (!phone.trim()) {
    message = "Phone is required.";
  }
  else if (!email.trim()) {
    message = "Email is required.";
  } 
  else if (!password.trim()) {
    message = "Password is required.";
  } 

  return message

}

//for validation

function submitForm(){
  try{
    var form = document.getElementById('form')
    var message = validateForm(form)
    if(message){
    }else{
      form.submit()
    }
  }catch(err){
    console.log(err)
  }
}