// Handle form submission
document.getElementById("farmer-profile-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const bio = document.getElementById("bio").value;
    const location = document.getElementById("location").value;
    const products = document.getElementById("products").value;
    const image = document.getElementById("image").value;

    // Normally, you'd save this data to a server or database.
    // For now, we'll just log it to the console.
    console.log({
        name: name,
        bio: bio,
        location: location,
        products: products,
        image: image
    });

    // Show a success message
    alert("Profile saved successfully!");
    // Optionally, redirect to another page
    // window.location.href = "profile-view.html"; // If you have a profile view page
});
