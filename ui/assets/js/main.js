
function toggle_element(id){
	var element = document.getElementById(id);
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

function show_element(id){
	var element = document.getElementById(id);
	element.style.display = "block";

}

function hide_element(id){
	var element = document.getElementById(id);
	element.style.display = "none";
}

function initialise(){
	show_element("search_resuts");
	hide_element("post_offer_div");
	// hide all error inputs

}

function show_post_form(){
	show_element("post_offer_div");
	hide_element("search_resuts");
}

function validate_signup(){
	// values
	var name=document.forms["signup"]["name"];
	var email=document.forms["signup"]["email"];
	var password=document.forms["signup"]["password"];
	var confirm_password=document.forms["signup"]["confirm_password"];


	// error display objects
	var name_error=document.getElementById("name_error");
	var email_error=document.getElementById("email_error");
	var password_error=document.getElementById("password_error");
	var password_error2=document.getElementById("password_error2");

	name.addEventListener("blur",nameValidator,true)
	email.addEventListener("blur",emailValidator,true)
	password.addEventListener("blur",passwordValidator,true)
	confirm_password.addEventListener("blur",confirmValidator,true)

	if(name.value==""){
		name.style.border="1px solid #cea0a5";
		name_error.textContent="Name is required";
		name.focus()
		return false;
	}

	if(email.value==""){
		email.style.border="1px solid #cea0a5";
		email_error.textContent="Name is required";
		email.focus()
		return false;
	}

	if(password.value==""){
		password.style.border="1px solid #cea0a5";
		password_error.textContent="Name is required";
		password.focus()
		return false;
	}

	if(password.value !==confirm_password.value ){
		password.style.border="1px solid #cea0a5";
		password_error2.textContent="Name is required";
		confirm_password.focus()
		return false;
	}

}


function nameValidator(){
	if(name.value!=""){
		name.style.border=""
		name_error.innerHtml=""
		return true;
	}
}

function emailValidator(){
	if(email.value!=""){
		email.style.border=""
		email_error.innerHtml=""
		return true;
	}
}


function passwordValidator(){
	if(password.value!=""){
		password.style.border=""
		password_error.innerHtml=""
		return true;
	}
}

function confirmValidator(){
	if(confirm_password.value!=""){
		confirm_password.style.border=""
		password_error2.innerHtml=""
		return true;
	}
}