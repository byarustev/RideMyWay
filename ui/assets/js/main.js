// values
// global variables
var uname;
var email;
var password;
var confirm_password;

var name_error;
var email_error;
var password_error;
var password_error2;



window.onload = function(){
   	uname=document.getElementById("name");
	email=document.getElementById("email");
	password=document.getElementById("password");
	confirm_password=document.getElementById("confirm_password");
 	//add blur events
	uname.addEventListener("blur",nameValidator,true);
	email.addEventListener("blur",emailValidator,true);
	password.addEventListener("blur",passwordValidator,true);
	confirm_password.addEventListener("blur",confirmValidator,true);

		// error display objects
	name_error=document.getElementById("name_error");
	email_error=document.getElementById("email_error");
	password_error=document.getElementById("password_error");
	password_error2=document.getElementById("password_error2");

	name_error.style.visibility="hidden";
	email_error.style.visibility="hidden";
	password_error.style.visibility="hidden";
	password_error2.style.visibility="hidden";
 }






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
	
	if(uname.value==""){
		uname.style.border="1px solid #d63031";
		name_error.style.visibility="visible";
		name_error.textContent="* name is required";
		uname.focus()
		return false;
	}

	var reg=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

	if(email.value==""){
		email.style.border="1px solid #d63031";
		email_error.style.visibility="visible";
		email_error.textContent="* email is required";
		email.focus()
		return false;
		
	}else if(!reg.test(email.value)){
		email.style.border="1px solid #d63031";
		email_error.style.visibility="visible";
		email_error.textContent="* invalid email format";
		email.focus()
		return false;
	}

	if(password.value==""){
		password.style.border="1px solid #d63031";
		password_error.style.visibility="visible";
		password_error.textContent="* password is required";
		password.focus()
		return false;
	}

	if(password.value !=confirm_password.value ){
		password.style.border="1px solid #d63031";
		confirm_password.style.border="1px solid #d63031";
		password_error2.style.visibility="visible";
		password_error2.textContent="** password mismatch";
		confirm_password.focus()
		return false;
	}

}


function nameValidator(){
	if(uname.value!=""){
		uname.style.border="1px solid #d1d5da";
		name_error.innerHtml=""
		name_error.style.visibility="hidden";
		return true;
	}
}

function emailValidator(){
	if(email.value!=""){
		email.style.border="1px solid #d1d5da";
		email_error.innerHtml=""
		email_error.style.visibility="hidden";
		
		return true;
	}
}


function passwordValidator(){
	if(password.value!=""){
		password.style.border="1px solid #d1d5da"
		password_error.innerHtml=""
		password_error.style.visibility="hidden";
		
		return true;
	}
}

function confirmValidator(){
	if(confirm_password.value!=""){
		password.style.border="1px solid #d1d5da"
		confirm_password.style.border="1px solid #d1d5da"
		password_error2.innerHtml=""
		password_error2.style.visibility="hidden";
		
		return true;
	}
}