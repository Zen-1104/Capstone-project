function ask_password() {
    var password = prompt("Enter admin password:");

    if (password === "Aawez123!") {
        window.location.href = "/admin?password=Aawez123!";
    } else {
        alert("Incorrect password");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");

    searchInput.addEventListener("keyup", function () {
        const filter = searchInput.value.toLowerCase();
        const rows = document.querySelectorAll(".admin-table tbody tr");

        rows.forEach(row => {
            const text = row.textContent.toLowerCase();

            if (text.includes(filter)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});