const express = require('express');
const path = require('path');
const app = express();

// To store expenses in memory (for demo purposes)
let expenses = [];

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    const alertMessage = req.query.alert || "";
    res.render('home', { alertMessage, expenses });
});

app.post('/add-expense', (req, res) => {
    const { title, amount } = req.body;

    // Add new expense to array
    expenses.push({ title, amount });

    // Redirect to home with success alert
    res.redirect('/?alert=Expense added successfully!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});



