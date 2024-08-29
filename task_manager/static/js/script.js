function addRow() {  
    // Get input values  
    var item = document.getElementById("item").value;  
    var description = document.getElementById("description").value;  
    var location = document.getElementById("location").value;
    var date = document.getElementById("date").value;
    var status = document.getElementById("status").value;
    var note = document.getElementById("note").value;
    

    // Create a new row  
    var table = document.getElementById("dataTable");  
    var newRow = table.insertRow();  

    // Insert cells and set their values  
    var cell1 = newRow.insertCell(0);  
    var cell2 = newRow.insertCell(1);  
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6); // Action cell

    cell1.innerHTML = item;  
    cell2.innerHTML = description;  
    cell3.innerHTML = location;
    cell4.innerHTML = date;
    cell5.innerHTML = status;
    cell6.innerHTML = note;

    // Create update button
    var updateButton = document.createElement("button");
    updateButton.innerHTML = "Update";
    updateButton.onclick = function() {
        updateRow(newRow);
    };
    cell7.appendChild(updateButton);

    // Create delete button
    var deleteButton = document.createElement("button");
    deleteButton.innerHTML = "delete";
    deleteButton.onclick = function() {
        deleteRow(newRow);
    };
    cell7.appendChild(deleteButton)

    // Clear input fields  
    document.getElementById("item").value = "";  
    document.getElementById("description").value = "";  
    document.getElementById("location").value = "";
    document.getElementById("date").value = "";
    document.getElementById("status").value = "";
    document.getElementById("note").value = "";
} 