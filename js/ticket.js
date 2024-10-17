function createTicket() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const priority = document.getElementById('priority').value;

    console.log(`Ticket created: ${title}, ${description}, ${priority}`);
    // Implement ticket creation logic with API here
}
