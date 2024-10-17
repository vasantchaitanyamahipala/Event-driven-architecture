const tickets = [
    { title: 'Issue 1', status: 'Open' },
    { title: 'Issue 2', status: 'Closed' }
];

function renderTickets(filteredTickets) {
    const ticketList = document.getElementById('ticket-list');
    ticketList.innerHTML = '';
    filteredTickets.forEach(ticket => {
        const li = document.createElement('li');
        li.textContent = `${ticket.title} - ${ticket.status}`;
        ticketList.appendChild(li);
    });
}

function filterTickets() {
    const status = document.getElementById('status-filter').value;
    const filtered = status === 'All' ? tickets : tickets.filter(t => t.status === status);
    renderTickets(filtered);
}

filterTickets(); // Initial render
op