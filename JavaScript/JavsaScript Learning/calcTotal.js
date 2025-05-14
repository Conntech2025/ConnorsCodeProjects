var cake_prices = new Array();
    cake_prices ["Round6"] = 20;
    cake_prices ["Round8"] = 25;
    cake_prices ["Round10"] = 35;
    cake_prices ["Round12"] = 75;

var filling_prices = new Array();
    filling_prices ["None"] = 0;
    filling_prices ["Lemon"] = 5;
    filling_prices ["Custard"] = 5;
    filling_prices ["Fudge"] = 7;
    filling_prices ["Mocha"] = 8;
    filling_prices ["Raspberry"] = 10;
    filling_prices ["Pineapple"] = 5;
    filling_prices ["Dobash"] = 9;
    filling_prices ["Mint"] = 5;
    filling_prices ["Cherry"] = 5;
    filling_prices ["Apricot"] = 8;
    filling_prices ["Buttercream"] = 7;
    filling_prices ["Chocolate Mousse"] = 12;

function getCakeSizePrice() {
	var cakeSizePrice = 0;
	var theForm = document.form["cakeform"];
	var selectCake = theForm.elements["selectedcake"];

	cakeSizePrice = cake_prices[selectedCake.value];

	return cakeSizePrize;
}


function getFillingPrice() {

	var cakeFillingPrice=0;
	var theForm = document.forms["cakeform"];
	var selectedFilling = theForm.elements["filling"];

	cakeFillingPrice = filling_prices[selectedFilling.value];

	return cakeFillingPrice;


function candlesPrice() {

	var candlePrice=0;
	var theForm = document.forms["cakeform"];
	var includeCandles = theForm.elements["includecandles"];

	if (includeCandles.checked == true) {
	    candlePrice = 5;
	}

	return candlePrice;
}


function inscriptionPrice() {
	var inscriptionPrice = 0;
	var theForm = document.forms["cakeform"];
	var includeInscription = theForm.elements["includeinscription"];

	if (includeinscription.checked == true) {
	    incriptionPrice = 20;
	}

	return inscriptionPrice;
}

function calculateTotal() {
	var cakePrice = getCakeSizePrice() + getFillingPrice() + candlePrice() + inscriptionPrice();

	var divobj = document.getElementByID('totalPrice');
	divobj.style.display = 'block';
	divobj.innerHTML = "Total Price for the Cake: $" + cakePrice;
	var username = document.getElementById("name").value;
	document.cookie = "username = "+ username;

	alert("name is "+ username);



}


function hideTotal() {
	var divobj = document.getElementById('totalPrice');
	divobj.style.display = 'none';
}

