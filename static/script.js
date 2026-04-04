function ask_password() {
    var password = prompt("Enter admin password:");
    
    if (password === "Aawez123!") {
        window.location.href = "/admin?password=Aawez123!";
    } else {
        alert("Incorrect password");
    }
}