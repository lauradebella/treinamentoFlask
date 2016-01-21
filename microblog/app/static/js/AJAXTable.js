var getTableDataAJAX = function() {

	var getTableData = new XMLHttpRequest();

	getTableData.onreadystatechange = function() {
		if(getTableData.readyState === 4) {
			var tableInfo     = JSON.parse(getTableData.responseText);
			var tableHeading  = tableInfo.tableHeading;
			var tableCellsPets   = tableInfo.tableCellsPets;
			var tableCellsPeople   = tableInfo.tableCellsPeople;

			var createTable = function() {
				//Create Table and Heading Rows 
				var newTable = document.createElement('table');
				var tableHeadingRow = document.createElement('tr');
				var tableHeader = document.createElement('th');
				tableHeadingRow.appendChild(tableHeader);

				//Create first row with header and data
				var tableRowFirst = document.createElement('tr');
				var tableRowFirstHead = document.createElement('th');
				tableRowFirst.appendChild(tableRowFirstHead);

				for (i = 1; i < tableCellsPets.length; i++) {
					//create new heading
					var petData = document.createElement('td');

					// append Heading to table
					tableRowFirst.appendChild(petData);

					//set new heading text content to json information
					petData.textContent = tableCellsPets[i];
				};

				var tableRowSecond = document.createElement('tr');
				var tableRowSecondHead = document.createElement('th');
				tableRowSecond.appendChild(tableRowSecondHead);

				for (i = 1; i < tableCellsPets.length; i++) {
					//create new heading
					var peopleData = document.createElement('td');

					// append Heading to table
					tableRowSecond.appendChild(peopleData);

					//set new heading text content to json information
					peopleData.textContent = tableCellsPeople[i];
				};

				// Add classes to elements
				newTable.classList.add('jsTable');
				tableHeader.classList.add('jsTableHead');
				tableRowFirstHead.classList.add('jsTableRowHead');
				tableRowSecondHead.classList.add('jsTableRowHead');

				//Add text content and colspan attribute to tableHeader
				tableHeader.textContent = tableHeading;
				tableHeader.setAttribute("colspan", "4");

				//Add text content to row headings
				tableRowFirstHead.textContent = tableCellsPets[0]
				tableRowSecondHead.textContent = tableCellsPeople[0];

				//Append table to DOM
				document.body.appendChild(newTable);

				//Append rows to new table
				newTable.appendChild(tableHeadingRow);
				newTable.appendChild(tableRowFirst);
				newTable.appendChild(tableRowSecond);
			}();
		};
	};
	getTableData.open("GET", "posts-json.txt" , true);
	getTableData.send();
};

//var wrapperDiv = document.querySelector('div');
//var AJAXbutton = document.getElementById('button');

//AJAXbutton.addEventListener('click', getTableDataAJAX);

getTableDataAJAX();