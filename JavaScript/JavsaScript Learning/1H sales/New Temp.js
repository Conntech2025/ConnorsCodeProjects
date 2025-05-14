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
		 { var num = prompt('Enter sales amount for the day ' + (i+1));
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
		
