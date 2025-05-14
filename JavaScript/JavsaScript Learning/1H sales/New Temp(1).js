var totSum = 0.0;

function getData()
	{var arr = new Array();
	 var Names = new Array();
	 var outString = "";
	 var sum = 0.0;
	 var totSum = 0.0;
	 ;
	 var tableDiv = document.getElementById("Total");


	 for (var count = 0; count < 3; count++)
	     { outString = "";

	       outString = prompt('Enter employees name: ');
	       Names.push(outString);

	     for (var i = 0; i < 5; i++)
		 { var nume = prompt('Enter sales amount for the day ' + (i+1));
		 // push the value into the array
		   num = parseFloat(num);
		   sum += num;
	   	   outString += ", " + num ;

		 }
		arr.push(outString);
		totSum += sum;
		tableDiv.innerHTML = ">Full array: " + arr;
		tableDiv.innerHTML += ("<p>For " + Names[count]);
		tableDiv.innerHTML += (' [' + count + ',' + i + '] = ' + arr[count][i]);
		tableDiv.innerHTML += "<p>sum is " + sum.toFixed(2) ;
		arr.sort()
		tableDiv.innerHTML += "Full Sorted array: " + arr;


	}
	   tableDiv.innerHTML += "=== END OF REPORT ===";
}
		
<style>
body, html {
   height: 100%;
   font-family: Arial, Helvetica, sans-serif;
}
*  {
   box-sizing: border-box;
}
.bg-img {
   /* The image used */
   background-image: url("img_nature.jpg");

   min-height: 380px;

   /* Center and scale the image nicely */
   background-position: center;
   background-repeat: no-repeat;
   background-size: cover;
   position: relative;
}
/* Add styles to the form container */
.container {
   position: absolute;
   right: 0;
   margin: 20px;
   max-width: 300px;
   padding: 16px;
   background-color: white;
}
/* Full-width input fields *?
input[type=text], input[type=password] {
   width: 100%;
   padding: 15px;
   margin: 5px 0 22px 0;
   border: none;
   background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus {
   background-color: #ddd;
   outline: none;
}
/* Set a style for the submit button */
.btn {
   background-color: #04AA6D;
   color: white;
   padding: 16px 20px;
   border: none;
   cursor: pointer;
   width: 25%;
   opacity: 0.9;
}
.btn:hover {
   opacity: 1;
}
</style>

<style>
body, html   {
   height: 100%;
   font-family: Arial, Helvetica, sans-serif;
}
*  {
   box-sizing: border-box;
}
.bg-img   {
   /* The image used */
   background-image: url("img_nature.jpg");

   min-height: 380px;

   /* Center and scale the image nicely */
   background-position: center;
   background-repeat: nor-repeat;
   background-size: cover;
   position: relative;
}
/* Add styles to the form container */
.container {
   position: absolute;
   right: 0;
   margin: 20px;
   max-width: 300px;
   padding: 16px;
   background-color: white;
}
/* Full-width input fields */
input[type=text], input[type=password] {
   width: 100%;
   padding: 15px;
   margin: 5px 0 22px 0;
   border: none;
   background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus {
   background-color: #ddd;
   outline: none;
}
/* Set a style for the submit button */
.btn {
   background-color: #04AA6D;
   color: white;
   padding: 16px 20px;
   border: none;
   cursor: pointer;
   width: 25%;
   opacity: 0.9;
}
.btn:hover  {
   opacity: 1;
}
</style>
